## Validasi donchian_breakout @ ASII

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 4 < 30: belum cukup bukti
- GAGAL: PF OOS 0.54 < 1.15
- GAGAL: PF in-sample 0.27 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.47 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 46 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.71 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.28 < buy&hold 0.03: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 4 trade OOS (50.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 8 | 4 | 4 |
| Profit factor | 0.27 | 0.54 | 0.47 |
| Win rate | 23.9% | 50.0% | 50.0% |
| Expectancy (R) | -0.57 | -0.50 | -0.61 |
| Sharpe | -0.50 | -0.28 | -0.34 |
| Max DD | -5.5% | -3.9% | -3.8% |
| CAGR | -0.9% | -0.8% | -0.9% |

- Deflated Sharpe prob (n_trials=45): 0.00
- Timing vs entry acak: persentil 46 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.71 (harus < 0.5)
- Buy & hold jendela OOS: return -11.8%, Sharpe 0.03, maxDD -41.1% | strategi: return -2.1%, Sharpe -0.28, maxDD -3.9%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'donchian_n': 20, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-25 | 2023-10-26→2024-05-30 | {'donchian_n': 20, 'rr': 1.5} | 0.31 | 0.00 | 0 |
| 2 | 2019-03-13→2024-05-30 | 2024-05-31→2024-12-12 | {'donchian_n': 20, 'rr': 1.5} | 0.31 | 0.00 | 0 |
| 3 | 2019-09-20→2024-12-12 | 2024-12-13→2025-07-23 | {'donchian_n': 20, 'rr': 1.5} | 0.31 | 0.00 | 0 |
| 4 | 2020-04-06→2025-07-23 | 2025-07-24→2026-02-09 | {'donchian_n': 20, 'rr': 1.5} | 0.09 | 0.54 | 4 |
| 5 | 2020-11-02→2026-02-09 | 2026-02-10→2026-09-03 | {'donchian_n': 20, 'rr': 1.5} | 0.32 | 0.00 | 0 |