## Validasi tsmom @ ANTM

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 9 < 30: belum cukup bukti
- GAGAL: PF OOS 0.56 < 1.15
- GAGAL: PF in-sample 0.82 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.50 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 44 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.76 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.27 < buy&hold 0.66: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 9 trade OOS (22.2/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 15 | 9 | 9 |
| Profit factor | 0.82 | 0.56 | 0.50 |
| Win rate | 13.0% | 22.2% | 22.2% |
| Expectancy (R) | -0.03 | -0.21 | -0.27 |
| Sharpe | -0.14 | -0.27 | -0.34 |
| Max DD | -27.7% | -15.5% | -16.8% |
| CAGR | -1.2% | -3.5% | -4.3% |

- Deflated Sharpe prob (n_trials=30): 0.01
- Timing vs entry acak: persentil 44 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.76 (harus < 0.5)
- Buy & hold jendela OOS: return +75.1%, Sharpe 0.66, maxDD -46.8% | strategi: return -9.3%, Sharpe -0.27, maxDD -15.5%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -14.7%, p95 -20.1%
- Parameter terpilih (fold terakhir): {'lookback': 120, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'lookback': 120, 'rebalance': 10} | 0.88 | 0.00 | 0 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'lookback': 120, 'rebalance': 10} | 0.94 | 0.00 | 2 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'lookback': 60, 'rebalance': 10} | 1.40 | 0.65 | 4 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'lookback': 120, 'rebalance': 10} | 0.23 | 6.51 | 2 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'lookback': 120, 'rebalance': 10} | 0.63 | 0.00 | 1 |