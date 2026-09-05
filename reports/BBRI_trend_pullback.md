## Validasi trend_pullback @ BBRI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 0 < 30: belum cukup bukti
- GAGAL: PF OOS 0.00 < 1.15
- GAGAL: degradasi IS→OOS 100% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.00 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.03 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 0 trade OOS (300.0/100 trade)
- PERINGATAN: parameter tidak stabil antar fold (40%)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 18 | 0 | 0 |
| Profit factor | 0.60 | 0.00 | 0.00 |
| Win rate | 30.6% | 0.0% | 0.0% |
| Expectancy (R) | -0.06 | 0.00 | 0.00 |
| Sharpe | -0.41 | 0.00 | 0.00 |
| Max DD | -3.8% | 0.0% | 0.0% |
| CAGR | -0.7% | 0.0% | 0.0% |

- Deflated Sharpe prob (n_trials=135): 0.03
- Stabilitas parameter antar fold: 40%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2020-09-04→2024-09-03 | 2024-09-04→2025-01-22 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 0.60 | 0.00 | 0 |
| 2 | 2021-01-27→2025-01-22 | 2025-01-23→2025-07-01 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 0.58 | 0.00 | 0 |
| 3 | 2021-06-21→2025-07-01 | 2025-07-02→2025-11-13 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 0.46 | 0.00 | 0 |
| 4 | 2021-11-05→2025-11-13 | 2025-11-14→2026-04-14 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.75 | 0.00 | 0 |
| 5 | 2022-03-24→2026-04-14 | 2026-04-15→2026-08-31 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.62 | 0.00 | 0 |