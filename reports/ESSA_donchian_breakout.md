## Validasi donchian_breakout @ ESSA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 5 < 30: belum cukup bukti
- GAGAL: PF OOS 0.40 < 1.15
- GAGAL: degradasi IS→OOS 64% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.35 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 56 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.66 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.51 < buy&hold 0.28: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 5 trade OOS (40.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 16 | 5 | 5 |
| Profit factor | 1.13 | 0.40 | 0.35 |
| Win rate | 39.5% | 20.0% | 20.0% |
| Expectancy (R) | 0.05 | -0.39 | -0.45 |
| Sharpe | 0.07 | -0.51 | -0.60 |
| Max DD | -4.6% | -3.9% | -4.2% |
| CAGR | 0.1% | -0.7% | -0.8% |

- Deflated Sharpe prob (n_trials=45): 0.00
- Timing vs entry acak: persentil 56 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.66 (harus < 0.5)
- Buy & hold jendela OOS: return +3.2%, Sharpe 0.28, maxDD -47.7% | strategi: return -1.9%, Sharpe -0.51, maxDD -3.9%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -2.9%, p95 -3.2%
- Parameter terpilih (fold terakhir): {'donchian_n': 20, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-30 | {'donchian_n': 20, 'rr': 2.0} | 1.52 | 0.00 | 1 |
| 2 | 2019-03-15→2024-05-30 | 2024-05-31→2024-12-11 | {'donchian_n': 20, 'rr': 2.0} | 1.46 | 0.00 | 2 |
| 3 | 2019-09-23→2024-12-11 | 2024-12-12→2025-07-21 | {'donchian_n': 20, 'rr': 2.0} | 1.09 | 0.00 | 1 |
| 4 | 2020-04-06→2025-07-21 | 2025-07-22→2026-02-04 | {'donchian_n': 20, 'rr': 2.0} | 0.99 | 0.00 | 0 |
| 5 | 2020-10-27→2026-02-04 | 2026-02-05→2026-08-31 | {'donchian_n': 20, 'rr': 1.5} | 0.58 | inf | 1 |