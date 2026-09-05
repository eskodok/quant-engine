## Validasi rsi2_reversion @ BTC/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: PF OOS 1.04 < 1.15
- GAGAL: PF OOS dengan biaya x2.0 = 0.87 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 62 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.89 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS 0.06 < buy&hold 0.92: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 52 trade OOS (5.8/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 75 | 52 | 52 |
| Profit factor | 1.32 | 1.04 | 0.87 |
| Win rate | 73.3% | 65.4% | 61.5% |
| Expectancy (R) | 0.05 | 0.01 | -0.03 |
| Sharpe | 0.37 | 0.06 | -0.18 |
| Max DD | -3.1% | -4.5% | -4.9% |
| CAGR | 0.7% | 0.1% | -0.4% |

- Deflated Sharpe prob (n_trials=60): 0.01
- Timing vs entry acak: persentil 62 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.89 (harus < 0.5)
- Buy & hold jendela OOS: return +180.1%, Sharpe 0.92, maxDD -53.0% | strategi: return +0.3%, Sharpe 0.06, maxDD -4.5%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -3.5%, p95 -5.3%
- Parameter terpilih (fold terakhir): {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2017-10-19→2023-05-28 | 2023-05-29→2024-01-21 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 1} | 1.32 | 2.12 | 13 |
| 2 | 2018-06-21→2024-01-21 | 2024-01-22→2024-09-15 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 0} | 1.49 | 0.52 | 17 |
| 3 | 2019-02-14→2024-09-15 | 2024-09-16→2025-05-11 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 0} | 1.17 | 2.51 | 12 |
| 4 | 2019-10-10→2025-05-11 | 2025-05-12→2026-01-04 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 0} | 1.41 | 0.71 | 10 |
| 5 | 2020-06-04→2026-01-04 | 2026-01-05→2026-08-30 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 0} | 1.21 | 0.00 | 0 |