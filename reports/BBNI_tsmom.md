## Validasi tsmom @ BBNI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 6 < 30: belum cukup bukti
- GAGAL: PF OOS 0.26 < 1.15
- GAGAL: degradasi IS→OOS 78% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.19 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 44 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.74 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.43 < buy&hold -0.05: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 6 trade OOS (33.3/100 trade)
- PERINGATAN: parameter tidak stabil antar fold (40%)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 14 | 6 | 6 |
| Profit factor | 1.19 | 0.26 | 0.19 |
| Win rate | 24.3% | 16.7% | 16.7% |
| Expectancy (R) | 0.19 | -0.37 | -0.45 |
| Sharpe | 0.13 | -0.43 | -0.56 |
| Max DD | -19.6% | -22.7% | -24.8% |
| CAGR | 1.0% | -3.7% | -4.7% |

- Deflated Sharpe prob (n_trials=30): 0.00
- Timing vs entry acak: persentil 44 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.74 (harus < 0.5)
- Buy & hold jendela OOS: return -18.8%, Sharpe -0.05, maxDD -51.6% | strategi: return -9.9%, Sharpe -0.43, maxDD -22.7%
- Stabilitas parameter antar fold: 40%
- Monte Carlo max DD: median -11.1%, p95 -13.6%
- Parameter terpilih (fold terakhir): {'lookback': 120, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'lookback': 120, 'rebalance': 21} | 0.35 | inf | 1 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'lookback': 250, 'rebalance': 21} | 1.44 | 0.00 | 2 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'lookback': 250, 'rebalance': 10} | 1.06 | 0.00 | 0 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'lookback': 250, 'rebalance': 10} | 1.71 | 0.00 | 2 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'lookback': 120, 'rebalance': 10} | 1.37 | 0.00 | 1 |