## Validasi rsi2_reversion @ UNTR

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 13 < 30: belum cukup bukti
- GAGAL: PF OOS 0.48 < 1.15
- GAGAL: PF in-sample 0.68 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.28 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 13 trade OOS (23.1/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 19 | 13 | 13 |
| Profit factor | 0.68 | 0.48 | 0.28 |
| Win rate | 56.8% | 46.2% | 30.8% |
| Expectancy (R) | -0.13 | -0.16 | -0.27 |
| Sharpe | -0.24 | -0.47 | -0.80 |
| Max DD | -3.0% | -3.5% | -4.0% |
| CAGR | -0.3% | -0.7% | -1.2% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -2.6%, p95 -3.5%
- Parameter terpilih (fold terakhir): {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-25 | 2023-10-26→2024-05-30 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 0.56 | inf | 1 |
| 2 | 2019-03-13→2024-05-30 | 2024-05-31→2024-12-12 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 0.55 | 3.07 | 2 |
| 3 | 2019-09-20→2024-12-12 | 2024-12-13→2025-07-23 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 0.66 | inf | 2 |
| 4 | 2020-04-06→2025-07-23 | 2025-07-24→2026-02-09 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 0.89 | 0.77 | 4 |
| 5 | 2020-11-02→2026-02-09 | 2026-02-10→2026-09-03 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 0.77 | 0.00 | 4 |