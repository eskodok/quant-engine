"""Strategi = fungsi murni: fitur sampai bar t -> keputusan di CLOSE bar t.

Eksekusi selalu di OPEN bar t+1 (dilakukan backtester, bukan strategi).
Strategi tidak tahu harga masa depan, tidak tahu equity, tidak tahu posisi lain.

Batasi jumlah parameter. Aturan praktis: <= 1 parameter per 100 trade OOS.
"""
from __future__ import annotations

from dataclasses import dataclass, field, replace

import numpy as np
import pandas as pd

from .features import build_features


@dataclass(frozen=True)
class Signals:
    """Kolom: entry (bool), exit (bool), stop (float), target (float), reason (str)."""
    frame: pd.DataFrame


class Strategy:
    name: str = "base"
    params: dict = {}
    # ruang pencarian kecil untuk walk-forward; sengaja sempit agar tidak overfit
    grid: dict = {}

    def __init__(self, **overrides):
        self.params = {**self.params, **overrides}

    def with_params(self, **kw) -> "Strategy":
        return type(self)(**{**self.params, **kw})

    def features(self, df: pd.DataFrame) -> pd.DataFrame:
        return build_features(df, self.params)

    def signals(self, f: pd.DataFrame) -> pd.DataFrame:  # pragma: no cover - abstract
        raise NotImplementedError

    def run(self, df: pd.DataFrame) -> pd.DataFrame:
        return self.signals(self.features(df))

    @property
    def n_params(self) -> int:
        return len(self.grid) if self.grid else len(self.params)


class TrendPullback(Strategy):
    """Swing long: tren naik (regime=1, ADX>th), pullback ke EMA20 (RSI turun < rsi_pb),
    lalu close kembali di atas EMA20 = entry. SL di bawah swing low - 0.5 ATR,
    TP = entry + rr * risiko. Exit tambahan bila close < EMA50 (tren patah).
    """
    name = "trend_pullback"
    params = {"rsi_pb": 45.0, "adx_min": 18.0, "rr": 2.0, "atr_buf": 0.5, "lookback_pb": 5}
    grid = {"rsi_pb": [40.0, 45.0, 50.0], "adx_min": [15.0, 20.0, 25.0], "rr": [1.5, 2.0, 3.0]}

    def signals(self, f: pd.DataFrame) -> pd.DataFrame:
        p = self.params
        # pullback terjadi bila dalam `lookback_pb` bar terakhir RSI pernah < rsi_pb
        # atau close pernah <= ema_fast (semua memakai data sampai bar ini, inklusif)
        pulled = ((f.rsi < p["rsi_pb"]) | (f.close <= f.ema_fast)).rolling(p["lookback_pb"]).max().fillna(0) > 0
        was_below = (f.close.shift(1) <= f.ema_fast.shift(1))
        cross_up = (f.close > f.ema_fast) & was_below
        entry = (f.regime == 1) & (f.adx > p["adx_min"]) & pulled & cross_up
        stop = f.swing_low - p["atr_buf"] * f.atr
        stop = stop.where(stop < f.close, f.close - 2 * f.atr)  # jaga-jaga swing_low >= close
        risk = f.close - stop
        target = f.close + p["rr"] * risk
        exit_ = f.close < f.ema_mid
        out = pd.DataFrame({"entry": entry.fillna(False), "exit": exit_.fillna(False),
                            "stop": stop, "target": target}, index=f.index)
        out["reason"] = np.where(entry, "uptrend+ADX>" + str(p["adx_min"]) + ", pullback EMA20, close reclaim EMA20", "")
        # bar tanpa fitur lengkap tidak boleh menghasilkan sinyal
        out.loc[f[["ema_slow", "atr", "adx", "rsi"]].isna().any(axis=1), ["entry", "exit"]] = False
        return out


class DonchianBreakout(Strategy):
    """Swing long: breakout di atas Donchian high (n bar sebelumnya) saat regime=1.
    SL = don_lo atau close - 2 ATR (mana yang lebih dekat), TP = rr * risiko.
    """
    name = "donchian_breakout"
    params = {"donchian_n": 20, "rr": 2.0, "adx_min": 15.0}
    grid = {"donchian_n": [20, 40, 55], "rr": [1.5, 2.0, 3.0]}

    def signals(self, f: pd.DataFrame) -> pd.DataFrame:
        p = self.params
        entry = (f.regime == 1) & (f.adx > p["adx_min"]) & (f.close > f.don_hi) & (f.close.shift(1) <= f.don_hi.shift(1))
        stop = pd.concat([f.don_lo, f.close - 2 * f.atr], axis=1).max(axis=1)
        stop = stop.where(stop < f.close, f.close - 2 * f.atr)
        target = f.close + p["rr"] * (f.close - stop)
        exit_ = f.close < f.ema_mid
        out = pd.DataFrame({"entry": entry.fillna(False), "exit": exit_.fillna(False),
                            "stop": stop, "target": target}, index=f.index)
        out["reason"] = np.where(entry, f"breakout Donchian{p['donchian_n']} dalam uptrend", "")
        out.loc[f[["ema_slow", "atr", "adx", "don_hi"]].isna().any(axis=1), ["entry", "exit"]] = False
        return out


STRATEGIES = {s.name: s for s in (TrendPullback, DonchianBreakout)}
