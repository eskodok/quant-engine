#!/usr/bin/env python3
"""Tarik data OHLCV untuk semua item watchlist -> data/*.csv (dijalankan GitHub Actions).

Satu simbol gagal tidak menghentikan yang lain; hasilnya dicatat di data/fetch_log.md.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from engine.data import load  # noqa: E402
from engine.watchlist import DATA_DIR, read_watchlist  # noqa: E402


def main() -> int:
    DATA_DIR.mkdir(exist_ok=True)
    items = read_watchlist()
    log = [f"# Fetch log — {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M} UTC", "",
           "| item | status | bar | bar terakhir | sumber |", "|---|---|---|---|---|"]
    failed = 0
    for it in items:
        try:
            kw = {"limit_bars": 3000} if it.market.startswith("crypto") else {}
            df = load(it.symbol, it.market, it.timeframe, cache=False, **kw)
            df.to_csv(it.csv_path, index_label="ts")
            log.append(f"| {it.key} | OK | {len(df)} | {df.index[-1]} | {df.attrs.get('source', it.market)} |")
            print(f"OK   {it.key}: {len(df)} bar, terakhir {df.index[-1]}")
        except Exception as e:  # noqa: BLE001
            failed += 1
            msg = str(e).replace("|", "/").replace("\n", " ")[:200]
            log.append(f"| {it.key} | GAGAL | - | - | {msg} |")
            print(f"GAGAL {it.key}: {msg}")
    (DATA_DIR / "fetch_log.md").write_text("\n".join(log) + "\n")
    print(f"\nselesai: {len(items) - failed}/{len(items)} berhasil")
    return 0  # selalu 0 agar file yang berhasil tetap di-commit


if __name__ == "__main__":
    sys.exit(main())
