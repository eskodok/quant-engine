## Validasi tsmom @ BNB/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 10 < 30: belum cukup bukti
- GAGAL: PBO 0.91 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS 0.82 < buy&hold 0.89: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.22 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 10 trade OOS (20.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 18 | 10 | 10 |
| Profit factor | 2.08 | 4.52 | 4.21 |
| Win rate | 30.5% | 50.0% | 50.0% |
| Expectancy (R) | 0.67 | 0.69 | 0.65 |
| Sharpe | 0.65 | 0.82 | 0.79 |
| Max DD | -27.0% | -26.1% | -26.4% |
| CAGR | 10.2% | 15.5% | 14.8% |

- Deflated Sharpe prob (n_trials=30): 0.22
- Timing vs entry acak: persentil 94 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.91 (harus < 0.5)
- Buy & hold jendela OOS: return +136.8%, Sharpe 0.89, maxDD -58.2% | strategi: return +45.5%, Sharpe 0.82, maxDD -26.1%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -6.0%, p95 -10.1%
- Parameter terpilih (fold terakhir): {'lookback': 60, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2019-06-19→2024-01-24 | 2024-01-25→2024-08-01 | {'lookback': 60, 'rebalance': 21} | 1.69 | 79.86 | 2 |
| 2 | 2019-12-26→2024-08-01 | 2024-08-02→2025-02-07 | {'lookback': 60, 'rebalance': 10} | 2.87 | 0.66 | 2 |
| 3 | 2020-07-03→2025-02-07 | 2025-02-08→2025-08-16 | {'lookback': 60, 'rebalance': 10} | 2.15 | 4.55 | 3 |
| 4 | 2021-01-09→2025-08-16 | 2025-08-17→2026-02-22 | {'lookback': 250, 'rebalance': 21} | 1.82 | 0.52 | 2 |
| 5 | 2021-07-18→2026-02-22 | 2026-02-23→2026-08-31 | {'lookback': 60, 'rebalance': 10} | 1.88 | 0.00 | 1 |