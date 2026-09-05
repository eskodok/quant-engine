#!/usr/bin/env python3
"""CLI engine.

  python cli.py scrub    BTC/USDT --market crypto_spot --tf 4h
  python cli.py backtest BBCA     --market idx --tf 1d --strategy trend_pullback
  python cli.py validate BTC/USDT --market crypto_spot --tf 4h --strategy trend_pullback
  python cli.py signal   BTC/USDT --market crypto_spot --tf 4h --strategy trend_pullback
  python cli.py scan     BBCA BBRI TLKM ASII --market idx --tf 1d

Tambahkan --csv path.csv untuk memakai data sendiri, --synthetic untuk data uji.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from engine.config import MARKETS, RiskConfig  # noqa: E402
from engine.scrub import scrub, gate  # noqa: E402
from engine.strategy import STRATEGIES, make_strategy  # noqa: E402
from engine.backtest import run_backtest  # noqa: E402
from engine.metrics import summarize, monte_carlo_dd  # noqa: E402
from engine.validate import walk_forward  # noqa: E402
from engine.signal import generate, format_setup, to_json, save_validation, REPORT_DIR  # noqa: E402


def _load(sym: str, a) -> pd.DataFrame:
    if a.synthetic:
        from engine.synth import make_ohlcv
        return make_ohlcv(n=a.bars, timeframe=a.tf, seed=abs(hash(sym)) % 10_000,
                          continuous=MARKETS[a.market].continuous)
    if a.csv:
        from engine.data import load_csv
        return load_csv(a.csv, a.tf, continuous=MARKETS[a.market].continuous)
    from engine.data import load
    kw = {"limit_bars": a.bars} if a.market.startswith("crypto") else {}
    return load(sym, a.market, a.tf, cache=not a.no_cache, **kw)


def cmd_scrub(a):
    for sym in a.symbols:
        df = _load(sym, a)
        print(f"\n# {sym}\n" + scrub(df, MARKETS[a.market], a.tf).to_markdown())


def cmd_backtest(a):
    m = MARKETS[a.market]
    for sym in a.symbols:
        df = _load(sym, a)
        gate(df, m, a.tf)
        strat = make_strategy(a.strategy, a.market, a.tf)
        res = run_backtest(df, strat.run(df), m, RiskConfig(), cost_mult=a.cost_mult)
        met = summarize(res.trades, res.equity, m.bars_per_year[a.tf])
        mc = monte_carlo_dd(res.trades, RiskConfig().initial_equity)
        print(f"\n# {sym} {a.strategy} (parameter default, SELURUH data = in-sample, jangan dipercaya mentah)")
        for k, v in met.items():
            print(f"  {k:15s}: {v:.3f}" if isinstance(v, float) else f"  {k:15s}: {v}")
        print(f"  MC maxDD p50/p95: {mc['dd_p50']:.1%} / {mc['dd_p95']:.1%}")
        for w in res.warnings:
            print("  WARN:", w)
        if a.trades and len(res.trades):
            print(res.trades.tail(a.trades).to_string())


def cmd_validate(a):
    m = MARKETS[a.market]
    for sym in a.symbols:
        df = _load(sym, a)
        gate(df, m, a.tf)
        strat = make_strategy(a.strategy, a.market, a.tf)
        rep = walk_forward(df, strat, m, a.tf, symbol=sym, n_folds=a.folds)
        print(rep.to_markdown())
        p = save_validation(sym, a.strategy, rep)
        REPORT_DIR.mkdir(exist_ok=True)
        (REPORT_DIR / (p.stem + ".md")).write_text(rep.to_markdown())
        print(f"\n(tersimpan: {p})")


def cmd_signal(a):
    for sym in a.symbols:
        df = _load(sym, a)
        try:
            s = generate(df, sym, a.market, a.tf, a.strategy, risk=RiskConfig(initial_equity=a.equity))
        except RuntimeError as e:
            print(f"\n# {sym}\n{e}")
            continue
        print("\n" + (to_json(s) if a.json else format_setup(s)))


def cmd_scan(a):
    rows = []
    for sym in a.symbols:
        try:
            df = _load(sym, a)
            s = generate(df, sym, a.market, a.tf, a.strategy, risk=RiskConfig(initial_equity=a.equity))
            rows.append({"symbol": sym, "action": s.action, "regime": s.regime, "conf": f"{s.confidence:.0%}",
                         "close": s.entry_ref, "stop": s.stop if s.action == "LONG" else None,
                         "target": s.target if s.action == "LONG" else None, "val": s.validation_verdict})
        except Exception as e:  # satu simbol rusak tidak boleh mematikan scan
            rows.append({"symbol": sym, "action": "ERROR", "regime": str(e).splitlines()[0][:60]})
    print(pd.DataFrame(rows).to_string(index=False))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name, fn in (("scrub", cmd_scrub), ("backtest", cmd_backtest), ("validate", cmd_validate),
                     ("signal", cmd_signal), ("scan", cmd_scan)):
        p = sub.add_parser(name)
        p.add_argument("symbols", nargs="+")
        p.add_argument("--market", choices=list(MARKETS), default="crypto_spot")
        p.add_argument("--tf", default="4h")
        p.add_argument("--strategy", choices=list(STRATEGIES), default="trend_pullback")
        p.add_argument("--bars", type=int, default=3000)
        p.add_argument("--csv")
        p.add_argument("--synthetic", action="store_true")
        p.add_argument("--no-cache", action="store_true")
        p.add_argument("--cost-mult", type=float, default=1.0)
        p.add_argument("--folds", type=int, default=5)
        p.add_argument("--trades", type=int, default=0, help="tampilkan N trade terakhir")
        p.add_argument("--json", action="store_true")
        p.add_argument("--equity", type=float, default=100_000_000, help="modal untuk sizing (IDR/USDT)")
        p.set_defaults(fn=fn)
    a = ap.parse_args()
    if a.market == "idx" and a.tf != "1d":
        ap.error("IDX hanya mendukung --tf 1d")
    a.fn(a)


if __name__ == "__main__":
    main()
