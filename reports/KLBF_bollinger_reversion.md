## Validasi bollinger_reversion @ KLBF

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 5 < 30: belum cukup bukti
- GAGAL: PF OOS 0.31 < 1.15
- GAGAL: PF in-sample 0.88 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 65% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.22 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 40 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.51 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.81 < buy&hold -0.67: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 5 trade OOS (60.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 13 | 5 | 5 |
| Profit factor | 0.88 | 0.31 | 0.22 |
| Win rate | 59.6% | 40.0% | 40.0% |
| Expectancy (R) | 0.15 | -0.55 | -0.65 |
| Sharpe | -0.07 | -0.81 | -0.95 |
| Max DD | -3.1% | -3.5% | -3.8% |
| CAGR | -0.1% | -1.0% | -1.2% |

- Deflated Sharpe prob (n_trials=40): 0.00
- Timing vs entry acak: persentil 40 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.51 (harus < 0.5)
- Buy & hold jendela OOS: return -57.1%, Sharpe -0.67, maxDD -62.2% | strategi: return -2.7%, Sharpe -0.81, maxDD -3.5%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -3.2%, p95 -3.9%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 0} | 0.92 | 0.00 | 0 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.73 | 0.70 | 2 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.00 | inf | 1 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.04 | 0.00 | 2 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.71 | 0.00 | 0 |