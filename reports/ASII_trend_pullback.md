## Validasi trend_pullback @ ASII

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 10 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.83 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- PERINGATAN: deflated Sharpe prob 0.02 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 10 trade OOS (30.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 15 | 10 | 10 |
| Profit factor | 0.83 | 1.55 | 1.07 |
| Win rate | 26.2% | 40.0% | 30.0% |
| Expectancy (R) | -0.05 | 0.17 | 0.05 |
| Sharpe | -0.15 | 0.35 | 0.04 |
| Max DD | -2.8% | -2.3% | -2.8% |
| CAGR | -0.2% | 0.4% | 0.0% |

- Deflated Sharpe prob (n_trials=135): 0.02
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -1.5%, p95 -2.0%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-25 | 2023-10-26→2024-05-30 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.78 | 0.00 | 0 |
| 2 | 2019-03-13→2024-05-30 | 2024-05-31→2024-12-12 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.78 | 0.00 | 0 |
| 3 | 2019-09-20→2024-12-12 | 2024-12-13→2025-07-23 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.78 | 0.00 | 0 |
| 4 | 2020-04-06→2025-07-23 | 2025-07-24→2026-02-09 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.66 | 20.19 | 4 |
| 5 | 2020-11-02→2026-02-09 | 2026-02-10→2026-09-03 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 1.15 | 0.03 | 6 |