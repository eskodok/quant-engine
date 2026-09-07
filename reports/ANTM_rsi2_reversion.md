## Validasi rsi2_reversion @ ANTM

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 16 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.89 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PBO 0.61 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS 0.47 < buy&hold 0.68: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.05 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 16 trade OOS (18.8/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 29 | 16 | 16 |
| Profit factor | 0.89 | 2.77 | 1.20 |
| Win rate | 56.6% | 75.0% | 62.5% |
| Expectancy (R) | -0.02 | 0.08 | 0.01 |
| Sharpe | -0.10 | 0.47 | 0.08 |
| Max DD | -4.1% | -0.8% | -0.9% |
| CAGR | -0.1% | 0.5% | 0.1% |

- Deflated Sharpe prob (n_trials=60): 0.05
- Timing vs entry acak: persentil 98 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.61 (harus < 0.5)
- Buy & hold jendela OOS: return +80.9%, Sharpe 0.68, maxDD -46.8% | strategi: return +1.3%, Sharpe 0.47, maxDD -0.8%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -0.5%, p95 -0.7%
- Parameter terpilih (fold terakhir): {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 1}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 1} | 1.01 | 0.00 | 0 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 1} | 0.90 | inf | 2 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 1} | 0.95 | 4.19 | 5 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 1} | 0.77 | 7.41 | 7 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 1} | 0.81 | 0.21 | 2 |