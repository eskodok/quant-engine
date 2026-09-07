## Validasi bollinger_reversion @ ICBP

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 8 < 30: belum cukup bukti
- GAGAL: PF OOS 0.99 < 1.15
- GAGAL: PF OOS dengan biaya x2.0 = 0.69 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 8 trade OOS (37.5/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 14 | 8 | 8 |
| Profit factor | 1.49 | 0.99 | 0.69 |
| Win rate | 64.2% | 50.0% | 50.0% |
| Expectancy (R) | 0.18 | 0.00 | -0.15 |
| Sharpe | 0.25 | -0.00 | -0.25 |
| Max DD | -2.4% | -2.4% | -2.8% |
| CAGR | 0.4% | -0.0% | -0.4% |

- Deflated Sharpe prob (n_trials=40): 0.01
- Timing vs entry acak: persentil 82 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.07 (harus < 0.5)
- Buy & hold jendela OOS: return -27.8%, Sharpe -0.26, maxDD -53.1% | strategi: return -0.0%, Sharpe -0.00, maxDD -2.4%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -2.2%, p95 -3.4%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-30 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.57 | 1.42 | 3 |
| 2 | 2019-03-15→2024-05-30 | 2024-05-31→2024-12-11 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.47 | 0.00 | 1 |
| 3 | 2019-09-23→2024-12-11 | 2024-12-12→2025-07-21 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 2.24 | 0.86 | 4 |
| 4 | 2020-04-06→2025-07-21 | 2025-07-22→2026-02-04 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.98 | 0.00 | 0 |
| 5 | 2020-10-27→2026-02-04 | 2026-02-05→2026-08-31 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.21 | 0.00 | 0 |