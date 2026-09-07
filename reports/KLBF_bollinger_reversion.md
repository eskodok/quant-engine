## Validasi bollinger_reversion @ KLBF

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 6 < 30: belum cukup bukti
- GAGAL: PF OOS 0.35 < 1.15
- GAGAL: PF in-sample 0.96 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 63% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.24 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 44 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.54 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.75 < buy&hold -0.64: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 6 trade OOS (50.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 14 | 6 | 6 |
| Profit factor | 0.96 | 0.35 | 0.24 |
| Win rate | 61.0% | 50.0% | 50.0% |
| Expectancy (R) | 0.17 | -0.43 | -0.53 |
| Sharpe | -0.03 | -0.75 | -0.93 |
| Max DD | -3.1% | -3.3% | -3.7% |
| CAGR | -0.1% | -0.9% | -1.1% |

- Deflated Sharpe prob (n_trials=40): 0.00
- Timing vs entry acak: persentil 44 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.54 (harus < 0.5)
- Buy & hold jendela OOS: return -55.8%, Sharpe -0.64, maxDD -62.1% | strategi: return -2.5%, Sharpe -0.75, maxDD -3.3%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -3.3%, p95 -3.9%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 0} | 1.03 | 0.00 | 0 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.73 | 0.70 | 2 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.00 | inf | 2 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.32 | 0.00 | 2 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.71 | 0.00 | 0 |