## Validasi tsmom @ INDF

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 9 < 30: belum cukup bukti
- GAGAL: PF OOS 1.13 < 1.15
- GAGAL: PF in-sample 0.32 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.91 < 1: edge habis dimakan biaya
- GAGAL: PBO 0.59 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS 0.03 < buy&hold 0.22: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.02 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 9 trade OOS (22.2/100 trade)
- PERINGATAN: parameter tidak stabil antar fold (40%)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 14 | 9 | 9 |
| Profit factor | 0.32 | 1.13 | 0.91 |
| Win rate | 13.0% | 22.2% | 11.1% |
| Expectancy (R) | -0.31 | 0.02 | -0.09 |
| Sharpe | -0.47 | 0.03 | -0.14 |
| Max DD | -25.8% | -17.7% | -20.7% |
| CAGR | -3.8% | -0.2% | -1.9% |

- Deflated Sharpe prob (n_trials=30): 0.02
- Timing vs entry acak: persentil 94 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.59 (harus < 0.5)
- Buy & hold jendela OOS: return +7.0%, Sharpe 0.22, maxDD -30.8% | strategi: return -0.4%, Sharpe 0.03, maxDD -17.7%
- Stabilitas parameter antar fold: 40%
- Monte Carlo max DD: median -14.3%, p95 -19.1%
- Parameter terpilih (fold terakhir): {'lookback': 250, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'lookback': 60, 'rebalance': 10} | 0.20 | 0.00 | 1 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'lookback': 120, 'rebalance': 10} | 0.00 | inf | 1 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'lookback': 120, 'rebalance': 10} | 0.98 | 0.04 | 6 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'lookback': 60, 'rebalance': 10} | 0.38 | 0.00 | 1 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'lookback': 250, 'rebalance': 10} | 0.04 | 0.00 | 0 |