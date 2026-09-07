## Validasi rsi2_reversion @ BBNI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 14 < 30: belum cukup bukti
- GAGAL: PF OOS 0.36 < 1.15
- GAGAL: PF in-sample 0.51 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.16 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 28 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: Sharpe OOS -0.73 < buy&hold -0.05: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 14 trade OOS (21.4/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 32 | 14 | 14 |
| Profit factor | 0.51 | 0.36 | 0.16 |
| Win rate | 55.4% | 50.0% | 35.7% |
| Expectancy (R) | -0.14 | -0.21 | -0.33 |
| Sharpe | -0.61 | -0.73 | -1.15 |
| Max DD | -6.2% | -3.2% | -4.5% |
| CAGR | -0.8% | -0.9% | -1.5% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 28 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.17 (harus < 0.5)
- Buy & hold jendela OOS: return -18.8%, Sharpe -0.05, maxDD -51.6% | strategi: return -2.6%, Sharpe -0.73, maxDD -3.2%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -3.1%, p95 -3.8%
- Parameter terpilih (fold terakhir): {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 0.55 | 0.42 | 6 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 0.54 | 0.19 | 3 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 0.51 | 0.00 | 0 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 1} | 0.53 | 0.20 | 4 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 0.44 | inf | 1 |