## Validasi rsi2_reversion @ ENRG

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 18 < 30: belum cukup bukti
- GAGAL: PF OOS 0.44 < 1.15
- GAGAL: degradasi IS→OOS 70% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.32 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 4 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.74 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.71 < buy&hold 1.18: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 18 trade OOS (16.7/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 38 | 18 | 18 |
| Profit factor | 1.45 | 0.44 | 0.32 |
| Win rate | 68.6% | 50.0% | 44.4% |
| Expectancy (R) | 0.06 | -0.16 | -0.21 |
| Sharpe | 0.30 | -0.71 | -0.92 |
| Max DD | -1.8% | -4.2% | -4.4% |
| CAGR | 0.4% | -1.0% | -1.3% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 4 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.74 (harus < 0.5)
- Buy & hold jendela OOS: return +449.2%, Sharpe 1.18, maxDD -57.1% | strategi: return -2.8%, Sharpe -0.71, maxDD -4.2%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -3.5%, p95 -4.4%
- Parameter terpilih (fold terakhir): {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 1}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 1} | 1.51 | inf | 1 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 1} | 1.60 | 1.33 | 5 |
| 3 | 2019-09-24→2024-12-16 | 2024-12-17→2025-07-25 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 1} | 1.59 | 0.94 | 4 |
| 4 | 2020-04-08→2025-07-25 | 2025-07-28→2026-02-11 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 1} | 1.26 | 0.46 | 3 |
| 5 | 2020-11-04→2026-02-11 | 2026-02-12→2026-09-04 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 1} | 1.28 | 0.06 | 5 |