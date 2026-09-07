## Validasi tsmom @ SCMA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.96 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PBO 0.56 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: deflated Sharpe prob 0.14 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 7 trade OOS (28.6/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 9 | 7 | 7 |
| Profit factor | 0.96 | 7.34 | 5.79 |
| Win rate | 16.0% | 57.1% | 57.1% |
| Expectancy (R) | 0.01 | 0.58 | 0.51 |
| Sharpe | -0.07 | 0.63 | 0.58 |
| Max DD | -17.0% | -9.5% | -9.5% |
| CAGR | -0.5% | 6.1% | 5.5% |

- Deflated Sharpe prob (n_trials=30): 0.14
- Timing vs entry acak: persentil 100 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.56 (harus < 0.5)
- Buy & hold jendela OOS: return +37.8%, Sharpe 0.48, maxDD -61.1% | strategi: return +17.9%, Sharpe 0.63, maxDD -9.5%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -1.6%, p95 -2.5%
- Parameter terpilih (fold terakhir): {'lookback': 120, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'lookback': 120, 'rebalance': 10} | 0.76 | 0.00 | 0 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'lookback': 60, 'rebalance': 10} | 0.95 | 9.51 | 3 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'lookback': 120, 'rebalance': 10} | 0.89 | 1.02 | 2 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'lookback': 60, 'rebalance': 10} | 0.34 | inf | 1 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'lookback': 120, 'rebalance': 10} | 1.87 | 0.00 | 1 |