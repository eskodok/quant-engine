## Validasi trend_pullback @ SOL/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 14 < 30: belum cukup bukti
- GAGAL: PF OOS 0.37 < 1.15
- GAGAL: degradasi IS→OOS 74% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.29 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.02 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 14 trade OOS (21.4/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 12 | 14 | 14 |
| Profit factor | 1.42 | 0.37 | 0.29 |
| Win rate | 44.7% | 14.3% | 14.3% |
| Expectancy (R) | 0.08 | -0.37 | -0.49 |
| Sharpe | 0.51 | -2.01 | -2.65 |
| Max DD | -2.8% | -4.2% | -5.0% |
| CAGR | 1.9% | -5.6% | -7.4% |

- Deflated Sharpe prob (n_trials=135): 0.02
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -3.4%, p95 -4.3%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2025-04-23→2026-03-05 | 2026-03-05→2026-04-11 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 1.84 | 0.00 | 0 |
| 2 | 2025-05-29→2026-04-11 | 2026-04-11→2026-05-17 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 1.84 | 0.00 | 4 |
| 3 | 2025-07-05→2026-05-17 | 2026-05-17→2026-06-23 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 1.08 | 0.00 | 0 |
| 4 | 2025-08-10→2026-06-23 | 2026-06-23→2026-07-29 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 1.92 | 0.00 | 3 |
| 5 | 2025-09-16→2026-07-29 | 2026-07-29→2026-09-04 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.43 | 1.29 | 7 |