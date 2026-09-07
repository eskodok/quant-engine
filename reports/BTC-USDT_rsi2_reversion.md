## Validasi rsi2_reversion @ BTC/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: PF OOS 0.97 < 1.15
- GAGAL: PF OOS dengan biaya x2.0 = 0.81 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 54 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.89 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.04 < buy&hold 0.93: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 51 trade OOS (5.9/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 75 | 51 | 51 |
| Profit factor | 1.31 | 0.97 | 0.81 |
| Win rate | 73.3% | 64.7% | 60.8% |
| Expectancy (R) | 0.05 | -0.01 | -0.04 |
| Sharpe | 0.36 | -0.04 | -0.28 |
| Max DD | -3.1% | -4.5% | -4.9% |
| CAGR | 0.7% | -0.1% | -0.7% |

- Deflated Sharpe prob (n_trials=60): 0.01
- Timing vs entry acak: persentil 54 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.89 (harus < 0.5)
- Buy & hold jendela OOS: return +188.2%, Sharpe 0.93, maxDD -53.0% | strategi: return -0.4%, Sharpe -0.04, maxDD -4.5%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -3.7%, p95 -5.6%
- Parameter terpilih (fold terakhir): {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2017-10-19→2023-05-29 | 2023-05-30→2024-01-23 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 1} | 1.32 | 1.78 | 13 |
| 2 | 2018-06-22→2024-01-23 | 2024-01-24→2024-09-18 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 0} | 1.45 | 0.45 | 16 |
| 3 | 2019-02-16→2024-09-18 | 2024-09-19→2025-05-15 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 0} | 1.17 | 2.51 | 12 |
| 4 | 2019-10-13→2025-05-15 | 2025-05-16→2026-01-09 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 0} | 1.41 | 0.71 | 10 |
| 5 | 2020-06-08→2026-01-09 | 2026-01-10→2026-09-05 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 0} | 1.21 | 0.00 | 0 |