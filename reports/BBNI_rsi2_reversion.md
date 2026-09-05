## Validasi rsi2_reversion @ BBNI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 15 < 30: belum cukup bukti
- GAGAL: PF OOS 0.37 < 1.15
- GAGAL: PF in-sample 0.52 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.18 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 19 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: Sharpe OOS -0.82 < buy&hold -0.09: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 15 trade OOS (20.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 35 | 15 | 15 |
| Profit factor | 0.52 | 0.37 | 0.18 |
| Win rate | 56.1% | 46.7% | 33.3% |
| Expectancy (R) | -0.13 | -0.23 | -0.35 |
| Sharpe | -0.59 | -0.82 | -1.26 |
| Max DD | -6.6% | -3.7% | -5.1% |
| CAGR | -0.9% | -1.1% | -1.7% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 19 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.17 (harus < 0.5)
- Buy & hold jendela OOS: return -21.5%, Sharpe -0.09, maxDD -51.6% | strategi: return -3.0%, Sharpe -0.82, maxDD -3.7%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -3.6%, p95 -4.4%
- Parameter terpilih (fold terakhir): {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 0.58 | 0.49 | 6 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 1} | 0.52 | 0.23 | 4 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 0.51 | 0.00 | 0 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 1} | 0.53 | 0.20 | 4 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 0.44 | inf | 1 |