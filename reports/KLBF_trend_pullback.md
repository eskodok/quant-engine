## Validasi trend_pullback @ KLBF

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 3 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.57 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 3 trade OOS (100.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 22 | 3 | 3 |
| Profit factor | 0.57 | 1.60 | 1.13 |
| Win rate | 17.6% | 33.3% | 33.3% |
| Expectancy (R) | -0.18 | 0.16 | 0.04 |
| Sharpe | -0.46 | 0.16 | 0.05 |
| Max DD | -5.6% | -1.0% | -1.1% |
| CAGR | -0.8% | 0.2% | 0.0% |

- Deflated Sharpe prob (n_trials=135): 0.01
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 0.50 | 0.00 | 0 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 0.58 | 4.77 | 2 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 0.55 | 0.00 | 1 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 0.61 | 0.00 | 0 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 0.61 | 0.00 | 0 |