## Validasi donchian_breakout @ BUMI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 10 < 30: belum cukup bukti
- GAGAL: PF OOS 1.08 < 1.15
- GAGAL: PF OOS dengan biaya x2.0 = 0.96 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 49 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.87 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS 0.07 < buy&hold 0.65: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.02 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 10 trade OOS (20.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 8 | 10 | 10 |
| Profit factor | 1.39 | 1.08 | 0.96 |
| Win rate | 51.1% | 40.0% | 40.0% |
| Expectancy (R) | 0.20 | 0.04 | -0.03 |
| Sharpe | 0.21 | 0.07 | -0.05 |
| Max DD | -3.1% | -3.6% | -3.9% |
| CAGR | 0.3% | 0.1% | -0.1% |

- Deflated Sharpe prob (n_trials=45): 0.02
- Timing vs entry acak: persentil 49 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.87 (harus < 0.5)
- Buy & hold jendela OOS: return +82.6%, Sharpe 0.65, maxDD -72.0% | strategi: return +0.3%, Sharpe 0.07, maxDD -3.6%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -3.2%, p95 -4.7%
- Parameter terpilih (fold terakhir): {'donchian_n': 20, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'donchian_n': 20, 'rr': 1.5} | 1.66 | 0.00 | 0 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'donchian_n': 20, 'rr': 1.5} | 1.66 | 0.00 | 2 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'donchian_n': 20, 'rr': 1.5} | 1.00 | 0.00 | 1 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'donchian_n': 20, 'rr': 1.5} | 1.02 | 2.88 | 6 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'donchian_n': 20, 'rr': 1.5} | 1.62 | 0.00 | 1 |