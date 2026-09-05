"""Metrik performa. Semua anualisasi memakai bars_per_year dari MarketProfile."""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats


def summarize(trades: pd.DataFrame, equity: pd.Series, bars_per_year: int) -> dict:
    m: dict = {"n_trades": int(len(trades))}
    if len(trades) == 0:
        m.update(profit_factor=0.0, win_rate=0.0, expectancy_r=0.0, sharpe=0.0, sortino=0.0,
                 max_dd=0.0, cagr=0.0, total_return=0.0, avg_bars=0.0, exposure=0.0)
        return m
    wins = trades.pnl[trades.pnl > 0].sum()
    losses = -trades.pnl[trades.pnl < 0].sum()
    m["profit_factor"] = float(wins / losses) if losses > 0 else float("inf")
    m["win_rate"] = float((trades.pnl > 0).mean())
    m["expectancy_r"] = float(trades.r_multiple.mean())
    m["avg_win_r"] = float(trades.r_multiple[trades.pnl > 0].mean()) if (trades.pnl > 0).any() else 0.0
    m["avg_loss_r"] = float(trades.r_multiple[trades.pnl <= 0].mean()) if (trades.pnl <= 0).any() else 0.0
    m["avg_bars"] = float(trades.bars.mean())
    m["exposure"] = float(trades.bars.sum() / max(len(equity), 1))

    r = equity.pct_change().dropna()
    if len(r) > 1 and r.std() > 0:
        m["sharpe"] = float(r.mean() / r.std() * np.sqrt(bars_per_year))
        dn = r[r < 0].std()
        m["sortino"] = float(r.mean() / dn * np.sqrt(bars_per_year)) if dn and dn > 0 else float("inf")
    else:
        m["sharpe"] = m["sortino"] = 0.0
    peak = equity.cummax()
    m["max_dd"] = float(((equity - peak) / peak).min())
    yrs = len(equity) / bars_per_year
    m["total_return"] = float(equity.iloc[-1] / equity.iloc[0] - 1)
    m["cagr"] = float((equity.iloc[-1] / equity.iloc[0]) ** (1 / yrs) - 1) if yrs > 0 else 0.0
    m["calmar"] = float(m["cagr"] / abs(m["max_dd"])) if m["max_dd"] < 0 else float("inf")
    m["skew"] = float(r.skew()) if len(r) > 2 else 0.0
    m["kurt"] = float(r.kurt()) if len(r) > 3 else 0.0
    return m


def deflated_sharpe(sharpe_annual: float, n_obs: int, bars_per_year: int, n_trials: int,
                    skew: float = 0.0, kurt: float = 3.0, var_sr_trials: float | None = None) -> float:
    """Probabilitas Sharpe asli > 0 setelah koreksi jumlah percobaan (Bailey & Lopez de Prado 2014).

    Mengembalikan probabilitas [0,1]. < 0.90 berarti Sharpe kemungkinan besar hasil seleksi/overfit.
    """
    if n_obs < 10 or n_trials < 1:
        return 0.0
    sr = sharpe_annual / np.sqrt(bars_per_year)  # per-bar Sharpe
    # ekspektasi maksimum SR dari n_trials percobaan tanpa sinyal
    if var_sr_trials is None:
        var_sr_trials = (1.0 / np.sqrt(bars_per_year)) ** 2 * 0.25  # asumsi konservatif
    emc = 0.5772156649
    if n_trials > 1:
        sr0 = np.sqrt(var_sr_trials) * ((1 - emc) * stats.norm.ppf(1 - 1 / n_trials) +
                                        emc * stats.norm.ppf(1 - 1 / (n_trials * np.e)))
    else:
        sr0 = 0.0
    kurt_excess = kurt if kurt is not None else 3.0
    denom = np.sqrt(max(1 - skew * sr + (kurt_excess - 1) / 4 * sr ** 2, 1e-9))
    z = (sr - sr0) * np.sqrt(n_obs - 1) / denom
    return float(stats.norm.cdf(z))


def monte_carlo_dd(trades: pd.DataFrame, initial_equity: float, n: int = 2000, seed: int = 0) -> dict:
    """Acak urutan trade -> distribusi max drawdown. Menjawab: seberapa buruk yang wajar?"""
    if len(trades) < 5:
        return {"dd_p50": 0.0, "dd_p95": 0.0, "dd_worst": 0.0}
    rng = np.random.default_rng(seed)
    rets = (trades.pnl / initial_equity).values
    dds = np.empty(n)
    for k in range(n):
        eq = 1 + np.cumsum(rng.permutation(rets))
        peak = np.maximum.accumulate(np.concatenate([[1.0], eq]))[1:]
        dds[k] = ((eq - peak) / peak).min()
    return {"dd_p50": float(np.median(dds)), "dd_p95": float(np.percentile(dds, 5)), "dd_worst": float(dds.min())}
