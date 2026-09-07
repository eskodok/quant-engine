## Validasi tsmom @ ASII

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 4 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.18 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- PERINGATAN: PBO 0.43 agak tinggi
- PERINGATAN: deflated Sharpe prob 0.16 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 4 trade OOS (50.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 12 | 4 | 4 |
| Profit factor | 0.18 | 3.15 | 2.86 |
| Win rate | 14.0% | 25.0% | 25.0% |
| Expectancy (R) | -0.38 | 1.20 | 1.08 |
| Sharpe | -0.58 | 0.67 | 0.63 |
| Max DD | -26.7% | -6.9% | -7.2% |
| CAGR | -4.1% | 5.2% | 4.9% |

- Deflated Sharpe prob (n_trials=30): 0.16
- Timing vs entry acak: persentil 92 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.43 (harus < 0.5)
- Buy & hold jendela OOS: return -15.3%, Sharpe -0.02, maxDD -41.1% | strategi: return +15.1%, Sharpe 0.67, maxDD -6.9%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'lookback': 60, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'lookback': 60, 'rebalance': 10} | 0.12 | 0.00 | 0 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'lookback': 250, 'rebalance': 10} | 0.00 | 0.00 | 0 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'lookback': 120, 'rebalance': 10} | 0.00 | 0.00 | 0 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'lookback': 60, 'rebalance': 10} | 0.05 | 3.92 | 3 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'lookback': 60, 'rebalance': 10} | 0.76 | 0.00 | 1 |