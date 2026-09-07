## Validasi tsmom @ UNTR

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: PF OOS 0.37 < 1.15
- GAGAL: PF in-sample 0.76 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 51% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.28 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 38 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.61 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.11 < buy&hold 0.21: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 7 trade OOS (28.6/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 15 | 7 | 7 |
| Profit factor | 0.76 | 0.37 | 0.28 |
| Win rate | 14.0% | 14.3% | 14.3% |
| Expectancy (R) | -0.18 | -0.26 | -0.36 |
| Sharpe | -0.13 | -0.11 | -0.18 |
| Max DD | -22.1% | -21.6% | -22.0% |
| CAGR | -1.9% | -2.5% | -3.4% |

- Deflated Sharpe prob (n_trials=30): 0.01
- Timing vs entry acak: persentil 38 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.61 (harus < 0.5)
- Buy & hold jendela OOS: return +3.7%, Sharpe 0.21, maxDD -35.8% | strategi: return -6.8%, Sharpe -0.11, maxDD -21.6%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -9.7%, p95 -11.1%
- Parameter terpilih (fold terakhir): {'lookback': 60, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'lookback': 60, 'rebalance': 10} | 0.60 | 0.00 | 1 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'lookback': 60, 'rebalance': 10} | 0.56 | 0.73 | 3 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'lookback': 60, 'rebalance': 10} | 0.97 | 0.00 | 0 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'lookback': 60, 'rebalance': 10} | 0.80 | 0.00 | 2 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'lookback': 60, 'rebalance': 10} | 0.88 | 0.00 | 1 |