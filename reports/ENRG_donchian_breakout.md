## Validasi donchian_breakout @ ENRG

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 13 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.71 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PBO 0.51 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS 0.61 < buy&hold 1.18: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.10 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 13 trade OOS (15.4/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 12 | 13 | 13 |
| Profit factor | 0.71 | 1.87 | 1.65 |
| Win rate | 33.6% | 61.5% | 61.5% |
| Expectancy (R) | -0.20 | 0.37 | 0.30 |
| Sharpe | -0.26 | 0.61 | 0.49 |
| Max DD | -5.6% | -2.4% | -2.5% |
| CAGR | -0.4% | 1.7% | 1.4% |

- Deflated Sharpe prob (n_trials=45): 0.10
- Timing vs entry acak: persentil 83 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.51 (harus < 0.5)
- Buy & hold jendela OOS: return +449.2%, Sharpe 1.18, maxDD -57.1% | strategi: return +4.9%, Sharpe 0.61, maxDD -2.4%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -2.4%, p95 -4.2%
- Parameter terpilih (fold terakhir): {'donchian_n': 55, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'donchian_n': 20, 'rr': 1.5} | 0.51 | 0.00 | 0 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'donchian_n': 20, 'rr': 1.5} | 0.51 | inf | 1 |
| 3 | 2019-09-24→2024-12-16 | 2024-12-17→2025-07-25 | {'donchian_n': 20, 'rr': 1.5} | 0.65 | 1.24 | 2 |
| 4 | 2020-04-08→2025-07-25 | 2025-07-28→2026-02-11 | {'donchian_n': 20, 'rr': 1.5} | 0.50 | 2.28 | 9 |
| 5 | 2020-11-04→2026-02-11 | 2026-02-12→2026-09-04 | {'donchian_n': 55, 'rr': 1.5} | 1.40 | 0.00 | 1 |