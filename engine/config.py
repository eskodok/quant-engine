"""Konfigurasi engine: profil market, biaya, dan aturan risk.

Prinsip: SEMUA angka biaya/slippage eksplisit di sini, tidak ada default
tersembunyi di kode lain. Kalau biaya salah, backtest pasti bohong.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class MarketProfile:
    name: str
    # biaya per sisi (fraksi). Buy dan sell bisa beda (IDX kena PPh final saat jual).
    fee_buy: float
    fee_sell: float
    # slippage per sisi (fraksi) untuk order market di TF swing.
    slippage: float
    # batas gerak harian wajar; return absolut di atas ini dianggap outlier data (BLOCK).
    max_abs_return: float
    # pasar 24/7 (crypto) atau ada sesi/hari libur (IDX)?
    continuous: bool
    # ukuran lot minimum (IDX = 100 lembar) dan tick harga (IDX bertingkat, disederhanakan).
    lot_size: float
    # bar per tahun untuk anualisasi metrik, per timeframe.
    bars_per_year: dict = field(default_factory=dict)
    # umur maksimum bar terakhir (dalam kelipatan timeframe) sebelum data dianggap basi.
    stale_multiplier: float = 2.5


CRYPTO_SPOT = MarketProfile(
    name="crypto_spot",
    fee_buy=0.0010,     # Binance taker 0.10% (tanpa BNB discount)
    fee_sell=0.0010,
    slippage=0.0005,    # 0.05% per sisi; naikkan untuk altcoin tipis
    max_abs_return=0.35,
    continuous=True,
    lot_size=0.0,
    bars_per_year={"4h": 6 * 365, "1d": 365},
)

CRYPTO_PERP = MarketProfile(
    name="crypto_perp",
    fee_buy=0.0005,     # taker 0.05%. Funding TIDAK dimodelkan -> engine akan WARN.
    fee_sell=0.0005,
    slippage=0.0005,
    max_abs_return=0.35,
    continuous=True,
    lot_size=0.0,
    bars_per_year={"4h": 6 * 365, "1d": 365},
)

IDX = MarketProfile(
    name="idx",
    fee_buy=0.0015,     # komisi broker ~0.15% (sudah termasuk levy & PPN, kira-kira)
    fee_sell=0.0025,    # komisi ~0.15% + PPh final 0.1%
    slippage=0.0020,    # spread 1-2 tick pada saham lapis 2 mudah 0.2%+
    max_abs_return=0.36,  # ARA/ARB maksimal ~35%
    continuous=False,
    lot_size=100.0,
    bars_per_year={"1d": 245},
)

MARKETS = {m.name: m for m in (CRYPTO_SPOT, CRYPTO_PERP, IDX)}

TIMEFRAME_SECONDS = {"1h": 3600, "4h": 4 * 3600, "1d": 86400}


@dataclass(frozen=True)
class RiskConfig:
    risk_per_trade: float = 0.01      # 1% equity per trade (jarak ke SL)
    max_position_pct: float = 0.25    # maks 25% equity di satu posisi
    max_open_positions: int = 4
    initial_equity: float = 100_000_000.0  # IDR untuk IDX; untuk crypto anggap USDT


# Batas validasi (dipakai engine/validate.py untuk verdict).
@dataclass(frozen=True)
class ValidationThresholds:
    min_trades_oos: int = 30
    max_oos_degradation: float = 0.40   # PF/Sharpe OOS turun >40% dari IS = FIX
    min_oos_profit_factor: float = 1.15
    min_deflated_sharpe_prob: float = 0.90
    max_params_per_100_trades: float = 1.0
    cost_stress_multiplier: float = 2.0  # strategi harus tetap PF>1 saat biaya x2
    min_random_pctile: float = 75.0      # PF strategi harus > 75% dari versi entry-acak dirinya
    max_pbo: float = 0.5                 # Probability of Backtest Overfitting (CSCV) harus < 0.5
    min_is_profit_factor: float = 1.10   # setelah dioptimasi pun in-sample harus jelas untung
