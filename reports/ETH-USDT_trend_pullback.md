## Validasi trend_pullback @ ETH/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 21 < 30: belum cukup bukti
- GAGAL: PF OOS 1.13 < 1.15
- GAGAL: PF OOS dengan biaya x2.0 = 0.86 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.23 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 21 trade OOS (14.3/100 trade)
- PERINGATAN: parameter tidak stabil antar fold (40%)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 18 | 21 | 21 |
| Profit factor | 0.62 | 1.13 | 0.86 |
| Win rate | 16.8% | 28.6% | 28.6% |
| Expectancy (R) | -0.14 | 0.11 | -0.03 |
| Sharpe | -1.22 | 0.30 | -0.39 |
| Max DD | -5.0% | -2.6% | -3.6% |
| CAGR | -3.6% | 1.2% | -1.7% |

- Deflated Sharpe prob (n_trials=135): 0.23
- Stabilitas parameter antar fold: 40%
- Monte Carlo max DD: median -2.2%, p95 -3.4%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2025-04-23→2026-03-05 | 2026-03-05→2026-04-11 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0} | 0.37 | 0.00 | 1 |
| 2 | 2025-05-29→2026-04-11 | 2026-04-11→2026-05-17 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0} | 0.46 | 3.68 | 2 |
| 3 | 2025-07-05→2026-05-17 | 2026-05-17→2026-06-23 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 0.33 | 0.00 | 0 |
| 4 | 2025-08-10→2026-06-23 | 2026-06-23→2026-07-29 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.47 | 2.78 | 5 |
| 5 | 2025-09-16→2026-07-29 | 2026-07-29→2026-09-04 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 1.45 | 0.41 | 13 |