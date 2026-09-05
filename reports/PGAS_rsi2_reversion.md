## Validasi rsi2_reversion @ PGAS

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: PF OOS 0.77 < 1.15
- GAGAL: PF in-sample 1.09 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.47 < 1: edge habis dimakan biaya
- GAGAL: PBO 0.74 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.37 < buy&hold 0.33: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 31 trade OOS (9.7/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 36 | 31 | 31 |
| Profit factor | 1.09 | 0.77 | 0.47 |
| Win rate | 62.7% | 61.3% | 54.8% |
| Expectancy (R) | 0.01 | -0.08 | -0.18 |
| Sharpe | 0.06 | -0.37 | -0.93 |
| Max DD | -3.0% | -4.5% | -6.8% |
| CAGR | 0.1% | -0.7% | -1.9% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 84 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.74 (harus < 0.5)
- Buy & hold jendela OOS: return +16.2%, Sharpe 0.33, maxDD -44.3% | strategi: return -2.1%, Sharpe -0.37, maxDD -4.5%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -4.1%, p95 -5.8%
- Parameter terpilih (fold terakhir): {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-25 | 2023-10-26→2024-05-30 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 0} | 0.77 | inf | 2 |
| 2 | 2019-03-13→2024-05-30 | 2024-05-31→2024-12-12 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 0} | 0.95 | 1.79 | 8 |
| 3 | 2019-09-20→2024-12-12 | 2024-12-13→2025-07-23 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 0} | 1.26 | 0.90 | 12 |
| 4 | 2020-04-06→2025-07-23 | 2025-07-24→2026-02-09 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 1} | 1.40 | 0.00 | 1 |
| 5 | 2020-11-02→2026-02-09 | 2026-02-10→2026-09-03 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 0} | 1.09 | 0.19 | 8 |