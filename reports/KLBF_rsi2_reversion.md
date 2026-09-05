## Validasi rsi2_reversion @ KLBF

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 6 < 30: belum cukup bukti
- GAGAL: degradasi IS→OOS 50% > 40%: indikasi overfit
- GAGAL: PBO 0.50 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: deflated Sharpe prob 0.07 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 6 trade OOS (50.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 20 | 6 | 6 |
| Profit factor | 7.94 | 3.95 | 2.11 |
| Win rate | 77.8% | 66.7% | 50.0% |
| Expectancy (R) | 0.24 | 0.24 | 0.13 |
| Sharpe | 0.71 | 0.69 | 0.38 |
| Max DD | -1.5% | -0.7% | -0.9% |
| CAGR | 0.8% | 0.5% | 0.3% |

- Deflated Sharpe prob (n_trials=60): 0.07
- Timing vs entry acak: persentil 98 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.50 (harus < 0.5)
- Buy & hold jendela OOS: return -57.1%, Sharpe -0.67, maxDD -62.2% | strategi: return +1.5%, Sharpe 0.69, maxDD -0.7%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -0.3%, p95 -0.5%
- Parameter terpilih (fold terakhir): {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 1}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 1.68 | 0.00 | 0 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 1} | 1.77 | 9.74 | 4 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 4.10 | inf | 1 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 1} | 13.66 | 0.00 | 1 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 1} | 18.52 | 0.00 | 0 |