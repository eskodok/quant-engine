## Validasi rsi2_reversion @ ANTM

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 16 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.88 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PBO 0.61 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS 0.42 < buy&hold 0.66: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.05 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 16 trade OOS (18.8/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 29 | 16 | 16 |
| Profit factor | 0.88 | 2.29 | 1.06 |
| Win rate | 56.6% | 75.0% | 62.5% |
| Expectancy (R) | -0.02 | 0.07 | 0.00 |
| Sharpe | -0.11 | 0.42 | 0.03 |
| Max DD | -4.1% | -1.0% | -1.1% |
| CAGR | -0.1% | 0.4% | 0.0% |

- Deflated Sharpe prob (n_trials=60): 0.05
- Timing vs entry acak: persentil 100 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.61 (harus < 0.5)
- Buy & hold jendela OOS: return +75.1%, Sharpe 0.66, maxDD -46.8% | strategi: return +1.2%, Sharpe 0.42, maxDD -1.0%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -0.5%, p95 -0.9%
- Parameter terpilih (fold terakhir): {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 1}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 1} | 1.01 | 0.00 | 0 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 1} | 0.90 | inf | 2 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 1} | 0.95 | 4.19 | 5 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 1} | 0.77 | 3.43 | 7 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 1} | 0.77 | 0.21 | 2 |