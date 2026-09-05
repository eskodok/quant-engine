## Validasi bollinger_reversion @ ASII

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 6 < 30: belum cukup bukti
- GAGAL: PF OOS 0.57 < 1.15
- GAGAL: degradasi IS→OOS 47% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.46 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 6 trade OOS (50.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 13 | 6 | 6 |
| Profit factor | 1.07 | 0.57 | 0.46 |
| Win rate | 59.8% | 33.3% | 33.3% |
| Expectancy (R) | 0.03 | -0.31 | -0.41 |
| Sharpe | 0.05 | -0.41 | -0.54 |
| Max DD | -2.9% | -3.1% | -3.6% |
| CAGR | 0.1% | -0.7% | -0.9% |

- Deflated Sharpe prob (n_trials=40): 0.00
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -3.1%, p95 -4.1%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-25 | 2023-10-26→2024-05-30 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.03 | 0.00 | 0 |
| 2 | 2019-03-13→2024-05-30 | 2024-05-31→2024-12-12 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.03 | inf | 1 |
| 3 | 2019-09-20→2024-12-12 | 2024-12-13→2025-07-23 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.26 | 0.00 | 0 |
| 4 | 2020-04-06→2025-07-23 | 2025-07-24→2026-02-09 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.16 | 0.00 | 1 |
| 5 | 2020-11-02→2026-02-09 | 2026-02-10→2026-09-03 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.88 | 0.34 | 4 |