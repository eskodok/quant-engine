## Validasi donchian_breakout @ BBNI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 3 < 30: belum cukup bukti
- GAGAL: PF OOS 0.35 < 1.15
- GAGAL: degradasi IS→OOS 72% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.27 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 48 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.87 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.33 < buy&hold -0.09: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 3 trade OOS (66.7/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 16 | 3 | 3 |
| Profit factor | 1.25 | 0.35 | 0.27 |
| Win rate | 53.7% | 33.3% | 33.3% |
| Expectancy (R) | 0.17 | -0.48 | -0.60 |
| Sharpe | 0.21 | -0.33 | -0.42 |
| Max DD | -3.7% | -3.0% | -3.1% |
| CAGR | 0.4% | -0.5% | -0.6% |

- Deflated Sharpe prob (n_trials=45): 0.00
- Timing vs entry acak: persentil 48 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.87 (harus < 0.5)
- Buy & hold jendela OOS: return -21.5%, Sharpe -0.09, maxDD -51.6% | strategi: return -1.4%, Sharpe -0.33, maxDD -3.0%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'donchian_n': 40, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'donchian_n': 40, 'rr': 1.5} | 1.28 | 0.69 | 2 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'donchian_n': 40, 'rr': 1.5} | 1.38 | 0.00 | 1 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'donchian_n': 40, 'rr': 1.5} | 1.20 | 0.00 | 0 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'donchian_n': 40, 'rr': 1.5} | 1.18 | 0.00 | 0 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'donchian_n': 40, 'rr': 1.5} | 1.18 | 0.00 | 0 |