## Validasi bollinger_reversion @ BBCA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 4 < 30: belum cukup bukti
- GAGAL: PF OOS dengan biaya x2.0 = 0.92 < 1: edge habis dimakan biaya
- GAGAL: PBO 0.50 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: deflated Sharpe prob 0.03 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 4 trade OOS (75.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 17 | 4 | 4 |
| Profit factor | 2.04 | 1.57 | 0.92 |
| Win rate | 68.1% | 75.0% | 75.0% |
| Expectancy (R) | 0.20 | 0.17 | -0.02 |
| Sharpe | 0.29 | 0.18 | -0.03 |
| Max DD | -3.7% | -1.1% | -1.2% |
| CAGR | 0.5% | 0.2% | -0.0% |

- Deflated Sharpe prob (n_trials=40): 0.03
- Timing vs entry acak: persentil 91 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.50 (harus < 0.5)
- Buy & hold jendela OOS: return -23.9%, Sharpe -0.21, maxDD -55.7% | strategi: return +0.6%, Sharpe 0.18, maxDD -1.1%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.98 | inf | 3 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.03 | 0.00 | 1 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 2.13 | 0.00 | 0 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 3.12 | 0.00 | 0 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-07 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 2.93 | 0.00 | 0 |