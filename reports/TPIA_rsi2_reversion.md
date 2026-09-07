## Validasi rsi2_reversion @ TPIA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 25 < 30: belum cukup bukti
- GAGAL: PF OOS 0.43 < 1.15
- GAGAL: PF in-sample 0.48 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.29 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 17 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.57 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -1.10 < buy&hold 0.22: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 25 trade OOS (12.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 44 | 25 | 25 |
| Profit factor | 0.48 | 0.43 | 0.29 |
| Win rate | 57.5% | 56.0% | 48.0% |
| Expectancy (R) | -0.19 | -0.21 | -0.28 |
| Sharpe | -0.93 | -1.10 | -1.48 |
| Max DD | -8.5% | -5.8% | -7.3% |
| CAGR | -1.5% | -1.8% | -2.5% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 17 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.57 (harus < 0.5)
- Buy & hold jendela OOS: return -30.0%, Sharpe 0.22, maxDD -87.7% | strategi: return -5.0%, Sharpe -1.10, maxDD -5.8%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -5.9%, p95 -7.2%
- Parameter terpilih (fold terakhir): {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 1} | 0.38 | 0.64 | 8 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 1} | 0.40 | 0.35 | 8 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 0} | 0.50 | 1.31 | 5 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 0} | 0.48 | 0.15 | 4 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-07 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 0} | 0.61 | 0.00 | 0 |