## Validasi rsi2_reversion @ BNB/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: PF OOS 0.79 < 1.15
- GAGAL: degradasi IS→OOS 52% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.67 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 38 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.79 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.31 < buy&hold 0.85: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 34 trade OOS (8.8/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 38 | 34 | 34 |
| Profit factor | 1.65 | 0.79 | 0.67 |
| Win rate | 76.0% | 67.6% | 67.6% |
| Expectancy (R) | 0.07 | -0.04 | -0.07 |
| Sharpe | 0.41 | -0.31 | -0.50 |
| Max DD | -2.9% | -3.5% | -3.9% |
| CAGR | 0.6% | -0.6% | -0.9% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 38 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.79 (harus < 0.5)
- Buy & hold jendela OOS: return +126.0%, Sharpe 0.85, maxDD -58.2% | strategi: return -1.5%, Sharpe -0.31, maxDD -3.5%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -3.4%, p95 -4.8%
- Parameter terpilih (fold terakhir): {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 1}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2019-06-19→2024-01-25 | 2024-01-26→2024-08-02 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 1} | 2.57 | 1.22 | 10 |
| 2 | 2019-12-26→2024-08-02 | 2024-08-03→2025-02-08 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 1} | 1.93 | 0.46 | 13 |
| 3 | 2020-07-03→2025-02-08 | 2025-02-09→2025-08-17 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 1} | 1.20 | 3.19 | 4 |
| 4 | 2021-01-09→2025-08-17 | 2025-08-18→2026-02-23 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 1} | 1.29 | 0.81 | 7 |
| 5 | 2021-07-18→2026-02-23 | 2026-02-24→2026-09-01 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 1} | 1.26 | 0.00 | 0 |