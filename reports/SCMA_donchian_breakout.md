## Validasi donchian_breakout @ SCMA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 6 < 30: belum cukup bukti
- GAGAL: PBO 0.64 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: deflated Sharpe prob 0.07 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 6 trade OOS (33.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 6 | 6 | 6 |
| Profit factor | 2.89 | 2.35 | 2.12 |
| Win rate | 69.5% | 66.7% | 66.7% |
| Expectancy (R) | 0.62 | 0.48 | 0.42 |
| Sharpe | 0.53 | 0.55 | 0.49 |
| Max DD | -2.2% | -3.1% | -3.2% |
| CAGR | 0.7% | 1.0% | 0.9% |

- Deflated Sharpe prob (n_trials=45): 0.07
- Timing vs entry acak: persentil 85 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.64 (harus < 0.5)
- Buy & hold jendela OOS: return +37.8%, Sharpe 0.48, maxDD -61.1% | strategi: return +2.9%, Sharpe 0.55, maxDD -3.1%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -1.1%, p95 -2.1%
- Parameter terpilih (fold terakhir): {'donchian_n': 20, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'donchian_n': 20, 'rr': 1.5} | 3.19 | 0.00 | 0 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'donchian_n': 20, 'rr': 1.5} | 3.19 | 0.00 | 0 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'donchian_n': 20, 'rr': 1.5} | 3.19 | inf | 1 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'donchian_n': 20, 'rr': 1.5} | 2.53 | 1.69 | 5 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'donchian_n': 20, 'rr': 1.5} | 2.34 | 0.00 | 0 |