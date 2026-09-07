## Validasi rsi2_reversion @ SCMA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 16 < 30: belum cukup bukti
- GAGAL: PF OOS 0.49 < 1.15
- GAGAL: PF in-sample 0.90 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 46% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.37 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 31 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.59 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.61 < buy&hold 0.48: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 16 trade OOS (18.8/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 20 | 16 | 16 |
| Profit factor | 0.90 | 0.49 | 0.37 |
| Win rate | 56.9% | 50.0% | 50.0% |
| Expectancy (R) | -0.03 | -0.14 | -0.18 |
| Sharpe | -0.11 | -0.61 | -0.80 |
| Max DD | -1.7% | -3.4% | -3.7% |
| CAGR | -0.1% | -0.8% | -1.0% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 31 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.59 (harus < 0.5)
- Buy & hold jendela OOS: return +37.8%, Sharpe 0.48, maxDD -61.1% | strategi: return -2.2%, Sharpe -0.61, maxDD -3.4%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -2.9%, p95 -3.7%
- Parameter terpilih (fold terakhir): {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 0} | 0.67 | 0.00 | 0 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 0} | 0.65 | 0.00 | 0 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 1} | 0.83 | 1.15 | 9 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 1.32 | 0.17 | 4 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 0} | 1.02 | 0.05 | 3 |