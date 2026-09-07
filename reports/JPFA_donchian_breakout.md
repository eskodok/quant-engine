## Validasi donchian_breakout @ JPFA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: PBO 0.51 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS 0.18 < buy&hold 0.75: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.03 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 7 trade OOS (28.6/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 7 | 7 | 7 |
| Profit factor | 1.47 | 1.32 | 1.09 |
| Win rate | 49.7% | 42.9% | 42.9% |
| Expectancy (R) | 0.18 | 0.13 | 0.04 |
| Sharpe | 0.18 | 0.18 | 0.06 |
| Max DD | -2.9% | -1.9% | -1.9% |
| CAGR | 0.2% | 0.3% | 0.1% |

- Deflated Sharpe prob (n_trials=45): 0.03
- Timing vs entry acak: persentil 81 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.51 (harus < 0.5)
- Buy & hold jendela OOS: return +88.6%, Sharpe 0.75, maxDD -39.2% | strategi: return +0.9%, Sharpe 0.18, maxDD -1.9%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -1.8%, p95 -2.7%
- Parameter terpilih (fold terakhir): {'donchian_n': 40, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'donchian_n': 20, 'rr': 1.5} | 1.65 | 0.00 | 1 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'donchian_n': 20, 'rr': 1.5} | 1.65 | 2.07 | 3 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'donchian_n': 20, 'rr': 1.5} | 1.75 | 0.00 | 0 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'donchian_n': 20, 'rr': 1.5} | 1.44 | 6.36 | 2 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'donchian_n': 40, 'rr': 1.5} | 0.86 | 0.00 | 1 |