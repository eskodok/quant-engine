## Validasi tsmom @ TPIA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.99 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- PERINGATAN: deflated Sharpe prob 0.20 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 7 trade OOS (28.6/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 15 | 7 | 7 |
| Profit factor | 0.99 | 3.65 | 3.30 |
| Win rate | 20.7% | 28.6% | 28.6% |
| Expectancy (R) | 0.09 | 1.00 | 0.92 |
| Sharpe | -0.06 | 0.79 | 0.74 |
| Max DD | -28.4% | -12.2% | -12.7% |
| CAGR | -0.4% | 10.3% | 9.6% |

- Deflated Sharpe prob (n_trials=30): 0.20
- Timing vs entry acak: persentil 83 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.14 (harus < 0.5)
- Buy & hold jendela OOS: return -30.0%, Sharpe 0.22, maxDD -87.7% | strategi: return +31.2%, Sharpe 0.79, maxDD -12.2%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -8.0%, p95 -13.5%
- Parameter terpilih (fold terakhir): {'lookback': 250, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'lookback': 250, 'rebalance': 10} | 0.03 | 15.90 | 3 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'lookback': 120, 'rebalance': 10} | 1.23 | 0.00 | 2 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'lookback': 120, 'rebalance': 10} | 2.10 | 0.00 | 1 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'lookback': 250, 'rebalance': 10} | 0.67 | 0.00 | 1 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-07 | {'lookback': 250, 'rebalance': 10} | 0.94 | 0.00 | 0 |