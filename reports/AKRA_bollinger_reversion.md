## Validasi bollinger_reversion @ AKRA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: PF OOS 0.61 < 1.15
- GAGAL: PF in-sample 1.09 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 44% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.44 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 37 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.57 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.32 < buy&hold 0.20: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 7 trade OOS (42.9/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 14 | 7 | 7 |
| Profit factor | 1.09 | 0.61 | 0.44 |
| Win rate | 53.5% | 57.1% | 42.9% |
| Expectancy (R) | 0.08 | -0.18 | -0.29 |
| Sharpe | 0.05 | -0.32 | -0.52 |
| Max DD | -2.7% | -2.5% | -2.5% |
| CAGR | 0.1% | -0.5% | -0.7% |

- Deflated Sharpe prob (n_trials=40): 0.00
- Timing vs entry acak: persentil 37 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.57 (harus < 0.5)
- Buy & hold jendela OOS: return +0.7%, Sharpe 0.20, maxDD -51.4% | strategi: return -1.3%, Sharpe -0.32, maxDD -2.5%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -2.6%, p95 -3.3%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.94 | 1.30 | 3 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.86 | inf | 1 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 0} | 1.51 | 0.00 | 0 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.07 | 0.00 | 0 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-07 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.07 | 0.08 | 3 |