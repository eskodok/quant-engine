## Validasi tsmom @ BBCA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: PF OOS 0.11 < 1.15
- GAGAL: PF in-sample 0.54 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 80% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.01 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 30 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.54 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.27 < buy&hold -0.20: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 7 trade OOS (28.6/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 15 | 7 | 7 |
| Profit factor | 0.54 | 0.11 | 0.01 |
| Win rate | 25.2% | 28.6% | 14.3% |
| Expectancy (R) | -0.16 | -0.22 | -0.34 |
| Sharpe | -0.14 | -0.27 | -0.44 |
| Max DD | -19.9% | -12.6% | -14.6% |
| CAGR | -2.1% | -2.1% | -3.2% |

- Deflated Sharpe prob (n_trials=30): 0.01
- Timing vs entry acak: persentil 30 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.54 (harus < 0.5)
- Buy & hold jendela OOS: return -23.7%, Sharpe -0.20, maxDD -55.7% | strategi: return -5.6%, Sharpe -0.27, maxDD -12.6%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -5.9%, p95 -6.4%
- Parameter terpilih (fold terakhir): {'lookback': 250, 'rebalance': 21}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'lookback': 250, 'rebalance': 10} | 0.78 | 0.06 | 4 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'lookback': 250, 'rebalance': 10} | 0.64 | 0.46 | 2 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'lookback': 250, 'rebalance': 10} | 0.84 | 0.00 | 1 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'lookback': 120, 'rebalance': 10} | 0.19 | 0.00 | 0 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-03 | {'lookback': 250, 'rebalance': 21} | 0.24 | 0.00 | 0 |