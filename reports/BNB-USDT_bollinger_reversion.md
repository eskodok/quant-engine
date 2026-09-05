## Validasi bollinger_reversion @ BNB/USDT

**Verdict: FIX**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 17 < 30: belum cukup bukti
- PERINGATAN: deflated Sharpe prob 0.19 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 17 trade OOS (17.6/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 33 | 17 | 17 |
| Profit factor | 1.25 | 2.00 | 1.63 |
| Win rate | 61.0% | 70.6% | 70.6% |
| Expectancy (R) | 0.08 | 0.30 | 0.19 |
| Sharpe | 0.24 | 0.86 | 0.59 |
| Max DD | -5.0% | -2.1% | -2.4% |
| CAGR | 0.7% | 1.8% | 1.2% |

- Deflated Sharpe prob (n_trials=40): 0.19
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -1.6%, p95 -2.7%
- Parameter terpilih (fold terakhir): {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 1}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2021-03-15→2024-07-13 | 2024-07-13→2024-12-17 | {'bb_n': 30, 'bb_k': 2.5, 'need_trend': 1} | 1.09 | 0.64 | 4 |
| 2 | 2021-08-18→2024-12-17 | 2024-12-17→2025-05-22 | {'bb_n': 30, 'bb_k': 2.5, 'need_trend': 1} | 1.05 | 0.00 | 1 |
| 3 | 2022-01-22→2025-05-22 | 2025-05-22→2025-10-26 | {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 0} | 1.09 | 4.98 | 10 |
| 4 | 2022-06-27→2025-10-26 | 2025-10-26→2026-03-31 | {'bb_n': 30, 'bb_k': 2.5, 'need_trend': 1} | 1.53 | 0.00 | 0 |
| 5 | 2022-12-01→2026-03-31 | 2026-03-31→2026-09-04 | {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 1} | 1.49 | inf | 2 |