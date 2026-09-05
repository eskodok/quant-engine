## Validasi trend_pullback @ BBCA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 1 < 30: belum cukup bukti
- GAGAL: PF OOS 0.00 < 1.15
- GAGAL: degradasi IS→OOS 100% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.00 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 1 trade OOS (300.0/100 trade)
- PERINGATAN: parameter tidak stabil antar fold (40%)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 17 | 1 | 1 |
| Profit factor | 1.05 | 0.00 | 0.00 |
| Win rate | 34.5% | 0.0% | 0.0% |
| Expectancy (R) | 0.06 | -0.52 | -0.65 |
| Sharpe | 0.03 | -0.85 | -0.91 |
| Max DD | -3.1% | -0.5% | -0.6% |
| CAGR | 0.0% | -0.3% | -0.3% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Stabilitas parameter antar fold: 40%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2020-09-04→2024-09-03 | 2024-09-04→2025-01-22 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 1.33 | 0.00 | 1 |
| 2 | 2021-01-27→2025-01-22 | 2025-01-23→2025-07-01 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 1.23 | 0.00 | 0 |
| 3 | 2021-06-21→2025-07-01 | 2025-07-02→2025-11-13 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 0.77 | 0.00 | 0 |
| 4 | 2021-11-05→2025-11-13 | 2025-11-14→2026-04-14 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 1.26 | 0.00 | 0 |
| 5 | 2022-03-24→2026-04-14 | 2026-04-15→2026-09-01 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.68 | 0.00 | 0 |