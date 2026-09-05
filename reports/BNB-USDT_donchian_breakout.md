## Validasi donchian_breakout @ BNB/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: PF OOS 0.93 < 1.15
- GAGAL: degradasi IS→OOS 40% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.80 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 43 trade OOS (4.7/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 50 | 43 | 43 |
| Profit factor | 1.55 | 0.93 | 0.80 |
| Win rate | 40.2% | 30.2% | 30.2% |
| Expectancy (R) | 0.44 | 0.01 | -0.11 |
| Sharpe | 0.84 | -0.18 | -0.51 |
| Max DD | -5.9% | -6.2% | -7.3% |
| CAGR | 4.1% | -0.8% | -2.2% |

- Deflated Sharpe prob (n_trials=45): 0.01
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -7.4%, p95 -10.9%
- Parameter terpilih (fold terakhir): {'donchian_n': 55, 'rr': 3.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2021-03-15→2024-07-13 | 2024-07-13→2024-12-17 | {'donchian_n': 55, 'rr': 3.0} | 1.59 | 0.72 | 11 |
| 2 | 2021-08-18→2024-12-17 | 2024-12-17→2025-05-22 | {'donchian_n': 55, 'rr': 3.0} | 1.37 | 0.87 | 4 |
| 3 | 2022-01-22→2025-05-22 | 2025-05-22→2025-10-26 | {'donchian_n': 55, 'rr': 3.0} | 1.51 | 2.06 | 15 |
| 4 | 2022-06-27→2025-10-26 | 2025-10-26→2026-03-31 | {'donchian_n': 55, 'rr': 3.0} | 1.68 | 0.00 | 2 |
| 5 | 2022-12-01→2026-03-31 | 2026-03-31→2026-09-04 | {'donchian_n': 55, 'rr': 3.0} | 1.59 | 0.22 | 11 |