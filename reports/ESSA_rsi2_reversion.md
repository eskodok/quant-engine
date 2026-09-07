## Validasi rsi2_reversion @ ESSA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 13 < 30: belum cukup bukti
- GAGAL: PF OOS 0.27 < 1.15
- GAGAL: degradasi IS→OOS 88% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.16 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 3 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.51 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -1.00 < buy&hold 0.28: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 13 trade OOS (23.1/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 20 | 13 | 13 |
| Profit factor | 2.32 | 0.27 | 0.16 |
| Win rate | 75.3% | 61.5% | 46.2% |
| Expectancy (R) | 0.17 | -0.29 | -0.35 |
| Sharpe | 0.61 | -1.00 | -1.19 |
| Max DD | -1.2% | -5.1% | -5.5% |
| CAGR | 0.7% | -1.4% | -1.7% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 3 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.51 (harus < 0.5)
- Buy & hold jendela OOS: return +3.2%, Sharpe 0.28, maxDD -47.7% | strategi: return -3.8%, Sharpe -1.00, maxDD -5.1%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -4.1%, p95 -4.9%
- Parameter terpilih (fold terakhir): {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 1}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-30 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 2.23 | 0.00 | 0 |
| 2 | 2019-03-15→2024-05-30 | 2024-05-31→2024-12-11 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 2.23 | inf | 5 |
| 3 | 2019-09-23→2024-12-11 | 2024-12-12→2025-07-21 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 2.61 | 0.03 | 6 |
| 4 | 2020-04-06→2025-07-21 | 2025-07-22→2026-02-04 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 1} | 1.92 | 0.00 | 0 |
| 5 | 2020-10-27→2026-02-04 | 2026-02-05→2026-08-31 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 1} | 2.61 | 0.03 | 2 |