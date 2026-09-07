## Validasi tsmom @ ESSA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 5 < 30: belum cukup bukti
- GAGAL: PF OOS 1.13 < 1.15
- GAGAL: PF OOS dengan biaya x2.0 = 0.99 < 1: edge habis dimakan biaya
- GAGAL: PBO 0.86 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS 0.06 < buy&hold 0.28: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.02 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 5 trade OOS (40.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 14 | 5 | 5 |
| Profit factor | 1.66 | 1.13 | 0.99 |
| Win rate | 30.1% | 40.0% | 40.0% |
| Expectancy (R) | 0.33 | -0.02 | -0.07 |
| Sharpe | 0.30 | 0.06 | 0.01 |
| Max DD | -22.4% | -13.5% | -14.1% |
| CAGR | 2.8% | 0.2% | -0.2% |

- Deflated Sharpe prob (n_trials=30): 0.02
- Timing vs entry acak: persentil 94 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.86 (harus < 0.5)
- Buy & hold jendela OOS: return +3.2%, Sharpe 0.28, maxDD -47.7% | strategi: return +0.4%, Sharpe 0.06, maxDD -13.5%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -6.1%, p95 -7.6%
- Parameter terpilih (fold terakhir): {'lookback': 120, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-30 | {'lookback': 60, 'rebalance': 10} | 1.75 | inf | 1 |
| 2 | 2019-03-15→2024-05-30 | 2024-05-31→2024-12-11 | {'lookback': 60, 'rebalance': 10} | 2.26 | inf | 1 |
| 3 | 2019-09-23→2024-12-11 | 2024-12-12→2025-07-21 | {'lookback': 60, 'rebalance': 10} | 2.11 | 0.00 | 0 |
| 4 | 2020-04-06→2025-07-21 | 2025-07-22→2026-02-04 | {'lookback': 250, 'rebalance': 10} | 1.25 | 0.00 | 0 |
| 5 | 2020-10-27→2026-02-04 | 2026-02-05→2026-08-31 | {'lookback': 120, 'rebalance': 10} | 0.92 | 0.00 | 3 |