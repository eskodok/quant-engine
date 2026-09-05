"""Uji anti-GIGO. Jalankan: python -m pytest tests -q"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from engine.backtest import run_backtest
from engine.config import CRYPTO_SPOT, IDX, RiskConfig
from engine.features import assert_no_lookahead, build_features
from engine.scrub import scrub
from engine.strategy import STRATEGIES
from engine.synth import make_ohlcv


@pytest.fixture
def df():
    return make_ohlcv(n=1500, timeframe="1d", seed=1)


def test_features_no_lookahead(df):
    assert_no_lookahead(build_features, df)


@pytest.mark.parametrize("name", list(STRATEGIES))
def test_strategy_no_lookahead(df, name):
    s = STRATEGIES[name]()
    assert_no_lookahead(lambda d: s.run(d).drop(columns=["reason"]), df)


def test_lookahead_detector_catches_leak(df):
    def leaky(d):
        f = build_features(d)
        f["leak"] = d.close.shift(-1)  # memakai close bar depan
        return f
    with pytest.raises(AssertionError, match="LOOKAHEAD"):
        assert_no_lookahead(leaky, df)


def test_scrub_passes_clean_data(df):
    rep = scrub(df, CRYPTO_SPOT, "1d")
    assert not rep.blocked, rep.to_markdown()


def test_scrub_blocks_bad_ohlc_and_split(df):
    bad = df.copy()
    bad.iloc[100, bad.columns.get_loc("low")] = bad.iloc[100]["high"] * 1.1   # low > high
    bad.iloc[500:, :4] = bad.iloc[500:, :4] / 5.0                                  # stock split 1:5 tak di-adjust
    rep = scrub(bad, IDX, "1d")
    names = {c.name: c.severity for c in rep.checks}
    assert names["ohlc.integrity"] == "BLOCK"
    assert names["outlier.return"] == "BLOCK"


def test_scrub_blocks_stale_data(df):
    old = df.iloc[:-30]
    rep = scrub(old, CRYPTO_SPOT, "1d")
    assert {c.name: c.severity for c in rep.checks}["freshness"] == "BLOCK"


def test_backtest_fills_next_open_and_charges_costs(df):
    s = STRATEGIES["trend_pullback"]()
    sig = s.run(df)
    res = run_backtest(df, sig, CRYPTO_SPOT, RiskConfig())
    assert len(res.trades) > 5
    t = res.trades.iloc[0]
    i_sig = df.index.get_loc(t.entry_ts) - 1        # sinyal seharusnya di bar sebelum entry
    assert bool(sig.iloc[i_sig]["entry"])
    fill_expected = df.iloc[i_sig + 1]["open"] * (1 + CRYPTO_SPOT.slippage)
    assert np.isclose(t.entry, fill_expected)
    assert t.fees > 0
    # tidak ada trade yang untung lebih dari target (limit) atau rugi jauh melebihi stop tanpa gap
    assert (res.trades.r_multiple <= res.trades.apply(lambda r: (r.target - r.entry) / (r.entry - r.stop), axis=1) + 1e-6).all()


def test_costs_reduce_pnl(df):
    s = STRATEGIES["donchian_breakout"]()
    sig = s.run(df)
    a = run_backtest(df, sig, CRYPTO_SPOT, RiskConfig(), cost_mult=1.0)
    b = run_backtest(df, sig, CRYPTO_SPOT, RiskConfig(), cost_mult=3.0)
    assert b.trades.pnl.sum() < a.trades.pnl.sum()


def test_idx_lot_rounding(df):
    s = STRATEGIES["trend_pullback"]()
    res = run_backtest(df, s.run(df), IDX, RiskConfig())
    if len(res.trades):
        assert (res.trades.qty % 100 == 0).all()


def test_risk_per_trade_respected(df):
    risk = RiskConfig(risk_per_trade=0.01)
    s = STRATEGIES["trend_pullback"]()
    res = run_backtest(df, s.run(df), CRYPTO_SPOT, risk)
    # rugi per trade (tanpa gap) tidak boleh jauh > 1% equity awal + biaya
    stop_losses = res.trades[res.trades.exit_reason == "stop"]
    assert (stop_losses.pnl > -0.02 * risk.initial_equity).all()


def test_load_csv_idx_keeps_yesterday_bar(tmp_path):
    """Regresi: bar IDX kemarin (stempel 16:00 WIB) tidak boleh dibuang pagi ini."""
    from engine.data import load_csv
    d = make_ohlcv(n=500, timeframe="1d", seed=3, continuous=False)
    # stempel semua bar di 09:00 UTC (16:00 WIB) hari masing-masing, terakhir = kemarin
    end = (pd.Timestamp.now(tz="UTC") - pd.Timedelta(days=1)).normalize() + pd.Timedelta(hours=9)
    d.index = pd.date_range(end=end, periods=len(d), freq="B", tz="UTC") + pd.Timedelta(hours=9)
    p = tmp_path / "x.csv"; d.to_csv(p, index_label="ts")
    assert load_csv(str(p), "1d", continuous=False).index[-1] == d.index[-1]
    assert len(load_csv(str(p), "1d", continuous=True)) == len(d) - 1  # aturan crypto memang membuangnya
