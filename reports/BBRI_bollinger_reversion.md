## Validasi bollinger_reversion @ BBRI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 5 < 30: belum cukup bukti
- GAGAL: PF OOS 0.20 < 1.15
- GAGAL: PF in-sample 0.90 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 78% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.14 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 5 trade OOS (60.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 17 | 5 | 5 |
| Profit factor | 0.90 | 0.20 | 0.14 |
| Win rate | 49.6% | 20.0% | 20.0% |
| Expectancy (R) | -0.11 | -0.73 | -0.86 |
| Sharpe | -0.08 | -0.76 | -0.88 |
| Max DD | -4.6% | -4.2% | -4.8% |
| CAGR | -0.2% | -1.2% | -1.5% |

- Deflated Sharpe prob (n_trials=40): 0.00
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -3.4%, p95 -4.2%
- Parameter terpilih (fold terakhir): {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 0} | 0.99 | 0.20 | 5 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.67 | 0.00 | 0 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.98 | 0.00 | 0 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.08 | 0.00 | 0 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 0} | 0.76 | 0.00 | 0 |