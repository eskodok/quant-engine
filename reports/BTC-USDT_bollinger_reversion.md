## Validasi bollinger_reversion @ BTC/USDT

**Verdict: FIX**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 21 < 30: belum cukup bukti
- PERINGATAN: deflated Sharpe prob 0.31 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 21 trade OOS (14.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 27 | 21 | 21 |
| Profit factor | 1.84 | 2.32 | 2.09 |
| Win rate | 68.2% | 76.2% | 71.4% |
| Expectancy (R) | 0.25 | 0.33 | 0.28 |
| Sharpe | 0.59 | 0.94 | 0.81 |
| Max DD | -3.2% | -1.8% | -1.9% |
| CAGR | 1.3% | 2.1% | 1.8% |

- Deflated Sharpe prob (n_trials=40): 0.31
- Timing vs entry acak: persentil 97 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.17 (harus < 0.5)
- Buy & hold jendela OOS: return +188.2%, Sharpe 0.93, maxDD -53.0% | strategi: return +7.0%, Sharpe 0.94, maxDD -1.8%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -2.0%, p95 -3.3%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2017-10-19→2023-05-29 | 2023-05-30→2024-01-23 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.40 | 2.69 | 5 |
| 2 | 2018-06-22→2024-01-23 | 2024-01-24→2024-09-18 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.55 | 2.09 | 7 |
| 3 | 2019-02-16→2024-09-18 | 2024-09-19→2025-05-15 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.61 | 1.92 | 4 |
| 4 | 2019-10-13→2025-05-15 | 2025-05-16→2026-01-09 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 2.31 | 2.80 | 5 |
| 5 | 2020-06-08→2026-01-09 | 2026-01-10→2026-09-05 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 2.31 | 0.00 | 0 |