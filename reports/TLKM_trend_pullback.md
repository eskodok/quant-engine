## Validasi trend_pullback @ TLKM

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 3 < 30: belum cukup bukti
- GAGAL: PF OOS 0.00 < 1.15
- GAGAL: degradasi IS→OOS 100% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.00 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 3 trade OOS (100.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 7 | 3 | 3 |
| Profit factor | 0.77 | 0.00 | 0.00 |
| Win rate | 24.0% | 0.0% | 0.0% |
| Expectancy (R) | -0.10 | -0.62 | -0.70 |
| Sharpe | -0.11 | -0.99 | -1.11 |
| Max DD | -2.1% | -1.9% | -2.1% |
| CAGR | -0.1% | -0.9% | -1.1% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2020-09-04→2024-09-03 | 2024-09-04→2025-01-22 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 1.16 | 0.00 | 0 |
| 2 | 2021-01-27→2025-01-22 | 2025-01-23→2025-07-01 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 1.18 | 0.00 | 0 |
| 3 | 2021-06-21→2025-07-01 | 2025-07-02→2025-11-13 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.38 | 0.00 | 1 |
| 4 | 2021-11-05→2025-11-13 | 2025-11-14→2026-04-14 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.69 | 0.00 | 2 |
| 5 | 2022-03-24→2026-04-14 | 2026-04-15→2026-08-31 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.44 | 0.00 | 0 |