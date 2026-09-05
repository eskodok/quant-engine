"""Data scrub: gerbang wajib sebelum backtest atau signal.

Kalau ada satu saja BLOCK, engine berhenti. Tidak ada mode "abaikan saja".
Diadaptasi dari pola /data-scrub (claude-code-quant-skills) + pengalaman IDX.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from .config import MarketProfile, TIMEFRAME_SECONDS
from .data import COLUMNS


@dataclass
class Check:
    name: str
    severity: str  # OK | WARN | BLOCK
    detail: str
    fix: str = ""


@dataclass
class ScrubReport:
    checks: list = field(default_factory=list)

    @property
    def blocked(self) -> bool:
        return any(c.severity == "BLOCK" for c in self.checks)

    @property
    def warnings(self) -> list:
        return [c for c in self.checks if c.severity == "WARN"]

    def to_markdown(self) -> str:
        lines = ["| Check | Hasil | Severity | Fix |", "|---|---|---|---|"]
        for c in self.checks:
            lines.append(f"| {c.name} | {c.detail} | **{c.severity}** | {c.fix} |")
        verdict = "DATA TIDAK LAYAK — perbaiki dulu" if self.blocked else "Data layak untuk backtest/signal"
        return "\n".join(lines) + f"\n\n**Verdict:** {verdict}"


def scrub(df: pd.DataFrame, market: MarketProfile, timeframe: str,
          min_bars: int = 400, now: pd.Timestamp | None = None) -> ScrubReport:
    rep = ScrubReport()
    add = rep.checks.append

    # 1. Schema
    missing = [c for c in COLUMNS if c not in df.columns]
    if missing or not isinstance(df.index, pd.DatetimeIndex) or df.index.tz is None:
        add(Check("schema", "BLOCK", f"kolom hilang={missing}, index tz-aware={getattr(df.index, 'tz', None) is not None}",
                  "gunakan engine.data.load()"))
        return rep  # tidak ada gunanya lanjut
    add(Check("schema", "OK", f"{len(df)} bar, kolom lengkap, tz={df.index.tz}"))

    # 2. Panjang histori
    if len(df) < min_bars:
        add(Check("history", "BLOCK", f"hanya {len(df)} bar (< {min_bars})", "ambil histori lebih panjang"))
    else:
        add(Check("history", "OK", f"{len(df)} bar"))

    # 3. Timestamp: monoton, unik, gap
    if not df.index.is_monotonic_increasing:
        add(Check("timestamp.order", "BLOCK", "tidak monoton naik", "sort_index()"))
    dups = int(df.index.duplicated().sum())
    if dups:
        add(Check("timestamp.dup", "BLOCK", f"{dups} timestamp duplikat", "drop_duplicates(keep='last')"))
    else:
        add(Check("timestamp.dup", "OK", "tidak ada duplikat"))
    tf = TIMEFRAME_SECONDS[timeframe]
    deltas = df.index.to_series().diff().dt.total_seconds().dropna()
    if market.continuous:
        gaps = deltas[deltas > tf * 1.5]
        sev = "BLOCK" if len(gaps) > max(3, 0.002 * len(df)) else ("WARN" if len(gaps) else "OK")
        add(Check("timestamp.gaps", sev, f"{len(gaps)} gap > 1.5x TF (maks {deltas.max()/tf:.1f}x)",
                  "isi dari exchange lain / potong rentang" if sev != "OK" else ""))
    else:
        # IDX: gap 1-4 hari normal (weekend, libur), 8-13 hari = libur Lebaran (1x/tahun).
        # >13 hari kalender = suspensi/masalah data.
        long_gaps = deltas[deltas > 13 * 86400]
        lebaran = deltas[(deltas > 7 * 86400) & (deltas <= 13 * 86400)]
        years = max((df.index[-1] - df.index[0]).days / 365, 1)
        if len(long_gaps):
            sev = "BLOCK" if len(long_gaps) > 1 else "WARN"
            add(Check("timestamp.gaps", sev, f"{len(long_gaps)} gap > 13 hari (maks {long_gaps.max()/86400:.0f} hari) — suspensi?",
                      "cek riwayat suspensi emiten / potong histori"))
        elif len(lebaran) > years + 1:
            add(Check("timestamp.gaps", "WARN", f"{len(lebaran)} gap 8-13 hari dalam {years:.0f} tahun (lebih dari libur Lebaran)"))
        else:
            add(Check("timestamp.gaps", "OK", f"{len(lebaran)} gap libur panjang (Lebaran) dalam {years:.0f} tahun"))

    # 4. NaN
    nan_rows = int(df[COLUMNS].isna().any(axis=1).sum())
    if nan_rows:
        sev = "BLOCK" if nan_rows > 0.01 * len(df) else "WARN"
        add(Check("nan", sev, f"{nan_rows} baris NaN", "dropna() lalu cek gap"))
    else:
        add(Check("nan", "OK", "tidak ada NaN"))

    # 5. Integritas OHLC
    bad = ((df.low > df[["open", "close"]].min(axis=1)) |
           (df.high < df[["open", "close"]].max(axis=1)) |
           (df.low > df.high) | (df[COLUMNS[:4]] <= 0).any(axis=1))
    nbad = int(bad.sum())
    add(Check("ohlc.integrity", "BLOCK" if nbad else "OK", f"{nbad} bar melanggar low<=o,c<=high / harga<=0",
              "buang/perbaiki bar dari sumber lain" if nbad else ""))
    negvol = int((df.volume < 0).sum())
    if negvol:
        add(Check("volume.negative", "BLOCK", f"{negvol} bar volume negatif", "perbaiki sumber"))

    # 6. Stale bars (volume 0 & OHLC datar) — di IDX ini saham tidur, di crypto = feed mati
    stale = ((df.volume == 0) & (df.high == df.low)).sum()
    stale_pct = stale / len(df)
    sev = "OK" if stale_pct < 0.02 else ("WARN" if stale_pct < 0.10 else "BLOCK")
    add(Check("stale_bars", sev, f"{int(stale)} bar ({stale_pct:.1%}) volume 0 & datar",
              "likuiditas rendah: jangan trading simbol ini" if sev != "OK" else ""))

    # 7. Outlier return (split, data error, ARA/ARB beruntun)
    ret = df.close.pct_change().abs()
    out = ret[ret > market.max_abs_return]
    if len(out):
        add(Check("outlier.return", "BLOCK", f"{len(out)} bar |return| > {market.max_abs_return:.0%} (terakhir {out.index[-1].date()})",
                  "kemungkinan stock split / data error: adjust atau potong histori sebelum tanggal itu"))
    else:
        add(Check("outlier.return", "OK", f"maks |return| {ret.max():.1%}"))
    # gap open vs close sebelumnya juga (split sering muncul di open)
    gap_open = (df.open / df.close.shift(1) - 1).abs()
    go = gap_open[gap_open > market.max_abs_return]
    if len(go):
        add(Check("outlier.gap_open", "BLOCK", f"{len(go)} open gap > {market.max_abs_return:.0%}", "cek corporate action"))

    # 8. Volume spike (bukan blocker, tapi ditandai)
    med = df.volume.rolling(50, min_periods=20).median()
    spikes = int(((df.volume > 20 * med) & (med > 0)).sum())
    add(Check("volume.spikes", "WARN" if spikes > 0.01 * len(df) else "OK", f"{spikes} bar volume > 20x median"))

    # 9. Kesegaran data — sinyal dari data basi = sinyal sampah
    now = now or pd.Timestamp.now(tz="UTC")
    age = (now - df.index[-1]).total_seconds() / tf
    limit = market.stale_multiplier if market.continuous else 6.0  # IDX: weekend + libur
    sev = "OK" if age <= limit else ("WARN" if age <= 2 * limit else "BLOCK")
    add(Check("freshness", sev, f"bar terakhir {df.index[-1]} ({age:.1f}x TF yang lalu)",
              "refresh data" if sev != "OK" else ""))

    # 10. Bar yang belum tutup. Crypto: stempel = jam BUKA bar (ts+TF harus <= now).
    #     IDX: stempel = jam TUTUP sesi (ts harus <= now).
    last_close = df.index[-1] + pd.Timedelta(seconds=tf) if market.continuous else df.index[-1]
    if last_close > now:
        add(Check("open_bar", "BLOCK", "bar terakhir masih berjalan", "buang bar terakhir (engine.data melakukan ini)"))

    return rep


def gate(df: pd.DataFrame, market: MarketProfile, timeframe: str, **kw) -> ScrubReport:
    rep = scrub(df, market, timeframe, **kw)
    if rep.blocked:
        raise RuntimeError("DATA GATE GAGAL:\n" + rep.to_markdown())
    return rep
