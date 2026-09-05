"""Validasi: walk-forward, uji lookahead, stress biaya, Monte Carlo, deflated Sharpe.

Output akhir: verdict SHIP / FIX / SCRAP + alasan. Signal engine hanya mau
memakai strategi yang verdict-nya SHIP (atau FIX dengan override eksplisit).
"""
from __future__ import annotations

import itertools
from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from .backtest import run_backtest
from .config import MarketProfile, RiskConfig, ValidationThresholds
from .features import assert_no_lookahead
from .metrics import deflated_sharpe, monte_carlo_dd, summarize
from .strategy import Strategy


@dataclass
class ValidationReport:
    strategy: str
    symbol: str
    verdict: str = "SCRAP"
    reasons: list = field(default_factory=list)
    is_metrics: dict = field(default_factory=dict)
    oos_metrics: dict = field(default_factory=dict)
    oos_metrics_cost_x2: dict = field(default_factory=dict)
    folds: list = field(default_factory=list)
    best_params: dict = field(default_factory=dict)
    param_stability: float = 0.0
    dsr_prob: float = 0.0
    monte_carlo: dict = field(default_factory=dict)
    n_trials: int = 0
    random_pctile: float = float("nan")  # persentil PF strategi vs distribusi entry-acak (0-100)
    pbo: float = float("nan")            # Probability of Backtest Overfitting (CSCV, Bailey et al. 2015)
    benchmark: dict = field(default_factory=dict)  # buy&hold pada jendela OOS yang sama
    oos_trades: pd.DataFrame | None = None
    oos_equity: pd.Series | None = None

    def to_markdown(self) -> str:
        o, i = self.oos_metrics, self.is_metrics
        x2 = self.oos_metrics_cost_x2
        rows = [
            ("Trades", i.get("n_trades", 0), o.get("n_trades", 0), x2.get("n_trades", 0)),
            ("Profit factor", i.get("profit_factor", 0), o.get("profit_factor", 0), x2.get("profit_factor", 0)),
            ("Win rate", i.get("win_rate", 0), o.get("win_rate", 0), x2.get("win_rate", 0)),
            ("Expectancy (R)", i.get("expectancy_r", 0), o.get("expectancy_r", 0), x2.get("expectancy_r", 0)),
            ("Sharpe", i.get("sharpe", 0), o.get("sharpe", 0), x2.get("sharpe", 0)),
            ("Max DD", i.get("max_dd", 0), o.get("max_dd", 0), x2.get("max_dd", 0)),
            ("CAGR", i.get("cagr", 0), o.get("cagr", 0), x2.get("cagr", 0)),
        ]
        md = [f"## Validasi {self.strategy} @ {self.symbol}", "",
              f"**Verdict: {self.verdict}**", ""]
        md += [f"- {r}" for r in self.reasons]
        md += ["", "| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |", "|---|---|---|---|"]
        for name, a, b, c2 in rows:
            fmt = (lambda v: f"{v:.2f}") if name not in ("Trades",) else (lambda v: f"{int(v)}")
            if name in ("Win rate", "Max DD", "CAGR"):
                fmt = lambda v: f"{v:.1%}"
            md.append(f"| {name} | {fmt(a)} | {fmt(b)} | {fmt(c2)} |")
        md += ["", f"- Deflated Sharpe prob (n_trials={self.n_trials}): {self.dsr_prob:.2f}",
               f"- Timing vs entry acak: persentil {self.random_pctile:.0f} (harus >= 75)",
               f"- Probability of Backtest Overfitting (CSCV): {self.pbo:.2f} (harus < 0.5)",
               (f"- Buy & hold jendela OOS: return {self.benchmark.get('bh_return', 0):+.1%}, Sharpe {self.benchmark.get('bh_sharpe', 0):.2f}, "
                f"maxDD {self.benchmark.get('bh_max_dd', 0):.1%} | strategi: return {self.benchmark.get('strat_return', 0):+.1%}, "
                f"Sharpe {self.oos_metrics.get('sharpe', 0):.2f}, maxDD {self.oos_metrics.get('max_dd', 0):.1%}" if self.benchmark else "- Benchmark: n/a"),
               f"- Stabilitas parameter antar fold: {self.param_stability:.0%}",
               f"- Monte Carlo max DD: median {self.monte_carlo.get('dd_p50', 0):.1%}, p95 {self.monte_carlo.get('dd_p95', 0):.1%}",
               f"- Parameter terpilih (fold terakhir): {self.best_params}", "", "### Fold"]
        md += ["| # | Train | Test | Params | IS PF | OOS PF | OOS trades |", "|---|---|---|---|---|---|---|"]
        for k, f in enumerate(self.folds):
            md.append(f"| {k+1} | {f['train'][0].date()}→{f['train'][1].date()} | {f['test'][0].date()}→{f['test'][1].date()} | "
                      f"{f['params']} | {f['is_pf']:.2f} | {f['oos_pf']:.2f} | {f['oos_trades']} |")
        return "\n".join(md)


def _score(m: dict, min_trades: int = 15) -> float:
    """Skor optimasi: expectancy dikali akar jumlah trade; PF < 1 atau trade sedikit -> penalti."""
    if m["n_trades"] < min_trades:
        return -1e9 + m["n_trades"]
    pf = min(m["profit_factor"], 5.0)
    return m["expectancy_r"] * np.sqrt(m["n_trades"]) * (1 if pf > 1 else 0.1)


def grid_search(df: pd.DataFrame, strat: Strategy, market: MarketProfile, risk: RiskConfig,
                bars_per_year: int) -> tuple[dict, dict, int]:
    keys = list(strat.grid.keys())
    best, best_m, best_s = None, None, -np.inf
    n = 0
    for combo in itertools.product(*(strat.grid[k] for k in keys)):
        p = dict(zip(keys, combo))
        n += 1
        s = strat.with_params(**p)
        res = run_backtest(df, s.run(df), market, risk)
        m = summarize(res.trades, res.equity, bars_per_year)
        sc = _score(m)
        if sc > best_s:
            best, best_m, best_s = p, m, sc
    return best or {}, best_m or {}, n


def random_entry_pctile(seg: pd.DataFrame, sig: pd.DataFrame, market: MarketProfile, risk: RiskConfig,
                        bars_per_year: int, actual_pf: float, n_sims: int = 100, seed: int = 0) -> float:
    """Persentil PF strategi terhadap PF dari entry ACAK dengan jumlah entry, stop, target,
    dan aturan exit yang sama. Menjawab: apakah *timing* entry bernilai, atau hanya arus pasar?"""
    rng = np.random.default_rng(seed)
    n_entry = int(sig["entry"].sum())
    if n_entry < 3:
        return float("nan")
    valid = np.where(np.isfinite(sig["stop"].values) & np.isfinite(sig["target"].values))[0]
    if len(valid) < n_entry:
        return float("nan")
    pfs = []
    col = sig.columns.get_loc("entry")
    for _ in range(n_sims):
        r = sig.copy()
        r.iloc[:, col] = False
        r.iloc[rng.choice(valid, size=n_entry, replace=False), col] = True
        res = run_backtest(seg, r, market, risk)
        m = summarize(res.trades, res.equity, bars_per_year)
        pfs.append(min(m["profit_factor"], 10.0))
    pfs = np.array(pfs)
    return float((pfs < min(actual_pf, 10.0)).mean() * 100)


def pbo_cscv(df: pd.DataFrame, strat: Strategy, market: MarketProfile, risk: RiskConfig,
             n_blocks: int = 8) -> float:
    """Probability of Backtest Overfitting via Combinatorially Symmetric Cross-Validation.
    Semua kombinasi grid dijalankan di seluruh data -> matriks return per bar (T x N).
    Untuk tiap pembagian n_blocks/2 blok IS vs sisanya OOS: pilih kombinasi terbaik di IS,
    lihat peringkat OOS-nya. PBO = proporsi kasus peringkat OOS di bawah median."""
    keys = list(strat.grid.keys())
    combos = list(itertools.product(*(strat.grid[k] for k in keys)))
    if len(combos) < 2:
        return float("nan")
    cols = []
    for combo in combos:
        s_ = strat.with_params(**dict(zip(keys, combo)))
        res = run_backtest(df, s_.run(df), market, risk)
        cols.append(res.equity.pct_change().fillna(0.0).values)
    M = np.column_stack(cols)  # T x N
    T, N = M.shape
    blocks = np.array_split(np.arange(T), n_blocks)
    half = n_blocks // 2
    n_below = 0; n_tot = 0
    def sharpe(x):
        sd = x.std(axis=0); mu = x.mean(axis=0)
        return np.where(sd > 0, mu / np.where(sd > 0, sd, 1), -np.inf)
    for is_idx in itertools.combinations(range(n_blocks), half):
        is_rows = np.concatenate([blocks[b] for b in is_idx])
        oos_rows = np.concatenate([blocks[b] for b in range(n_blocks) if b not in is_idx])
        best = int(np.argmax(sharpe(M[is_rows])))
        oos_sr = sharpe(M[oos_rows])
        rank = (oos_sr < oos_sr[best]).sum() + 1  # 1 = terburuk
        w = rank / (N + 1)
        n_below += (w <= 0.5); n_tot += 1
    return float(n_below / n_tot)


def walk_forward(df: pd.DataFrame, strat: Strategy, market: MarketProfile, timeframe: str,
                 symbol: str = "", risk: RiskConfig = RiskConfig(), n_folds: int = 5,
                 train_frac: float = 0.6, th: ValidationThresholds = ValidationThresholds(),
                 warmup: int = 250) -> ValidationReport:
    """Anchored-rolling walk-forward: data dibagi n_folds blok test berurutan;
    tiap blok test dioptimasi hanya dari data SEBELUM blok itu (rolling window).
    """
    bpy = market.bars_per_year[timeframe]
    rep = ValidationReport(strategy=strat.name, symbol=symbol)

    # 0. uji lookahead pada pipeline fitur+sinyal (harga masa depan diacak, sinyal lama harus sama)
    try:
        assert_no_lookahead(lambda d: strat.run(d).drop(columns=["reason"]), df)
        rep.reasons.append("Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)")
    except AssertionError as e:
        rep.reasons.append(f"Uji lookahead: GAGAL — {e}")
        rep.verdict = "SCRAP"
        return rep

    n = len(df)
    usable = n - warmup
    test_len = int(usable * (1 - train_frac) / n_folds)
    train_len = int(usable * train_frac)
    if test_len < 60:
        rep.reasons.append(f"Data terlalu pendek untuk {n_folds} fold (test_len={test_len} bar)")
        return rep

    oos_trades, oos_eq, is_metrics_list, params_list = [], [], [], []
    n_trials_total = 0
    start_test = warmup + train_len
    for k in range(n_folds):
        t0, t1 = start_test + k * test_len, min(start_test + (k + 1) * test_len, n)
        tr0 = max(0, t0 - train_len - warmup)
        train = df.iloc[tr0:t0]
        best, best_m, ntr = grid_search(train, strat, market, risk, bpy)
        n_trials_total += ntr
        if not best:
            continue
        s = strat.with_params(**best)
        # OOS: fitur dihitung dengan warmup dari data sebelum t0 (tanpa mengintip setelah t1)
        seg = df.iloc[max(0, t0 - warmup):t1]
        sig = s.run(seg).iloc[t0 - max(0, t0 - warmup):]
        seg_test = seg.loc[sig.index]
        res = run_backtest(seg_test, sig, market, risk)
        m = summarize(res.trades, res.equity, bpy)
        rep.folds.append({"train": (train.index[0], train.index[-1]), "test": (seg_test.index[0], seg_test.index[-1]),
                          "params": best, "is_pf": best_m.get("profit_factor", 0), "oos_pf": m["profit_factor"],
                          "oos_trades": m["n_trades"]})
        is_metrics_list.append(best_m)
        params_list.append(best)
        if len(res.trades):
            oos_trades.append(res.trades)
        oos_eq.append(res.equity / res.equity.iloc[0])

    if not oos_eq:
        rep.reasons.append("Tidak ada fold yang menghasilkan parameter valid")
        return rep

    # gabungkan OOS: equity disambung secara geometris
    eq = stitch(oos_eq, risk.initial_equity)
    trades = pd.concat(oos_trades, ignore_index=True) if oos_trades else pd.DataFrame(columns=["pnl", "r_multiple", "bars"])
    rep.oos_trades, rep.oos_equity = trades, eq
    rep.oos_metrics = summarize(trades, eq, bpy)
    rep.is_metrics = {k: float(np.mean([m.get(k, 0) for m in is_metrics_list])) for k in is_metrics_list[0]}
    rep.best_params = params_list[-1]
    rep.n_trials = n_trials_total
    # stabilitas: proporsi fold yang memilih parameter sama dengan modus
    keyed = [tuple(sorted(p.items())) for p in params_list]
    rep.param_stability = keyed.count(max(set(keyed), key=keyed.count)) / len(keyed)

    # stress biaya x2 pada OOS dengan parameter per fold
    x2_tr, x2_eq = [], []
    for k, f in enumerate(rep.folds):
        s = strat.with_params(**f["params"])
        t0 = df.index.get_loc(f["test"][0]); t1 = df.index.get_loc(f["test"][1]) + 1
        seg = df.iloc[max(0, t0 - warmup):t1]
        sig = s.run(seg).iloc[t0 - max(0, t0 - warmup):]
        res = run_backtest(seg.loc[sig.index], sig, market, risk, cost_mult=th.cost_stress_multiplier)
        if len(res.trades):
            x2_tr.append(res.trades)
        x2_eq.append(res.equity / res.equity.iloc[0])
    eq2 = stitch(x2_eq, risk.initial_equity)
    tr2 = pd.concat(x2_tr, ignore_index=True) if x2_tr else pd.DataFrame(columns=["pnl", "r_multiple", "bars"])
    rep.oos_metrics_cost_x2 = summarize(tr2, eq2, bpy)

    o = rep.oos_metrics
    rep.dsr_prob = deflated_sharpe(o["sharpe"], len(eq), bpy, max(n_trials_total, 1), o.get("skew", 0), o.get("kurt", 3) + 3)
    rep.monte_carlo = monte_carlo_dd(trades, risk.initial_equity)
    # baseline entry acak: sinyal OOS tiap fold digabung (parameter per fold), entry diacak
    segs, sigs = [], []
    for f in rep.folds:
        s_ = strat.with_params(**f["params"])
        t0 = df.index.get_loc(f["test"][0]); t1 = df.index.get_loc(f["test"][1]) + 1
        seg = df.iloc[max(0, t0 - warmup):t1]
        sg = s_.run(seg).iloc[t0 - max(0, t0 - warmup):]
        segs.append(seg.loc[sg.index]); sigs.append(sg)
    if segs:
        rep.random_pctile = random_entry_pctile(pd.concat(segs), pd.concat(sigs), market, risk, bpy, o["profit_factor"])
        allseg = pd.concat(segs)
        bh = allseg.close / allseg.close.iloc[0]
        bh_r = bh.pct_change().dropna()
        rep.benchmark = {"bh_return": float(bh.iloc[-1] - 1),
                         "bh_sharpe": float(bh_r.mean() / bh_r.std() * np.sqrt(bpy)) if bh_r.std() > 0 else 0.0,
                         "bh_max_dd": float(((bh - bh.cummax()) / bh.cummax()).min()),
                         "strat_return": float(o.get("total_return", 0.0))}
    try:
        rep.pbo = pbo_cscv(df, strat, market, risk)
    except Exception:  # noqa: BLE001
        rep.pbo = float("nan")

    # ---- verdict ----
    fails, warns = [], []
    if o["n_trades"] < th.min_trades_oos:
        fails.append(f"trade OOS {o['n_trades']} < {th.min_trades_oos}: belum cukup bukti")
    if o["profit_factor"] < th.min_oos_profit_factor:
        fails.append(f"PF OOS {o['profit_factor']:.2f} < {th.min_oos_profit_factor}")
    is_pf, oos_pf = rep.is_metrics.get("profit_factor", 0), o["profit_factor"]
    if is_pf < th.min_is_profit_factor:
        fails.append(f"PF in-sample {is_pf:.2f} < {th.min_is_profit_factor}: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan")
    if is_pf > 0 and np.isfinite(is_pf) and (is_pf - oos_pf) / is_pf > th.max_oos_degradation:
        fails.append(f"degradasi IS→OOS {(is_pf - oos_pf) / is_pf:.0%} > {th.max_oos_degradation:.0%}: indikasi overfit")
    if rep.oos_metrics_cost_x2["profit_factor"] < 1.0:
        fails.append(f"PF OOS dengan biaya x{th.cost_stress_multiplier} = {rep.oos_metrics_cost_x2['profit_factor']:.2f} < 1: edge habis dimakan biaya")
    if np.isfinite(rep.random_pctile) and rep.random_pctile < th.min_random_pctile:
        fails.append(f"timing entry tidak lebih baik dari acak (persentil {rep.random_pctile:.0f} < {th.min_random_pctile:.0f}): hasil = arus pasar, bukan sinyal")
    if np.isfinite(rep.pbo) and rep.pbo >= th.max_pbo:
        fails.append(f"PBO {rep.pbo:.2f} >= {th.max_pbo}: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)")
    elif np.isfinite(rep.pbo) and rep.pbo >= th.max_pbo * 0.6:
        warns.append(f"PBO {rep.pbo:.2f} agak tinggi")
    if rep.benchmark and o.get("sharpe", 0) < rep.benchmark.get("bh_sharpe", 0):
        warns.append(f"Sharpe OOS {o.get('sharpe', 0):.2f} < buy&hold {rep.benchmark['bh_sharpe']:.2f}: belum lebih baik dari sekadar memegang aset")
    if rep.dsr_prob < th.min_deflated_sharpe_prob:
        warns.append(f"deflated Sharpe prob {rep.dsr_prob:.2f} < {th.min_deflated_sharpe_prob}: Sharpe bisa hasil kebetulan")
    ppt = strat.n_params / max(o["n_trades"], 1) * 100
    if ppt > th.max_params_per_100_trades:
        warns.append(f"{strat.n_params} parameter untuk {o['n_trades']} trade OOS ({ppt:.1f}/100 trade)")
    if rep.param_stability < 0.5:
        warns.append(f"parameter tidak stabil antar fold ({rep.param_stability:.0%})")

    # SCRAP = edge tidak ada / habis oleh biaya. FIX = edge ada tapi bukti belum cukup.
    hard_fail = (o["profit_factor"] < th.min_oos_profit_factor or is_pf < th.min_is_profit_factor
                 or rep.oos_metrics_cost_x2["profit_factor"] < 1.0
                 or o["n_trades"] < th.min_trades_oos // 3
                 or (np.isfinite(rep.random_pctile) and rep.random_pctile < th.min_random_pctile)
                 or (np.isfinite(rep.pbo) and rep.pbo >= th.max_pbo))
    if fails:
        rep.verdict = "SCRAP" if hard_fail else "FIX"
    elif warns:
        rep.verdict = "FIX"
    else:
        rep.verdict = "SHIP"
    rep.reasons += [f"GAGAL: {f}" for f in fails] + [f"PERINGATAN: {w}" for w in warns]
    if not fails and not warns:
        rep.reasons.append("Semua uji lulus: OOS profitable, tahan biaya x2, tidak overfit, parameter stabil")
    return rep


def stitch(eqs: list[pd.Series], initial: float) -> pd.Series:
    """Sambung kurva equity antar fold secara geometris (tiap fold sudah dinormalisasi ke 1)."""
    out, mult = [], 1.0
    for e in eqs:
        out.append(e * mult)
        mult *= float(e.iloc[-1])
    return pd.concat(out) * initial


# ---------------------------------------------------------------------------
# Validasi gabungan (pooled): satu strategi diuji pada sekumpulan simbol dalam
# market yang sama. Trade OOS digabung -> bukti statistik jauh lebih kuat daripada
# per simbol (strategi swing per simbol biasanya hanya 5-30 trade OOS).
# ---------------------------------------------------------------------------
def pool_reports(reps: list, bars_per_year: int, risk: RiskConfig = RiskConfig(),
                 th: ValidationThresholds = ValidationThresholds(), label: str = "") -> ValidationReport:
    reps = [r for r in reps if r.oos_trades is not None and len(r.oos_trades)]
    out = ValidationReport(strategy=reps[0].strategy if reps else "?", symbol=label or "POOLED")
    if not reps:
        out.reasons.append("tidak ada laporan OOS yang bisa digabung")
        return out
    trades = pd.concat([r.oos_trades for r in reps], ignore_index=True).sort_values("exit_ts")
    # kurva equity gabungan BERBASIS WAKTU: modal dibagi rata, kurva tiap simbol (dinormalisasi)
    # disejajarkan per tanggal lalu dirata-rata -> Sharpe/DD/CAGR yang bermakna.
    curves = [(r.oos_equity / r.oos_equity.iloc[0]) for r in reps if r.oos_equity is not None]
    idx = sorted(set().union(*[c.index for c in curves]))
    aligned = pd.concat([c.reindex(idx).ffill().fillna(1.0) for c in curves], axis=1)
    eq = aligned.mean(axis=1) * risk.initial_equity
    out.oos_metrics = summarize(trades, eq, bars_per_year)
    out.oos_trades, out.oos_equity = trades, eq
    # biaya x2: hitung ulang dari laporan per simbol
    x2 = [r.oos_metrics_cost_x2 for r in reps if r.oos_metrics_cost_x2]
    out.oos_metrics_cost_x2 = {"profit_factor": float(np.mean([m.get("profit_factor", 0) for m in x2])) if x2 else 0.0,
                               "n_trades": int(sum(m.get("n_trades", 0) for m in x2))}
    out.is_metrics = {k: float(np.mean([r.is_metrics.get(k, 0) for r in reps])) for k in reps[0].is_metrics}
    out.n_trials = max(r.n_trials for r in reps)
    pct = [r.random_pctile for r in reps if np.isfinite(r.random_pctile)]
    out.random_pctile = float(np.mean(pct)) if pct else float("nan")
    pb = [r.pbo for r in reps if np.isfinite(r.pbo)]
    out.pbo = float(np.mean(pb)) if pb else float("nan")
    bms = [r.benchmark for r in reps if r.benchmark]
    if bms:
        out.benchmark = {k: float(np.mean([b[k] for b in bms])) for k in bms[0]}
    out.param_stability = float(np.mean([r.param_stability for r in reps]))
    out.folds = []
    o = out.oos_metrics
    # DSR pada seri R-multiple per trade (n_obs = jumlah trade)
    rm = trades.r_multiple.dropna()
    sr_trade = float(rm.mean() / rm.std()) if len(rm) > 2 and rm.std() > 0 else 0.0
    out.dsr_prob = deflated_sharpe(sr_trade, len(rm), 1, out.n_trials, float(rm.skew()), float(rm.kurt()) + 3)
    out.monte_carlo = monte_carlo_dd(trades, risk.initial_equity * len(reps))
    fails, warns = [], []
    if o["n_trades"] < th.min_trades_oos:
        fails.append(f"trade OOS gabungan {o['n_trades']} < {th.min_trades_oos}")
    if o["profit_factor"] < th.min_oos_profit_factor:
        fails.append(f"PF OOS gabungan {o['profit_factor']:.2f} < {th.min_oos_profit_factor}")
    is_pf, oos_pf = out.is_metrics.get("profit_factor", 0), o["profit_factor"]
    if is_pf < th.min_is_profit_factor:
        fails.append(f"PF in-sample {is_pf:.2f} < {th.min_is_profit_factor}: OOS untung = kebetulan rezim, bukan edge")
    if is_pf > 0 and np.isfinite(is_pf) and (is_pf - oos_pf) / is_pf > th.max_oos_degradation:
        fails.append(f"degradasi IS→OOS {(is_pf - oos_pf) / is_pf:.0%} > {th.max_oos_degradation:.0%}")
    if out.oos_metrics_cost_x2["profit_factor"] < 1.0:
        fails.append(f"PF rata-rata dengan biaya x2 = {out.oos_metrics_cost_x2['profit_factor']:.2f} < 1")
    if np.isfinite(out.random_pctile) and out.random_pctile < th.min_random_pctile:
        fails.append(f"timing entry tidak lebih baik dari acak (rata-rata persentil {out.random_pctile:.0f} < {th.min_random_pctile:.0f})")
    if np.isfinite(out.pbo) and out.pbo >= th.max_pbo:
        fails.append(f"PBO rata-rata {out.pbo:.2f} >= {th.max_pbo}: overfit")
    if out.benchmark and o.get("sharpe", 0) < out.benchmark.get("bh_sharpe", 0):
        warns.append(f"Sharpe OOS {o.get('sharpe', 0):.2f} < rata-rata buy&hold {out.benchmark['bh_sharpe']:.2f}")
    if out.dsr_prob < th.min_deflated_sharpe_prob:
        warns.append(f"deflated Sharpe prob {out.dsr_prob:.2f} < {th.min_deflated_sharpe_prob}")
    if out.param_stability < 0.5:
        warns.append(f"parameter tidak stabil antar fold ({out.param_stability:.0%})")
    n_pos = sum(1 for r in reps if r.oos_metrics.get("profit_factor", 0) > 1)
    if n_pos < len(reps) / 2:
        warns.append(f"hanya {n_pos}/{len(reps)} simbol profitable OOS: edge tidak merata")
    n_bad = sum(1 for r in reps if (np.isfinite(r.pbo) and r.pbo >= th.max_pbo)
                or (np.isfinite(r.random_pctile) and r.random_pctile < th.min_random_pctile))
    if n_bad >= len(reps) / 2:
        fails.append(f"{n_bad}/{len(reps)} simbol gagal PBO atau tes acak: basket tidak boleh menutupi kegagalan mayoritas")
    hard_fail = (oos_pf < th.min_oos_profit_factor or is_pf < th.min_is_profit_factor or out.oos_metrics_cost_x2["profit_factor"] < 1.0
                 or o["n_trades"] < th.min_trades_oos // 3
                 or (np.isfinite(out.random_pctile) and out.random_pctile < th.min_random_pctile)
                 or (np.isfinite(out.pbo) and out.pbo >= th.max_pbo) or n_bad >= len(reps) / 2)
    out.verdict = "SCRAP" if (fails and hard_fail) else ("FIX" if fails or warns else "SHIP")
    out.reasons = [f"Gabungan {len(reps)} simbol: " + ", ".join(r.symbol for r in reps)]
    out.reasons += [f"GAGAL: {f}" for f in fails] + [f"PERINGATAN: {w}" for w in warns]
    if not fails and not warns:
        out.reasons.append("Semua uji lulus pada basket gabungan")
    return out
