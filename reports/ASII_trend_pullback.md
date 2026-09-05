## Validasi trend_pullback @ ASII

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 9 < 30: belum cukup bukti
- PERINGATAN: deflated Sharpe prob 0.14 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 9 trade OOS (33.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 10 | 9 | 9 |
| Profit factor | 0.52 | 1.74 | 1.22 |
| Win rate | 19.8% | 44.4% | 33.3% |
| Expectancy (R) | -0.21 | 0.22 | 0.10 |
| Sharpe | -0.48 | 0.52 | 0.19 |
| Max DD | -2.7% | -2.0% | -2.4% |
| CAGR | -0.5% | 0.7% | 0.3% |

- Deflated Sharpe prob (n_trials=135): 0.14
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -1.3%, p95 -1.8%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2020-09-04→2024-09-03 | 2024-09-04→2025-01-22 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.69 | 0.00 | 0 |
| 2 | 2021-01-27→2025-01-22 | 2025-01-23→2025-07-01 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.23 | 0.00 | 0 |
| 3 | 2021-06-21→2025-07-01 | 2025-07-02→2025-11-13 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.30 | inf | 2 |
| 4 | 2021-11-05→2025-11-13 | 2025-11-14→2026-04-14 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.67 | 0.80 | 7 |
| 5 | 2022-03-24→2026-04-14 | 2026-04-15→2026-08-31 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.70 | 0.00 | 0 |