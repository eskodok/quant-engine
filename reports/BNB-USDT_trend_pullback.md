## Validasi trend_pullback @ BNB/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: PF OOS 0.50 < 1.15
- GAGAL: degradasi IS→OOS 51% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.40 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 36 trade OOS (8.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 54 | 36 | 36 |
| Profit factor | 1.01 | 0.50 | 0.40 |
| Win rate | 24.9% | 16.7% | 16.7% |
| Expectancy (R) | 0.03 | -0.12 | -0.22 |
| Sharpe | 0.04 | -0.92 | -1.25 |
| Max DD | -6.5% | -6.5% | -8.6% |
| CAGR | 0.1% | -2.8% | -3.9% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -7.4%, p95 -9.5%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 25.0, 'rr': 3.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2021-03-15→2024-07-13 | 2024-07-13→2024-12-17 | {'rsi_pb': 40.0, 'adx_min': 25.0, 'rr': 3.0} | 1.12 | 0.00 | 9 |
| 2 | 2021-08-18→2024-12-17 | 2024-12-17→2025-05-22 | {'rsi_pb': 40.0, 'adx_min': 25.0, 'rr': 3.0} | 0.99 | 0.00 | 2 |
| 3 | 2022-01-22→2025-05-22 | 2025-05-22→2025-10-26 | {'rsi_pb': 40.0, 'adx_min': 25.0, 'rr': 3.0} | 1.01 | 1.17 | 16 |
| 4 | 2022-06-27→2025-10-26 | 2025-10-26→2026-03-31 | {'rsi_pb': 40.0, 'adx_min': 25.0, 'rr': 3.0} | 1.02 | 0.00 | 0 |
| 5 | 2022-12-01→2026-03-31 | 2026-03-31→2026-09-04 | {'rsi_pb': 40.0, 'adx_min': 25.0, 'rr': 3.0} | 0.94 | 0.35 | 9 |