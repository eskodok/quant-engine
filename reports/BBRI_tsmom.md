## Validasi tsmom @ BBRI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 1 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.34 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.00 < 1: edge habis dimakan biaya
- GAGAL: PBO 0.90 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: deflated Sharpe prob 0.02 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 1 trade OOS (200.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 14 | 1 | 1 |
| Profit factor | 0.34 | inf | 0.00 |
| Win rate | 20.7% | 100.0% | 0.0% |
| Expectancy (R) | -0.34 | 0.02 | -0.10 |
| Sharpe | -0.36 | 0.03 | 0.00 |
| Max DD | -24.6% | -10.1% | -10.1% |
| CAGR | -4.1% | 0.0% | -0.1% |

- Deflated Sharpe prob (n_trials=30): 0.02
- Timing vs entry acak: persentil 100 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.90 (harus < 0.5)
- Buy & hold jendela OOS: return -32.2%, Sharpe -0.27, maxDD -59.5% | strategi: return +0.1%, Sharpe 0.03, maxDD -10.1%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'lookback': 120, 'rebalance': 21}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'lookback': 250, 'rebalance': 10} | 0.34 | inf | 1 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'lookback': 250, 'rebalance': 10} | 0.46 | 0.00 | 0 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'lookback': 250, 'rebalance': 10} | 0.41 | 0.00 | 0 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'lookback': 250, 'rebalance': 10} | 0.27 | 0.00 | 0 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'lookback': 120, 'rebalance': 21} | 0.22 | 0.00 | 0 |