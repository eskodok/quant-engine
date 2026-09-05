## Validasi rsi2_reversion @ BNB/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: PF OOS 0.70 < 1.15
- GAGAL: PF OOS dengan biaya x2.0 = 0.44 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 86 trade OOS (3.5/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 121 | 86 | 86 |
| Profit factor | 1.05 | 0.70 | 0.44 |
| Win rate | 67.8% | 61.6% | 51.2% |
| Expectancy (R) | -0.00 | -0.08 | -0.16 |
| Sharpe | 0.08 | -0.75 | -1.59 |
| Max DD | -5.8% | -6.1% | -10.7% |
| CAGR | 0.2% | -2.4% | -5.0% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -6.9%, p95 -9.0%
- Parameter terpilih (fold terakhir): {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2021-03-15→2024-07-13 | 2024-07-13→2024-12-17 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 1.13 | 0.85 | 24 |
| 2 | 2021-08-18→2024-12-17 | 2024-12-17→2025-05-22 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 1.24 | 1.67 | 17 |
| 3 | 2022-01-22→2025-05-22 | 2025-05-22→2025-10-26 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 1.12 | 0.47 | 24 |
| 4 | 2022-06-27→2025-10-26 | 2025-10-26→2026-03-31 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 0.84 | 0.33 | 7 |
| 5 | 2022-12-01→2026-03-31 | 2026-03-31→2026-09-04 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 0.90 | 0.39 | 14 |