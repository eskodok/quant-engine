## Validasi rsi2_reversion @ INDF

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 14 < 30: belum cukup bukti
- GAGAL: PF OOS 0.53 < 1.15
- GAGAL: degradasi IS→OOS 70% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.30 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 14 trade OOS (21.4/100 trade)
- PERINGATAN: parameter tidak stabil antar fold (40%)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 28 | 14 | 14 |
| Profit factor | 1.74 | 0.53 | 0.30 |
| Win rate | 65.9% | 42.9% | 42.9% |
| Expectancy (R) | 0.11 | -0.16 | -0.27 |
| Sharpe | 0.30 | -0.59 | -1.00 |
| Max DD | -2.2% | -3.1% | -4.4% |
| CAGR | 0.4% | -0.8% | -1.4% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Stabilitas parameter antar fold: 40%
- Monte Carlo max DD: median -3.2%, p95 -4.1%
- Parameter terpilih (fold terakhir): {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 0} | 2.24 | 0.00 | 1 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 0} | 2.20 | inf | 2 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 0} | 2.01 | 0.52 | 6 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 1.61 | 0.25 | 4 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 0} | 0.64 | inf | 1 |