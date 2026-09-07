## Validasi rsi2_reversion @ MAPI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 17 < 30: belum cukup bukti
- GAGAL: PF OOS 0.57 < 1.15
- GAGAL: degradasi IS→OOS 62% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.40 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 46 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.97 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.50 < buy&hold 0.06: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 17 trade OOS (17.6/100 trade)
- PERINGATAN: parameter tidak stabil antar fold (40%)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 37 | 17 | 17 |
| Profit factor | 1.51 | 0.57 | 0.40 |
| Win rate | 64.1% | 47.1% | 35.3% |
| Expectancy (R) | 0.08 | -0.14 | -0.22 |
| Sharpe | 0.38 | -0.50 | -0.76 |
| Max DD | -2.5% | -4.5% | -4.9% |
| CAGR | 0.5% | -0.9% | -1.3% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 46 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.97 (harus < 0.5)
- Buy & hold jendela OOS: return -20.8%, Sharpe 0.06, maxDD -46.0% | strategi: return -2.5%, Sharpe -0.50, maxDD -4.5%
- Stabilitas parameter antar fold: 40%
- Monte Carlo max DD: median -3.7%, p95 -4.9%
- Parameter terpilih (fold terakhir): {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 0} | 2.04 | 0.41 | 10 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 0} | 1.18 | 0.03 | 4 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 1} | 1.28 | 0.00 | 0 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 1.41 | inf | 1 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 1.65 | 2.95 | 2 |