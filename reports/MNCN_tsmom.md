## Validasi tsmom @ MNCN

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 3 < 30: belum cukup bukti
- GAGAL: PF OOS 0.00 < 1.15
- GAGAL: PF in-sample 0.03 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 100% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.00 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 0 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.56 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.80 < buy&hold -0.60: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 3 trade OOS (66.7/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 9 | 3 | 3 |
| Profit factor | 0.03 | 0.00 | 0.00 |
| Win rate | 6.1% | 0.0% | 0.0% |
| Expectancy (R) | -0.49 | -0.68 | -0.74 |
| Sharpe | -0.73 | -0.80 | -0.90 |
| Max DD | -22.2% | -9.5% | -9.9% |
| CAGR | -4.2% | -3.1% | -3.5% |

- Deflated Sharpe prob (n_trials=30): 0.00
- Timing vs entry acak: persentil 0 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.56 (harus < 0.5)
- Buy & hold jendela OOS: return -57.7%, Sharpe -0.60, maxDD -59.7% | strategi: return -8.5%, Sharpe -0.80, maxDD -9.5%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'lookback': 120, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'lookback': 60, 'rebalance': 10} | 0.08 | 0.00 | 0 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'lookback': 120, 'rebalance': 10} | 0.03 | 0.00 | 0 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'lookback': 120, 'rebalance': 21} | 0.04 | 0.00 | 0 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'lookback': 120, 'rebalance': 10} | 0.00 | 0.00 | 2 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'lookback': 120, 'rebalance': 10} | 0.00 | 0.00 | 1 |