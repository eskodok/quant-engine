## Validasi trend_pullback @ BNB/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 19 < 30: belum cukup bukti
- GAGAL: PF OOS dengan biaya x2.0 = 0.87 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.26 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 19 trade OOS (15.8/100 trade)
- PERINGATAN: parameter tidak stabil antar fold (40%)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 23 | 19 | 19 |
| Profit factor | 1.40 | 1.16 | 0.87 |
| Win rate | 31.7% | 36.8% | 36.8% |
| Expectancy (R) | 0.26 | 0.11 | -0.04 |
| Sharpe | 0.71 | 0.39 | -0.39 |
| Max DD | -2.4% | -3.0% | -3.4% |
| CAGR | 2.4% | 1.3% | -1.4% |

- Deflated Sharpe prob (n_trials=135): 0.26
- Stabilitas parameter antar fold: 40%
- Monte Carlo max DD: median -2.0%, p95 -3.0%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2025-04-23→2026-03-05 | 2026-03-05→2026-04-11 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0} | 1.44 | 0.00 | 1 |
| 2 | 2025-05-29→2026-04-11 | 2026-04-11→2026-05-17 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0} | 1.46 | 6.34 | 2 |
| 3 | 2025-07-05→2026-05-17 | 2026-05-17→2026-06-23 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 1.80 | 0.00 | 5 |
| 4 | 2025-08-10→2026-06-23 | 2026-06-23→2026-07-29 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 1.13 | 0.00 | 0 |
| 5 | 2025-09-16→2026-07-29 | 2026-07-29→2026-09-04 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 1.15 | 2.31 | 11 |