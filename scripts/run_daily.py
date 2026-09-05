#!/usr/bin/env python3
"""Scan harian: scrub -> signal untuk semua item watchlist dari data/*.csv.

Output: reports/daily_scan.md (dibaca manusia) dan reports/daily_scan.json (dibaca Claude).
Tidak mengakses internet — hanya file CSV hasil fetch_data.py.
"""
from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from engine.config import MARKETS, RiskConfig  # noqa: E402
from engine.data import load_csv  # noqa: E402
from engine.scrub import scrub  # noqa: E402
from engine.signal import REPORT_DIR, format_setup, generate, load_validation  # noqa: E402
from engine.strategy import STRATEGIES  # noqa: E402

RANK = {"SHIP": 2, "FIX": 1}


def pick_strategy(it) -> tuple[str, str]:
    """'auto' -> strategi dengan validasi terbaik (per simbol, lalu basket). Tidak ada yang lolos -> default + catatan."""
    if it.strategy != "auto":
        return it.strategy, ""
    best, best_key = None, (-1, 0.0)
    for name in STRATEGIES:
        for label in (it.symbol, f"POOLED_{it.market}_{it.timeframe}"):
            v = load_validation(label, name)
            if v and v["verdict"] in RANK:
                key = (RANK[v["verdict"]], v["oos"].get("profit_factor", 0))
                if key > best_key:
                    best, best_key = name, key
    if best:
        return best, f"auto: {best} (validasi terbaik)"
    return "trend_pullback", "auto: belum ada strategi yang lolos validasi -> tidak akan ada sinyal LONG"
from engine.watchlist import read_watchlist  # noqa: E402

EQUITY = {"idx": 100_000_000.0, "crypto_spot": 5_000.0, "crypto_perp": 5_000.0}  # ubah sesuai modal


def main() -> int:
    REPORT_DIR.mkdir(exist_ok=True)
    now = pd.Timestamp.now(tz="UTC")
    items = read_watchlist()
    rows, details, out = [], [], {"generated": str(now), "items": []}
    for it in items:
        strat_name, strat_note = pick_strategy(it)
        rec = {"key": it.key, "market": it.market, "symbol": it.symbol, "timeframe": it.timeframe,
               "strategy": strat_name, "strategy_note": strat_note}
        if not it.csv_path.exists():
            rec.update(status="NO_DATA", note="file data belum ada (fetch gagal?)")
            out["items"].append(rec); rows.append(rec); continue
        try:
            df = load_csv(str(it.csv_path), it.timeframe, continuous=MARKETS[it.market].continuous)
            rep = scrub(df, MARKETS[it.market], it.timeframe, now=now)
            rec["scrub"] = [{"check": c.name, "sev": c.severity, "detail": c.detail} for c in rep.checks if c.severity != "OK"]
            if rep.blocked:
                rec.update(status="DATA_BLOCKED", note="; ".join(f"{c.name}: {c.detail}" for c in rep.checks if c.severity == "BLOCK"))
                out["items"].append(rec); rows.append(rec); continue
            s = generate(df, it.symbol, it.market, it.timeframe, strat_name,
                         risk=RiskConfig(initial_equity=EQUITY[it.market]))
            rec.update(status="OK", setup=asdict(s))
            if s.action == "LONG":
                details.append(format_setup(s))
        except Exception as e:  # noqa: BLE001
            rec.update(status="ERROR", note=str(e).splitlines()[0][:200])
        out["items"].append(rec); rows.append(rec)

    # ---- markdown ----
    md = [f"# Scan harian — {now:%Y-%m-%d %H:%M} UTC ({(now.tz_convert('Asia/Jakarta')):%H:%M} WIB)", "",
          "| Simbol | TF | Aksi | Regime | Conf | Close | SL | TP | Validasi | Catatan |", "|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        if r["status"] == "OK":
            s = r["setup"]
            sl = f"{s['stop']:,.6g}" if s["action"] == "LONG" else ""
            tp = f"{s['target']:,.6g}" if s["action"] == "LONG" else ""
            note = "; ".join(x["check"] for x in r.get("scrub", []))
            md.append(f"| {r['symbol']} | {r['timeframe']} | **{s['action']}** | {s['regime']} | {s['confidence']:.0%} | "
                      f"{s['entry_ref']:,.6g} | {sl} | {tp} | {s['validation_verdict']} | {note} |")
        else:
            md.append(f"| {r['symbol']} | {r['timeframe']} | {r['status']} | | | | | | | {r.get('note','')} |")
    longs = [r for r in rows if r["status"] == "OK" and r["setup"]["action"] == "LONG"]
    md += ["", f"**Setup LONG hari ini: {len(longs)}**", ""]
    for d in details:
        md += ["```", d, "```", ""]
    # regime pasar
    md += ["## Regime pasar", ""]
    for r in rows:
        if r["status"] == "OK":
            s = r["setup"]
            md.append(f"- {r['symbol']} ({r['timeframe']}): {s['regime']} — {s['reasons'][-1] if s['action']!='LONG' else s['reasons'][1]}")
    (REPORT_DIR / "daily_scan.md").write_text("\n".join(md) + "\n")
    (REPORT_DIR / "daily_scan.json").write_text(json.dumps(out, indent=2, default=str))
    print("\n".join(md))
    return 0


if __name__ == "__main__":
    sys.exit(main())
