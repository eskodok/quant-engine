## Validasi rsi2_reversion @ BBRI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 6 < 30: belum cukup bukti
- GAGAL: PF OOS 0.56 < 1.15
- GAGAL: degradasi IS→OOS 77% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.38 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 6 trade OOS (50.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 22 | 6 | 6 |
| Profit factor | 2.47 | 0.56 | 0.38 |
| Win rate | 71.9% | 50.0% | 50.0% |
| Expectancy (R) | 0.19 | -0.23 | -0.36 |
| Sharpe | 0.57 | -0.37 | -0.58 |
| Max DD | -2.6% | -3.1% | -3.4% |
| CAGR | 1.0% | -0.5% | -0.8% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -2.4%, p95 -3.2%
- Parameter terpilih (fold terakhir): {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 4.88 | 0.54 | 4 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 2.55 | 0.00 | 0 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 2.29 | 0.00 | 0 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 1.49 | 0.60 | 2 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 1.13 | 0.00 | 0 |