## Validasi donchian_breakout @ UNTR

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: PF OOS 0.35 < 1.15
- GAGAL: PF in-sample 0.66 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 46% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.29 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 27 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.51 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.68 < buy&hold 0.21: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 7 trade OOS (28.6/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 10 | 7 | 7 |
| Profit factor | 0.66 | 0.35 | 0.29 |
| Win rate | 35.2% | 28.6% | 28.6% |
| Expectancy (R) | -0.29 | -0.66 | -0.78 |
| Sharpe | -0.35 | -0.68 | -0.82 |
| Max DD | -4.9% | -5.5% | -5.7% |
| CAGR | -0.6% | -1.6% | -1.8% |

- Deflated Sharpe prob (n_trials=45): 0.00
- Timing vs entry acak: persentil 27 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.51 (harus < 0.5)
- Buy & hold jendela OOS: return +3.7%, Sharpe 0.21, maxDD -35.8% | strategi: return -4.4%, Sharpe -0.68, maxDD -5.5%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -5.5%, p95 -6.7%
- Parameter terpilih (fold terakhir): {'donchian_n': 55, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'donchian_n': 20, 'rr': 1.5} | 0.88 | 0.00 | 0 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'donchian_n': 20, 'rr': 1.5} | 0.88 | 1.13 | 2 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'donchian_n': 20, 'rr': 1.5} | 0.84 | 0.00 | 0 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'donchian_n': 55, 'rr': 1.5} | 0.36 | 0.24 | 4 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'donchian_n': 55, 'rr': 1.5} | 0.33 | 0.00 | 1 |