## Validasi donchian_breakout @ BBCA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 4 < 30: belum cukup bukti
- GAGAL: PF OOS 0.71 < 1.15
- GAGAL: PF in-sample 0.85 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.48 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 4 trade OOS (50.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 16 | 4 | 4 |
| Profit factor | 0.85 | 0.71 | 0.48 |
| Win rate | 35.2% | 50.0% | 50.0% |
| Expectancy (R) | -0.12 | -0.07 | -0.26 |
| Sharpe | -0.11 | -0.13 | -0.28 |
| Max DD | -4.6% | -2.5% | -2.9% |
| CAGR | -0.3% | -0.2% | -0.5% |

- Deflated Sharpe prob (n_trials=45): 0.01
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'donchian_n': 20, 'rr': 3.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'donchian_n': 20, 'rr': 2.0} | 0.86 | 1.02 | 2 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'donchian_n': 20, 'rr': 2.0} | 0.85 | 0.36 | 2 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'donchian_n': 20, 'rr': 2.0} | 0.87 | 0.00 | 0 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'donchian_n': 20, 'rr': 3.0} | 0.83 | 0.00 | 0 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-03 | {'donchian_n': 20, 'rr': 3.0} | 0.83 | 0.00 | 0 |