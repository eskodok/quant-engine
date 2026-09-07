## Validasi rsi2_reversion @ AKRA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 24 < 30: belum cukup bukti
- GAGAL: PF OOS 0.50 < 1.15
- GAGAL: degradasi IS→OOS 65% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.34 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 39 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: Sharpe OOS -0.79 < buy&hold 0.20: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 24 trade OOS (12.5/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 57 | 24 | 24 |
| Profit factor | 1.43 | 0.50 | 0.34 |
| Win rate | 66.4% | 41.7% | 37.5% |
| Expectancy (R) | 0.08 | -0.15 | -0.23 |
| Sharpe | 0.44 | -0.79 | -1.19 |
| Max DD | -2.9% | -4.4% | -5.9% |
| CAGR | 0.8% | -1.3% | -2.0% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 39 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.29 (harus < 0.5)
- Buy & hold jendela OOS: return +0.7%, Sharpe 0.20, maxDD -51.4% | strategi: return -3.6%, Sharpe -0.79, maxDD -4.4%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -4.6%, p95 -5.9%
- Parameter terpilih (fold terakhir): {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 1} | 1.76 | 0.27 | 7 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 0} | 1.43 | 0.22 | 5 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 0} | 1.20 | 0.00 | 1 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 0} | 1.41 | 2.65 | 4 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-07 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 0} | 1.36 | 0.66 | 7 |