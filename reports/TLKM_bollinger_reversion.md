## Validasi bollinger_reversion @ TLKM

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: PF OOS 0.85 < 1.15
- GAGAL: degradasi IS→OOS 45% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.62 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 7 trade OOS (42.9/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 13 | 7 | 7 |
| Profit factor | 1.54 | 0.85 | 0.62 |
| Win rate | 60.1% | 57.1% | 57.1% |
| Expectancy (R) | 0.05 | -0.10 | -0.25 |
| Sharpe | 0.20 | -0.13 | -0.36 |
| Max DD | -3.2% | -2.7% | -3.0% |
| CAGR | 0.4% | -0.2% | -0.5% |

- Deflated Sharpe prob (n_trials=40): 0.01
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -2.4%, p95 -3.4%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-25 | 2023-10-26→2024-05-30 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 2.82 | 0.21 | 3 |
| 2 | 2019-03-13→2024-05-30 | 2024-05-31→2024-12-12 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.17 | 0.00 | 0 |
| 3 | 2019-09-20→2024-12-12 | 2024-12-13→2025-07-23 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.17 | inf | 1 |
| 4 | 2020-04-06→2025-07-23 | 2025-07-24→2026-02-09 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.10 | inf | 1 |
| 5 | 2020-11-02→2026-02-09 | 2026-02-10→2026-09-03 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.43 | 0.26 | 2 |