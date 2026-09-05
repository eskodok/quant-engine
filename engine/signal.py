"""Signal engine: setup swing hari ini, hanya dari strategi yang sudah lolos validasi.

Alur: load -> scrub gate -> fitur -> sinyal di bar TUTUP terakhir -> setup.
Confidence bukan angka karangan: turunan dari PF OOS, verdict, regime, dan likuiditas.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path

import numpy as np
import pandas as pd

from .config import MARKETS, RiskConfig
from .scrub import scrub
from .strategy import STRATEGIES, Strategy, make_strategy

REPORT_DIR = Path(__file__).resolve().parent.parent / "reports"


@dataclass
class Setup:
    symbol: str
    market: str
    timeframe: str
    strategy: str
    as_of: str
    action: str          # LONG | NO_TRADE | AVOID_OR_EXIT (tren patah: jangan beli / keluar bila pegang)
    entry_ref: float     # close bar terakhir; eksekusi di open berikutnya
    entry_zone: tuple    # (low, high) toleransi entry
    stop: float
    target: float
    rr: float
    qty: float
    position_value: float
    risk_amount: float
    confidence: float    # 0-1
    confidence_notes: list
    reasons: list
    regime: str
    validation_verdict: str
    data_warnings: list


def load_validation(symbol: str, strategy: str) -> dict | None:
    p = REPORT_DIR / f"{symbol.replace('/', '-').replace(':', '_')}_{strategy}.json"
    if p.exists():
        return json.loads(p.read_text())
    return None


def save_validation(symbol: str, strategy: str, rep) -> Path:
    REPORT_DIR.mkdir(exist_ok=True)
    p = REPORT_DIR / f"{symbol.replace('/', '-').replace(':', '_')}_{strategy}.json"
    p.write_text(json.dumps({
        "verdict": rep.verdict, "best_params": rep.best_params, "oos": rep.oos_metrics,
        "oos_cost_x2": rep.oos_metrics_cost_x2, "dsr_prob": rep.dsr_prob, "n_trials": rep.n_trials,
        "random_pctile": rep.random_pctile, "pbo": rep.pbo, "benchmark": rep.benchmark,
        "reasons": rep.reasons, "generated": str(pd.Timestamp.now(tz="UTC"))}, indent=2, default=float))
    return p


def _confidence(val: dict | None, f_last: pd.Series, market_name: str) -> tuple[float, list]:
    notes = []
    if val is None:
        return 0.0, ["belum ada validasi walk-forward untuk simbol+strategi ini -> jalankan `validate` dulu"]
    v = val["verdict"]
    base = {"SHIP": 0.6, "FIX": 0.35, "SCRAP": 0.0}[v]
    notes.append(f"verdict validasi {v} -> basis {base:.2f}")
    pf = val["oos"].get("profit_factor", 0)
    adj = float(np.clip((min(pf, 2.0) - 1.15) / (2.0 - 1.15), 0, 1)) * 0.2
    base += adj
    notes.append(f"PF OOS {pf:.2f} -> +{adj:.2f}")
    if val.get("dsr_prob", 0) >= 0.9:
        base += 0.1; notes.append("deflated Sharpe >= 0.90 -> +0.10")
    if f_last["adx"] > 25:
        base += 0.05; notes.append(f"ADX {f_last['adx']:.0f} > 25 tren kuat -> +0.05")
    if f_last["atr_pct"] > 0.06:
        base -= 0.1; notes.append(f"ATR {f_last['atr_pct']:.1%} sangat tinggi -> -0.10")
    if market_name == "idx" and f_last["turnover_med"] < 2e9:
        base -= 0.15; notes.append(f"turnover median {f_last['turnover_med']/1e9:.1f} M/hari < 2M: likuiditas tipis -> -0.15")
    return float(np.clip(base, 0, 0.95)), notes


def generate(df: pd.DataFrame, symbol: str, market_name: str, timeframe: str,
             strategy: str = "trend_pullback", risk: RiskConfig = RiskConfig(),
             params: dict | None = None) -> Setup:
    market = MARKETS[market_name]
    rep = scrub(df, market, timeframe)
    if rep.blocked:
        raise RuntimeError("DATA GATE GAGAL — tidak ada sinyal dari data rusak:\n" + rep.to_markdown())
    warnings = [f"{c.name}: {c.detail}" for c in rep.warnings]

    val = load_validation(symbol, strategy)
    pooled = load_validation(f"POOLED_{market_name}_{timeframe}", strategy)
    p = params or (val or {}).get("best_params") or {}
    val_note = None
    if pooled and (val is None or val["verdict"] == "SCRAP") and pooled["verdict"] != "SCRAP":
        # per simbol gagal (biasanya karena sampel kecil) tapi basket lolos -> pakai bukti basket
        val_note = f"validasi per simbol {(val or {}).get('verdict', 'NONE')} -> memakai validasi basket {pooled['verdict']} " \
                   f"(PF OOS {pooled['oos'].get('profit_factor', 0):.2f}, {pooled['oos'].get('n_trades', 0)} trade)"
        val = pooled
    strat: Strategy = make_strategy(strategy, market_name, timeframe, **p)
    f = strat.features(df)
    sig = strat.signals(f)
    last, s = f.iloc[-1], sig.iloc[-1]
    regime = {1: "UPTREND", -1: "DOWNTREND", 0: "SIDEWAYS"}[int(last["regime"])]
    conf, notes = _confidence(val, last, market_name)
    if val_note:
        notes.insert(0, val_note)

    action = "LONG" if bool(s["entry"]) else ("AVOID_OR_EXIT" if bool(s["exit"]) else "NO_TRADE")
    entry_ref = float(last["close"])
    stop, target = float(s["stop"]), float(s["target"])
    if action == "LONG" and (val is None or val["verdict"] == "SCRAP"):
        action = "NO_TRADE"
        notes.append("sinyal entry ADA tapi strategi belum lolos validasi -> tidak direkomendasikan")
    risk_unit = entry_ref - stop
    if action == "LONG" and risk_unit > 0:
        qty = risk.risk_per_trade * risk.initial_equity / risk_unit
        qty = min(qty, risk.max_position_pct * risk.initial_equity / entry_ref)
        if market.lot_size:
            qty = float(np.floor(qty / market.lot_size) * market.lot_size)
        rr = (target - entry_ref) / risk_unit
    else:
        qty, rr = 0.0, 0.0
    tol = float(last["atr"]) * 0.25
    reasons = [s["reason"]] if s["reason"] else []
    reasons.append(f"regime {regime}, ADX {last['adx']:.0f}, RSI {last['rsi']:.0f}, "
                   f"close vs EMA20/50/200: {entry_ref/last['ema_fast']-1:+.1%}/{entry_ref/last['ema_mid']-1:+.1%}/{entry_ref/last['ema_slow']-1:+.1%}")
    if action == "NO_TRADE" and not s["entry"]:
        reasons.append("tidak ada setup: syarat entry strategi tidak terpenuhi di bar terakhir")
    if action == "AVOID_OR_EXIT":
        reasons.append("close < EMA50: tren patah. Bila pegang posisi -> exit di open berikutnya; bila tidak -> jangan beli")
    return Setup(symbol=symbol, market=market_name, timeframe=timeframe, strategy=strategy,
                 as_of=str(df.index[-1]), action=action, entry_ref=entry_ref,
                 entry_zone=(round(entry_ref - tol, 6), round(entry_ref + tol, 6)),
                 stop=stop, target=target, rr=float(rr), qty=qty, position_value=qty * entry_ref,
                 risk_amount=qty * risk_unit if action == "LONG" else 0.0,
                 confidence=conf, confidence_notes=notes, reasons=reasons, regime=regime,
                 validation_verdict=(val or {}).get("verdict", "NONE"), data_warnings=warnings)


def format_setup(s: Setup) -> str:
    L = [f"=== {s.symbol} [{s.market} {s.timeframe}] strategi={s.strategy} ===",
         f"bar tutup terakhir : {s.as_of}",
         f"AKSI               : {s.action}   (validasi: {s.validation_verdict}, confidence {s.confidence:.0%})",
         f"regime             : {s.regime}"]
    if s.action == "LONG":
        L += [f"entry (open bar berikutnya, zona) : {s.entry_zone[0]:,.6g} – {s.entry_zone[1]:,.6g}  (ref close {s.entry_ref:,.6g})",
              f"stop loss          : {s.stop:,.6g}  ({s.stop/s.entry_ref-1:+.2%})",
              f"take profit        : {s.target:,.6g}  ({s.target/s.entry_ref-1:+.2%})  RR 1:{s.rr:.1f}",
              f"qty                : {s.qty:,.6g}  nilai {s.position_value:,.0f}  risiko {s.risk_amount:,.0f}",
              "batalkan bila open bar berikutnya di luar zona entry (gap = RR rusak)"]
    L += ["alasan:"] + [f"  - {r}" for r in s.reasons]
    L += ["confidence:"] + [f"  - {n}" for n in s.confidence_notes]
    if s.data_warnings:
        L += ["peringatan data:"] + [f"  - {w}" for w in s.data_warnings]
    return "\n".join(L)


def to_json(s: Setup) -> str:
    return json.dumps(asdict(s), indent=2, default=float)
