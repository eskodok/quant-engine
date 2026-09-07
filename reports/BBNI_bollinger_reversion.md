## Validasi bollinger_reversion @ BBNI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: PF OOS 0.34 < 1.15
- GAGAL: PF in-sample 1.08 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 69% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.25 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 18 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.66 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.70 < buy&hold -0.05: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 7 trade OOS (42.9/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 18 | 7 | 7 |
| Profit factor | 1.08 | 0.34 | 0.25 |
| Win rate | 61.6% | 28.6% | 28.6% |
| Expectancy (R) | 0.04 | -0.55 | -0.67 |
| Sharpe | 0.08 | -0.70 | -0.86 |
| Max DD | -2.7% | -3.7% | -4.6% |
| CAGR | 0.1% | -1.4% | -1.7% |

- Deflated Sharpe prob (n_trials=40): 0.00
- Timing vs entry acak: persentil 18 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.66 (harus < 0.5)
- Buy & hold jendela OOS: return -18.8%, Sharpe -0.05, maxDD -51.6% | strategi: return -3.7%, Sharpe -0.70, maxDD -3.7%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -4.3%, p95 -5.6%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.16 | 0.68 | 3 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.20 | 0.00 | 1 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.05 | 0.00 | 0 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.99 | inf | 1 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.98 | 0.00 | 2 |