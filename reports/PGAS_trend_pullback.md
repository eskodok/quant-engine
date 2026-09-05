## Validasi trend_pullback @ PGAS

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 17 < 30: belum cukup bukti
- GAGAL: PF OOS 0.48 < 1.15
- GAGAL: PF in-sample 0.52 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.31 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 17 trade OOS (17.6/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 18 | 17 | 17 |
| Profit factor | 0.52 | 0.48 | 0.31 |
| Win rate | 22.2% | 29.4% | 23.5% |
| Expectancy (R) | -0.18 | -0.19 | -0.30 |
| Sharpe | -0.44 | -0.55 | -0.92 |
| Max DD | -5.3% | -5.4% | -6.7% |
| CAGR | -0.7% | -1.1% | -1.9% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -4.1%, p95 -5.4%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-25 | 2023-10-26→2024-05-30 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.55 | 0.00 | 0 |
| 2 | 2019-03-13→2024-05-30 | 2024-05-31→2024-12-12 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.55 | 0.07 | 4 |
| 3 | 2019-09-20→2024-12-12 | 2024-12-13→2025-07-23 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.45 | 0.62 | 5 |
| 4 | 2020-04-06→2025-07-23 | 2025-07-24→2026-02-09 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.51 | 0.13 | 5 |
| 5 | 2020-11-02→2026-02-09 | 2026-02-10→2026-09-03 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 0.53 | 2.11 | 3 |