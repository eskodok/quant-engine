## Validasi rsi2_reversion @ BMRI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: degradasi IS→OOS 57% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.61 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 7 trade OOS (42.9/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 21 | 7 | 7 |
| Profit factor | 2.68 | 1.16 | 0.61 |
| Win rate | 55.1% | 71.4% | 57.1% |
| Expectancy (R) | 0.13 | 0.03 | -0.09 |
| Sharpe | 0.37 | 0.07 | -0.20 |
| Max DD | -1.4% | -1.3% | -1.5% |
| CAGR | 0.5% | 0.1% | -0.2% |

- Deflated Sharpe prob (n_trials=60): 0.01
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -1.0%, p95 -1.3%
- Parameter terpilih (fold terakhir): {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 2.44 | inf | 1 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 2.49 | inf | 4 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 2.91 | 0.00 | 0 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 4.26 | 0.00 | 1 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 0} | 1.33 | 0.00 | 1 |