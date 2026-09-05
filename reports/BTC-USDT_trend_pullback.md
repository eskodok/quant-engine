## Validasi trend_pullback @ BTC/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 16 < 30: belum cukup bukti
- GAGAL: PF OOS 0.83 < 1.15
- GAGAL: PF OOS dengan biaya x2.0 = 0.64 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.09 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 16 trade OOS (18.8/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 14 | 16 | 16 |
| Profit factor | 0.58 | 0.83 | 0.64 |
| Win rate | 28.4% | 31.2% | 31.2% |
| Expectancy (R) | -0.20 | -0.18 | -0.32 |
| Sharpe | -1.15 | -0.60 | -1.46 |
| Max DD | -2.7% | -3.2% | -3.9% |
| CAGR | -2.0% | -1.6% | -3.8% |

- Deflated Sharpe prob (n_trials=135): 0.09
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -2.4%, p95 -3.5%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2025-04-23→2026-03-05 | 2026-03-05→2026-04-11 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.51 | 0.00 | 0 |
| 2 | 2025-05-29→2026-04-11 | 2026-04-11→2026-05-17 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.50 | 1.14 | 8 |
| 3 | 2025-07-05→2026-05-17 | 2026-05-17→2026-06-23 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.75 | 0.00 | 0 |
| 4 | 2025-08-10→2026-06-23 | 2026-06-23→2026-07-29 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.62 | 0.00 | 3 |
| 5 | 2025-09-16→2026-07-29 | 2026-07-29→2026-09-04 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.53 | 0.92 | 5 |