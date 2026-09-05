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
| Profit factor | 1.43 | 0.99 | 0.69 |
| Win rate | 65.2% | 50.0% | 50.0% |
| Expectancy (R) | 0.17 | 0.00 | -0.15 |
| Sharpe | 0.23 | -0.00 | -0.25 |
| Max DD | -2.4% | -2.4% | -2.8% |
| CAGR | 0.3% | -0.0% | -0.4% |

- Deflated Sharpe prob (n_trials=40): 0.01
- Timing vs entry acak: persentil 75 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.06 (harus < 0.5)
- Buy & hold jendela OOS: return -29.4%, Sharpe -0.29, maxDD -53.1% | strategi: return -0.0%, Sharpe -0.00, maxDD -2.4%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -2.2%, p95 -3.4%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.87 | 1.42 | 3 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.47 | 0.00 | 1 |
| 3 | 2019-09-20→2024-12-11 | 2024-12-12→2025-07-22 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.60 | 0.86 | 4 |
| 4 | 2020-04-06→2025-07-22 | 2025-07-23→2026-02-06 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.98 | 0.00 | 0 |
| 5 | 2020-11-02→2026-02-06 | 2026-02-09→2026-09-03 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.21 | 0.00 | 0 |