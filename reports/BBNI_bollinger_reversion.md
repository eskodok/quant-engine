## Validasi bollinger_reversion @ BBNI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 8 < 30: belum cukup bukti
- GAGAL: PF OOS 0.37 < 1.15
- GAGAL: degradasi IS→OOS 66% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.26 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 8 trade OOS (37.5/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 18 | 8 | 8 |
| Profit factor | 1.08 | 0.37 | 0.26 |
| Win rate | 61.6% | 37.5% | 37.5% |
| Expectancy (R) | 0.04 | -0.45 | -0.58 |
| Sharpe | 0.08 | -0.65 | -0.83 |
| Max DD | -2.7% | -3.9% | -4.8% |
| CAGR | 0.1% | -1.3% | -1.7% |

- Deflated Sharpe prob (n_trials=40): 0.00
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -4.3%, p95 -5.6%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.16 | 0.76 | 4 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.20 | 0.00 | 1 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.05 | 0.00 | 0 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.99 | inf | 1 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.98 | 0.00 | 2 |