## Validasi trend_pullback @ BBRI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 5 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.52 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 5 trade OOS (60.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 24 | 5 | 5 |
| Profit factor | 0.52 | 1.49 | 1.11 |
| Win rate | 24.8% | 60.0% | 60.0% |
| Expectancy (R) | -0.19 | 0.58 | 0.30 |
| Sharpe | -0.60 | 0.29 | 0.08 |
| Max DD | -5.8% | -1.2% | -1.3% |
| CAGR | -1.0% | 0.3% | 0.1% |

- Deflated Sharpe prob (n_trials=135): 0.01
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -1.1%, p95 -1.6%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 0.28 | 1.49 | 5 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 0.53 | 0.00 | 0 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 0.62 | 0.00 | 0 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 0.60 | 0.00 | 0 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 0.60 | 0.00 | 0 |