## Validasi trend_pullback @ ANTM

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 12 < 30: belum cukup bukti
- GAGAL: PF OOS 0.67 < 1.15
- GAGAL: PF in-sample 0.87 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.58 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 12 trade OOS (25.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 18 | 12 | 12 |
| Profit factor | 0.87 | 0.67 | 0.58 |
| Win rate | 26.0% | 25.0% | 25.0% |
| Expectancy (R) | -0.06 | -0.16 | -0.22 |
| Sharpe | -0.16 | -0.41 | -0.57 |
| Max DD | -4.3% | -2.6% | -2.9% |
| CAGR | -0.2% | -0.7% | -1.0% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -3.9%, p95 -5.4%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 1.37 | 0.00 | 0 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 0.98 | 0.00 | 0 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 0.98 | 0.84 | 5 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.51 | 0.00 | 3 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.49 | 1.44 | 4 |