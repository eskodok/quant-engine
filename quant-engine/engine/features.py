"""Feature engineering yang HANYA memakai data masa lalu.

Aturan:
- Semua fungsi menerima df OHLCV dan mengembalikan kolom baru.
- Dilarang: shift(-n), rolling(center=True), normalisasi dengan statistik seluruh
  seri (mean/std global), bfill(), interpolate().
- assert_no_lookahead() adalah uji otomatis: ubah data masa depan, fitur di masa
  lalu harus tetap identik. Dijalankan di test dan sebelum backtest.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def atr(df: pd.DataFrame, n: int = 14) -> pd.Series:
    prev_close = df.close.shift(1)
    tr = pd.concat([df.high - df.low, (df.high - prev_close).abs(), (df.low - prev_close).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1 / n, adjust=False, min_periods=n).mean()


def rsi(s: pd.Series, n: int = 14) -> pd.Series:
    d = s.diff()
    up = d.clip(lower=0).ewm(alpha=1 / n, adjust=False, min_periods=n).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1 / n, adjust=False, min_periods=n).mean()
    rs = up / dn.replace(0, np.nan)
    return 100 - 100 / (1 + rs)


def adx(df: pd.DataFrame, n: int = 14) -> pd.Series:
    up = df.high.diff()
    dn = -df.low.diff()
    plus_dm = ((up > dn) & (up > 0)) * up
    minus_dm = ((dn > up) & (dn > 0)) * dn
    tr = atr(df, n)
    plus_di = 100 * plus_dm.ewm(alpha=1 / n, adjust=False, min_periods=n).mean() / tr
    minus_di = 100 * minus_dm.ewm(alpha=1 / n, adjust=False, min_periods=n).mean() / tr
    dx = 100 * (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan)
    return dx.ewm(alpha=1 / n, adjust=False, min_periods=n).mean()


def build_features(df: pd.DataFrame, p: dict | None = None) -> pd.DataFrame:
    """Fitur standar untuk swing. Parameter diambil dari dict agar strategi bisa override."""
    p = {"ema_fast": 20, "ema_mid": 50, "ema_slow": 200, "atr_n": 14, "rsi_n": 14,
         "adx_n": 14, "donchian_n": 20, **(p or {})}
    f = df.copy()
    f["ema_fast"] = ema(df.close, p["ema_fast"])
    f["ema_mid"] = ema(df.close, p["ema_mid"])
    f["ema_slow"] = ema(df.close, p["ema_slow"])
    f["atr"] = atr(df, p["atr_n"])
    f["atr_pct"] = f["atr"] / df.close
    f["rsi"] = rsi(df.close, p["rsi_n"])
    f["adx"] = adx(df, p["adx_n"])
    f["don_hi"] = df.high.rolling(p["donchian_n"]).max().shift(1)  # shift(1): breakout dibanding bar SEBELUMNYA
    f["don_lo"] = df.low.rolling(p["donchian_n"]).min().shift(1)
    f["swing_low"] = df.low.rolling(5).min()
    # regime: 1 = uptrend, -1 = downtrend, 0 = sideways (dihitung dari data sampai bar ini)
    slope = f["ema_slow"] / f["ema_slow"].shift(10) - 1
    f["regime"] = np.select(
        [(df.close > f["ema_slow"]) & (f["ema_mid"] > f["ema_slow"]) & (slope > 0),
         (df.close < f["ema_slow"]) & (f["ema_mid"] < f["ema_slow"]) & (slope < 0)],
        [1, -1], 0)
    # likuiditas: nilai transaksi median 20 bar (untuk filter saham tidur)
    f["turnover_med"] = (df.close * df.volume).rolling(20).median()
    return f


def assert_no_lookahead(fn, df: pd.DataFrame, cut: int | None = None, n_trials: int = 3, seed: int = 0) -> None:
    """Uji: fitur pada bar <= cut tidak boleh berubah jika data setelah cut diacak.

    fn: callable(df) -> DataFrame. Melempar AssertionError bila ada kebocoran.
    """
    rng = np.random.default_rng(seed)
    n = len(df)
    cut = cut or int(n * 0.7)
    base = fn(df).iloc[:cut]
    for _ in range(n_trials):
        pert = df.copy()
        fut = pert.iloc[cut:].copy()
        noise = rng.uniform(0.5, 1.5, size=(len(fut), 1))
        for c in ("open", "high", "low", "close"):
            fut[c] = fut[c].values * noise[:, 0]
        fut["high"] = fut[["open", "high", "low", "close"]].max(axis=1)
        fut["low"] = fut[["open", "high", "low", "close"]].min(axis=1)
        fut["volume"] = fut["volume"].values * rng.uniform(0.1, 5, size=len(fut))
        pert.iloc[cut:] = fut
        out = fn(pert).iloc[:cut]
        num = base.select_dtypes(include=[np.number])
        num2 = out[num.columns]
        diff = ~np.isclose(num.values, num2.values, equal_nan=True, rtol=1e-9, atol=1e-12)
        if diff.any():
            cols = [num.columns[j] for j in np.where(diff.any(axis=0))[0]]
            raise AssertionError(f"LOOKAHEAD TERDETEKSI pada kolom: {cols}")
