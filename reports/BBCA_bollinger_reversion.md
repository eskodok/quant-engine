## Validasi bollinger_reversion @ BBCA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 4 < 30: belum cukup bukti
- PERINGATAN: deflated Sharpe prob 0.03 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 4 trade OOS (75.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 17 | 4 | 4 |
| Profit factor | 2.09 | 1.59 | 1.02 |
| Win rate | 68.1% | 75.0% | 75.0% |
| Expectancy (R) | 0.22 | 0.16 | 0.00 |
| Sharpe | 0.32 | 0.20 | 0.01 |
| Max DD | -3.5% | -1.1% | -1.3% |
| CAGR | 0.6% | 0.2% | 0.0% |

- Deflated Sharpe prob (n_trials=40): 0.03
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.00 | inf | 2 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.27 | 0.47 | 2 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 2.13 | 0.00 | 0 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 3.12 | 0.00 | 0 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-03 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 2.93 | 0.00 | 0 |