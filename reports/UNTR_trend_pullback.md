## Validasi trend_pullback @ UNTR

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 8 < 30: belum cukup bukti
- PERINGATAN: deflated Sharpe prob 0.03 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 8 trade OOS (37.5/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 17 | 8 | 8 |
| Profit factor | 1.34 | 1.92 | 1.49 |
| Win rate | 34.8% | 50.0% | 50.0% |
| Expectancy (R) | 0.30 | 0.32 | 0.17 |
| Sharpe | 0.27 | 0.49 | 0.30 |
| Max DD | -3.0% | -3.0% | -3.5% |
| CAGR | 0.4% | 0.9% | 0.5% |

- Deflated Sharpe prob (n_trials=135): 0.03
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -1.6%, p95 -2.6%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-25 | 2023-10-26→2024-05-30 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 1.64 | 0.00 | 0 |
| 2 | 2019-03-13→2024-05-30 | 2024-05-31→2024-12-12 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 1.31 | 2.03 | 4 |
| 3 | 2019-09-20→2024-12-12 | 2024-12-13→2025-07-23 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 2.0} | 1.15 | 0.00 | 1 |
| 4 | 2020-04-06→2025-07-23 | 2025-07-24→2026-02-09 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 1.08 | 1.86 | 2 |
| 5 | 2020-11-02→2026-02-09 | 2026-02-10→2026-09-03 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 1.49 | inf | 1 |