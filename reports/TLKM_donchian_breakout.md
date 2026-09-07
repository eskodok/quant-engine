## Validasi donchian_breakout @ TLKM

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 5 < 30: belum cukup bukti
- GAGAL: PF OOS 1.04 < 1.15
- GAGAL: PF in-sample 0.66 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.74 < 1: edge habis dimakan biaya
- GAGAL: PBO 0.61 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 5 trade OOS (40.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 12 | 5 | 5 |
| Profit factor | 0.66 | 1.04 | 0.74 |
| Win rate | 34.7% | 60.0% | 60.0% |
| Expectancy (R) | -0.26 | -0.06 | -0.20 |
| Sharpe | -0.29 | 0.02 | -0.11 |
| Max DD | -4.6% | -2.1% | -2.2% |
| CAGR | -0.6% | 0.0% | -0.2% |

- Deflated Sharpe prob (n_trials=45): 0.01
- Timing vs entry acak: persentil 75 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.61 (harus < 0.5)
- Buy & hold jendela OOS: return -23.7%, Sharpe -0.09, maxDD -45.6% | strategi: return +0.1%, Sharpe 0.02, maxDD -2.1%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -1.7%, p95 -1.9%
- Parameter terpilih (fold terakhir): {'donchian_n': 20, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'donchian_n': 20, 'rr': 1.5} | 0.66 | 0.00 | 1 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'donchian_n': 20, 'rr': 1.5} | 0.65 | 0.00 | 0 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'donchian_n': 20, 'rr': 1.5} | 0.65 | 0.00 | 0 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'donchian_n': 20, 'rr': 1.5} | 0.59 | 1.80 | 4 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'donchian_n': 20, 'rr': 1.5} | 0.77 | 0.00 | 0 |