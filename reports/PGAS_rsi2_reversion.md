## Validasi rsi2_reversion @ PGAS

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: PF OOS 0.82 < 1.15
- GAGAL: PF OOS dengan biaya x2.0 = 0.51 < 1: edge habis dimakan biaya
- GAGAL: PBO 0.66 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.28 < buy&hold 0.36: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 31 trade OOS (9.7/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 36 | 31 | 31 |
| Profit factor | 1.11 | 0.82 | 0.51 |
| Win rate | 63.3% | 64.5% | 58.1% |
| Expectancy (R) | 0.02 | -0.06 | -0.16 |
| Sharpe | 0.07 | -0.28 | -0.85 |
| Max DD | -3.0% | -4.1% | -6.3% |
| CAGR | 0.1% | -0.6% | -1.7% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 89 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.66 (harus < 0.5)
- Buy & hold jendela OOS: return +19.7%, Sharpe 0.36, maxDD -44.3% | strategi: return -1.5%, Sharpe -0.28, maxDD -4.1%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -3.9%, p95 -5.5%
- Parameter terpilih (fold terakhir): {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 0} | 0.85 | inf | 2 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 0} | 0.95 | 1.79 | 8 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 0} | 1.26 | 1.13 | 12 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 1} | 1.40 | 0.00 | 1 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 0} | 1.09 | 0.19 | 8 |