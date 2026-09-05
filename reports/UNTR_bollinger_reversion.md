## Validasi bollinger_reversion @ UNTR

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 9 < 30: belum cukup bukti
- GAGAL: PF OOS 0.80 < 1.15
- GAGAL: degradasi IS→OOS 42% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.54 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 9 trade OOS (33.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 16 | 9 | 9 |
| Profit factor | 1.38 | 0.80 | 0.54 |
| Win rate | 55.7% | 55.6% | 55.6% |
| Expectancy (R) | 0.13 | -0.09 | -0.24 |
| Sharpe | 0.25 | -0.14 | -0.36 |
| Max DD | -2.7% | -3.1% | -3.5% |
| CAGR | 0.4% | -0.3% | -0.7% |

- Deflated Sharpe prob (n_trials=40): 0.01
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -2.7%, p95 -3.9%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-25 | 2023-10-26→2024-05-30 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.29 | 0.00 | 0 |
| 2 | 2019-03-13→2024-05-30 | 2024-05-31→2024-12-12 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.29 | inf | 2 |
| 3 | 2019-09-20→2024-12-12 | 2024-12-13→2025-07-23 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.49 | 0.49 | 3 |
| 4 | 2020-04-06→2025-07-23 | 2025-07-24→2026-02-09 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.61 | 0.69 | 3 |
| 5 | 2020-11-02→2026-02-09 | 2026-02-10→2026-09-03 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.21 | 0.00 | 1 |