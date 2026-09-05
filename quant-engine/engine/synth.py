"""Data sintetis regime-switching untuk uji engine (BUKAN untuk validasi strategi sungguhan)."""
from __future__ import annotations

import numpy as np
import pandas as pd


def make_ohlcv(n: int = 2500, timeframe: str = "1d", seed: int = 42, start_price: float = 100.0,
               end: pd.Timestamp | None = None, continuous: bool = True) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    step = {"1d": pd.Timedelta(days=1), "4h": pd.Timedelta(hours=4)}[timeframe]
    end = end or (pd.Timestamp.now(tz="UTC").floor("D") - step)
    idx = pd.date_range(end=end, periods=n, freq=step, tz="UTC")
    if not continuous:
        idx = idx[idx.dayofweek < 5]
    n = len(idx)
    # regime: drift bergantian (bull / bear / sideways) dengan durasi acak
    drift = np.empty(n); vol = np.empty(n); i = 0
    while i < n:
        L = int(rng.integers(60, 250))
        r = rng.choice([1, -1, 0], p=[0.45, 0.25, 0.30])
        drift[i:i + L] = {1: 0.0012, -1: -0.0010, 0: 0.0}[r]
        vol[i:i + L] = {1: 0.018, -1: 0.028, 0: 0.014}[r]
        i += L
    ret = drift + vol * rng.standard_t(df=4, size=n) * 0.8
    close = start_price * np.exp(np.cumsum(ret))
    open_ = np.concatenate([[start_price], close[:-1]]) * (1 + rng.normal(0, 0.003, n))
    wick = np.abs(rng.normal(0, 0.006, n)) * close
    high = np.maximum(open_, close) + wick
    low = np.minimum(open_, close) - wick
    volume = rng.lognormal(mean=12, sigma=0.5, size=n) * (1 + 3 * np.abs(ret) / vol)
    df = pd.DataFrame({"open": open_, "high": high, "low": low, "close": close, "volume": volume}, index=idx)
    df.index.name = "ts"
    return df
