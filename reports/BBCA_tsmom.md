## Validasi tsmom @ BBCA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: PF OOS 0.00 < 1.15
- GAGAL: PF in-sample 0.61 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 100% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.00 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 0 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: Sharpe OOS -0.28 < buy&hold -0.21: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 7 trade OOS (28.6/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 14 | 7 | 7 |
| Profit factor | 0.61 | 0.00 | 0.00 |
| Win rate | 33.3% | 0.0% | 0.0% |
| Expectancy (R) | -0.12 | -0.29 | -0.42 |
| Sharpe | -0.09 | -0.28 | -0.45 |
| Max DD | -20.2% | -12.1% | -14.2% |
| CAGR | -1.6% | -2.2% | -3.3% |

- Deflated Sharpe prob (n_trials=30): 0.01
- Timing vs entry acak: persentil 0 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.14 (harus < 0.5)
- Buy & hold jendela OOS: return -23.9%, Sharpe -0.21, maxDD -55.7% | strategi: return -5.9%, Sharpe -0.28, maxDD -12.1%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -6.0%, p95 -6.0%
- Parameter terpilih (fold terakhir): {'lookback': 250, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'lookback': 250, 'rebalance': 10} | 0.82 | 0.00 | 4 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'lookback': 120, 'rebalance': 10} | 0.69 | 0.00 | 2 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'lookback': 120, 'rebalance': 10} | 0.84 | 0.00 | 1 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'lookback': 120, 'rebalance': 10} | 0.62 | 0.00 | 0 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-07 | {'lookback': 250, 'rebalance': 10} | 0.09 | 0.00 | 0 |