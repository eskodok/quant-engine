#!/usr/bin/env python3
"""Validasi walk-forward mingguan untuk semua item watchlist -> reports/<simbol>_<strategi>.{json,md}
dan ringkasan reports/validation_summary.md. Dijalankan GitHub Actions tiap Minggu malam."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from engine.config import MARKETS  # noqa: E402
from engine.data import load_csv  # noqa: E402
from engine.scrub import scrub  # noqa: E402
from engine.signal import REPORT_DIR, load_validation, save_validation  # noqa: E402
from engine.strategy import STRATEGIES  # noqa: E402
from engine.validate import pool_reports, walk_forward  # noqa: E402
from engine.watchlist import read_watchlist  # noqa: E402


def main() -> int:
    REPORT_DIR.mkdir(exist_ok=True)
    now = pd.Timestamp.now(tz="UTC")
    groups: dict = {}
    lines = [f"# Validasi mingguan — {now:%Y-%m-%d} ", "", "| Simbol | Strategi | Verdict | Sebelumnya | PF OOS | Trade OOS | DSR | Alasan utama |", "|---|---|---|---|---|---|---|---|"]
    for it in read_watchlist():
        prev = (load_validation(it.symbol, it.strategy) or {}).get("verdict", "-")
        if not it.csv_path.exists():
            lines.append(f"| {it.symbol} | {it.strategy} | NO_DATA | {prev} | | | | |"); continue
        try:
            df = load_csv(str(it.csv_path), it.timeframe, continuous=MARKETS[it.market].continuous)
            rep_s = scrub(df, MARKETS[it.market], it.timeframe, now=now)
            if rep_s.blocked:
                lines.append(f"| {it.symbol} | {it.strategy} | DATA_BLOCKED | {prev} | | | | data gagal scrub |"); continue
            rep = walk_forward(df, STRATEGIES[it.strategy](), MARKETS[it.market], it.timeframe, symbol=it.symbol)
            groups.setdefault((it.market, it.timeframe, it.strategy), []).append(rep)
            p = save_validation(it.symbol, it.strategy, rep)
            (REPORT_DIR / (p.stem + ".md")).write_text(rep.to_markdown())
            o = rep.oos_metrics
            reason = next((r for r in rep.reasons if r.startswith(("GAGAL", "PERINGATAN"))), rep.reasons[-1] if rep.reasons else "")
            flag = " ⚠️ BERUBAH" if prev not in ("-", rep.verdict) else ""
            lines.append(f"| {it.symbol} | {it.strategy} | **{rep.verdict}**{flag} | {prev} | {o.get('profit_factor', 0):.2f} | "
                         f"{o.get('n_trades', 0)} | {rep.dsr_prob:.2f} | {reason[:90]} |")
            print(f"{it.symbol} {it.strategy}: {rep.verdict}")
        except Exception as e:  # noqa: BLE001
            lines.append(f"| {it.symbol} | {it.strategy} | ERROR | {prev} | | | | {str(e).splitlines()[0][:90]} |")
    # ---- validasi basket (pooled) per market/timeframe/strategi ----
    lines += ["", "## Validasi basket (trade OOS semua simbol digabung)", "",
              "| Basket | Strategi | Verdict | PF OOS | Trade OOS | DSR | Catatan |", "|---|---|---|---|---|---|---|"]
    for (market, tf, strat), reps in groups.items():
        label = f"POOLED_{market}_{tf}"
        prep = pool_reports(reps, MARKETS[market].bars_per_year[tf], label=label)
        prep.strategy = strat
        p = save_validation(label, strat, prep)
        (REPORT_DIR / (p.stem + ".md")).write_text(prep.to_markdown())
        o = prep.oos_metrics
        note = "; ".join(r for r in prep.reasons if r.startswith(("GAGAL", "PERINGATAN")))[:120] or prep.reasons[-1]
        lines.append(f"| {market} {tf} ({len(reps)} simbol) | {strat} | **{prep.verdict}** | {o.get('profit_factor', 0):.2f} | "
                     f"{o.get('n_trades', 0)} | {prep.dsr_prob:.2f} | {note} |")
    (REPORT_DIR / "validation_summary.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
