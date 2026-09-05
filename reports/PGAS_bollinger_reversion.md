## Validasi bollinger_reversion @ PGAS

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 10 < 30: belum cukup bukti
- GAGAL: PF OOS dengan biaya x2.0 = 0.99 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.03 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 10 trade OOS (30.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 12 | 10 | 10 |
| Profit factor | 1.20 | 1.31 | 0.99 |
| Win rate | 68.3% | 70.0% | 50.0% |
| Expectancy (R) | 0.04 | 0.11 | -0.01 |
| Sharpe | 0.06 | 0.21 | -0.01 |
| Max DD | -3.1% | -3.1% | -3.5% |
| CAGR | 0.1% | 0.4% | -0.0% |

- Deflated Sharpe prob (n_trials=40): 0.03
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -2.5%, p95 -3.5%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-25 | 2023-10-26→2024-05-30 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.48 | inf | 1 |
| 2 | 2019-03-13→2024-05-30 | 2024-05-31→2024-12-12 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.85 | inf | 2 |
| 3 | 2019-09-20→2024-12-12 | 2024-12-13→2025-07-23 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.25 | inf | 2 |
| 4 | 2020-04-06→2025-07-23 | 2025-07-24→2026-02-09 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.70 | inf | 1 |
| 5 | 2020-11-02→2026-02-09 | 2026-02-10→2026-09-03 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.72 | 0.20 | 4 |