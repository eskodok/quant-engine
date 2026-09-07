## Validasi rsi2_reversion @ UNVR

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 10 < 30: belum cukup bukti
- GAGAL: PF OOS 0.87 < 1.15
- GAGAL: PF OOS dengan biaya x2.0 = 0.65 < 1: edge habis dimakan biaya
- GAGAL: PBO 0.99 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 10 trade OOS (30.0/100 trade)
- PERINGATAN: parameter tidak stabil antar fold (40%)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 17 | 10 | 10 |
| Profit factor | 1.28 | 0.87 | 0.65 |
| Win rate | 56.8% | 60.0% | 60.0% |
| Expectancy (R) | -0.00 | -0.04 | -0.12 |
| Sharpe | 0.11 | -0.13 | -0.38 |
| Max DD | -1.8% | -3.2% | -3.5% |
| CAGR | 0.1% | -0.2% | -0.4% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 87 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.99 (harus < 0.5)
- Buy & hold jendela OOS: return -57.7%, Sharpe -0.45, maxDD -74.5% | strategi: return -0.4%, Sharpe -0.13, maxDD -3.2%
- Stabilitas parameter antar fold: 40%
- Monte Carlo max DD: median -2.1%, p95 -3.2%
- Parameter terpilih (fold terakhir): {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 1}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 0} | 1.59 | 0.00 | 0 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 0} | 1.87 | 0.00 | 0 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 0} | 1.30 | 0.00 | 0 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 0} | 0.88 | 0.72 | 9 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 1} | 0.77 | inf | 1 |