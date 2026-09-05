## Validasi trend_pullback @ BBNI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: PF OOS 1.05 < 1.15
- GAGAL: PF OOS dengan biaya x2.0 = 0.79 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 7 trade OOS (42.9/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 20 | 7 | 7 |
| Profit factor | 1.25 | 1.05 | 0.79 |
| Win rate | 33.6% | 28.6% | 28.6% |
| Expectancy (R) | 0.09 | -0.04 | -0.18 |
| Sharpe | 0.22 | 0.04 | -0.19 |
| Max DD | -3.7% | -3.0% | -3.6% |
| CAGR | 0.4% | 0.1% | -0.3% |

- Deflated Sharpe prob (n_trials=135): 0.01
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -2.3%, p95 -3.5%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 1.00 | 2.42 | 4 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 2.0} | 1.26 | 0.00 | 1 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 1.20 | 0.00 | 0 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 2.0} | 1.30 | 0.00 | 1 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 1.49 | 0.00 | 1 |