## Validasi bollinger_reversion @ TPIA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 9 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.66 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PBO 0.69 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: deflated Sharpe prob 0.04 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 9 trade OOS (33.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 16 | 9 | 9 |
| Profit factor | 0.66 | 1.51 | 1.22 |
| Win rate | 42.9% | 66.7% | 66.7% |
| Expectancy (R) | -0.20 | 0.20 | 0.10 |
| Sharpe | -0.36 | 0.32 | 0.15 |
| Max DD | -6.4% | -2.9% | -3.3% |
| CAGR | -0.7% | 0.6% | 0.3% |

- Deflated Sharpe prob (n_trials=40): 0.04
- Timing vs entry acak: persentil 91 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.69 (harus < 0.5)
- Buy & hold jendela OOS: return -30.0%, Sharpe 0.22, maxDD -87.7% | strategi: return +1.6%, Sharpe 0.32, maxDD -2.9%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -2.1%, p95 -3.1%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.36 | inf | 2 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.53 | 0.95 | 4 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 0} | 0.76 | inf | 1 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 0} | 0.79 | 0.42 | 2 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-07 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.86 | 0.00 | 0 |