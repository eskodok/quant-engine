"""Backtester bar-per-bar, sengaja sederhana dan transparan.

Aturan eksekusi (sumber utama "backtest bagus, live jelek" kalau dilanggar):
1. Sinyal dihitung di CLOSE bar t, order diisi di OPEN bar t+1 + slippage.
2. SL/TP dicek dengan HIGH/LOW bar berikutnya. Jika SL dan TP kena di bar yang
   sama -> dianggap SL (konservatif). Gap melewati SL -> isi di open (lebih jelek).
3. Fee dan slippage dibayar dua kali (masuk & keluar), dari MarketProfile.
4. Ukuran posisi dari risiko (jarak ke SL), dibatasi maks % equity, dibulatkan ke lot.
5. Satu posisi per simbol. Long only (v1).
"""
from __future__ import annotations

from dataclasses import dataclass, asdict

import numpy as np
import pandas as pd

from .config import MarketProfile, RiskConfig


@dataclass
class Trade:
    entry_ts: pd.Timestamp
    exit_ts: pd.Timestamp
    entry: float
    exit: float
    qty: float
    stop: float
    target: float
    pnl: float
    r_multiple: float
    ret_pct: float
    bars: int
    exit_reason: str
    fees: float


@dataclass
class BacktestResult:
    trades: pd.DataFrame
    equity: pd.Series
    params: dict
    warnings: list


def _round_qty(qty: float, lot: float) -> float:
    if lot <= 0:
        return qty
    return np.floor(qty / lot) * lot


def run_backtest(df: pd.DataFrame, sig: pd.DataFrame, market: MarketProfile,
                 risk: RiskConfig = RiskConfig(), cost_mult: float = 1.0) -> BacktestResult:
    o, h, l, c = (df[k].values for k in ("open", "high", "low", "close"))
    entry_sig = sig["entry"].values
    exit_sig = sig["exit"].values
    stop_arr = sig["stop"].values
    tgt_arr = sig["target"].values
    max_hold = int(sig["max_hold"].iloc[0]) if "max_hold" in sig.columns else 0  # 0 = tanpa time-stop
    weight_arr = sig["weight"].values if "weight" in sig.columns else None  # fraksi equity (vol-target)
    idx = df.index

    fee_b, fee_s = market.fee_buy * cost_mult, market.fee_sell * cost_mult
    slip = market.slippage * cost_mult

    equity = risk.initial_equity
    eq_curve = np.empty(len(df))
    trades: list[Trade] = []
    warnings: list[str] = []
    pos = None  # dict saat ada posisi
    pending = None  # sinyal entry dari bar sebelumnya, diisi di open bar ini
    pending_exit = False

    for i in range(len(df)):
        # --- 1) eksekusi order yang tertunda di OPEN bar i ---
        if pos is None and pending is not None:
            fill = o[i] * (1 + slip)
            stop, target = pending["stop"], pending["target"]
            if stop < fill:  # kalau gap up melewati target/merusak RR, tetap pakai stop asli
                risk_per_unit = fill - stop
                if pending.get("weight") is not None:
                    qty = pending["weight"] * equity / fill            # ukuran dari vol-target
                else:
                    qty = risk.risk_per_trade * equity / risk_per_unit  # ukuran dari jarak SL
                    qty = min(qty, risk.max_position_pct * equity / fill)
                qty = _round_qty(qty, market.lot_size)
                if qty > 0:
                    fee = fill * qty * fee_b
                    pos = {"i": i, "entry": fill, "qty": qty, "stop": stop, "target": target, "fees": fee}
            pending = None
        elif pos is not None and pending_exit:
            fill = o[i] * (1 - slip)
            _close(pos, i, fill, "signal_exit", trades, idx, fee_s)
            equity += trades[-1].pnl
            pos = None
            pending_exit = False

        # --- 2) cek SL/TP intrabar untuk posisi terbuka (termasuk bar fill) ---
        if pos is not None:
            hit_stop = l[i] <= pos["stop"]
            hit_tgt = h[i] >= pos["target"]
            if hit_stop:  # konservatif: stop menang bila keduanya kena
                px = min(pos["stop"], o[i]) if o[i] < pos["stop"] else pos["stop"]
                _close(pos, i, px * (1 - slip), "stop", trades, idx, fee_s)
                equity += trades[-1].pnl
                pos = None
            elif hit_tgt:
                px = max(pos["target"], o[i]) if o[i] > pos["target"] else pos["target"]
                _close(pos, i, px, "target", trades, idx, fee_s)  # limit order: tanpa slippage
                equity += trades[-1].pnl
                pos = None

        # --- 3) keputusan di CLOSE bar i, dieksekusi bar i+1 ---
        if pos is None and entry_sig[i] and np.isfinite(stop_arr[i]) and np.isfinite(tgt_arr[i]):
            pending = {"stop": float(stop_arr[i]), "target": float(tgt_arr[i]),
                       "weight": (float(np.clip(weight_arr[i], 0, 1)) if weight_arr is not None and np.isfinite(weight_arr[i]) else None)}
        elif pos is not None and (exit_sig[i] or (max_hold and i - pos["i"] >= max_hold)):
            pending_exit = True

        # mark-to-market
        eq_curve[i] = equity + (pos["qty"] * (c[i] - pos["entry"]) - pos["fees"] if pos else 0.0)

    if pos is not None:  # tutup paksa di close terakhir agar tidak ada P&L gantung
        _close(pos, len(df) - 1, c[-1] * (1 - slip), "eod_force", trades, idx, fee_s)
        equity += trades[-1].pnl
        eq_curve[-1] = equity
        warnings.append("posisi terakhir ditutup paksa di bar terakhir")

    if market.name == "crypto_perp":
        warnings.append("funding rate tidak dimodelkan; strategi hold > 1 hari bisa kena 0.01%/8 jam")

    tdf = pd.DataFrame([asdict(t) for t in trades])
    return BacktestResult(tdf, pd.Series(eq_curve, index=idx, name="equity"), {}, warnings)


def _close(pos, i, px, reason, trades, idx, fee_s):
    fee = px * pos["qty"] * fee_s
    fees = pos["fees"] + fee
    pnl = (px - pos["entry"]) * pos["qty"] - fees
    risk_unit = (pos["entry"] - pos["stop"]) * pos["qty"]
    trades.append(Trade(
        entry_ts=idx[pos["i"]], exit_ts=idx[i], entry=pos["entry"], exit=px, qty=pos["qty"],
        stop=pos["stop"], target=pos["target"], pnl=pnl,
        r_multiple=pnl / risk_unit if risk_unit > 0 else np.nan,
        ret_pct=px / pos["entry"] - 1, bars=i - pos["i"], exit_reason=reason, fees=fees))
