## Validasi tsmom @ BTC/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 15 < 30: belum cukup bukti
- GAGAL: PBO 0.76 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS 0.85 < buy&hold 0.93: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.29 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 15 trade OOS (13.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 18 | 15 | 15 |
| Profit factor | 3.57 | 2.50 | 2.38 |
| Win rate | 41.9% | 40.0% | 40.0% |
| Expectancy (R) | 1.13 | 0.80 | 0.76 |
| Sharpe | 1.01 | 0.85 | 0.82 |
| Max DD | -17.9% | -16.7% | -17.0% |
| CAGR | 16.4% | 14.1% | 13.4% |

- Deflated Sharpe prob (n_trials=30): 0.29
- Timing vs entry acak: persentil 86 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.76 (harus < 0.5)
- Buy & hold jendela OOS: return +188.2%, Sharpe 0.93, maxDD -53.0% | strategi: return +54.1%, Sharpe 0.85, maxDD -16.7%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -12.7%, p95 -22.1%
- Parameter terpilih (fold terakhir): {'lookback': 60, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2017-10-19→2023-05-29 | 2023-05-30→2024-01-23 | {'lookback': 250, 'rebalance': 10} | 3.79 | 1.91 | 5 |
| 2 | 2018-06-22→2024-01-23 | 2024-01-24→2024-09-18 | {'lookback': 250, 'rebalance': 10} | 4.17 | 2.68 | 3 |
| 3 | 2019-02-16→2024-09-18 | 2024-09-19→2025-05-15 | {'lookback': 120, 'rebalance': 10} | 4.34 | 3.49 | 4 |
| 4 | 2019-10-13→2025-05-15 | 2025-05-16→2026-01-09 | {'lookback': 250, 'rebalance': 10} | 2.70 | 0.97 | 2 |
| 5 | 2020-06-08→2026-01-09 | 2026-01-10→2026-09-05 | {'lookback': 60, 'rebalance': 10} | 2.84 | inf | 1 |