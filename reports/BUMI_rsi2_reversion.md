## Validasi rsi2_reversion @ BUMI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 18 < 30: belum cukup bukti
- GAGAL: PF OOS 0.39 < 1.15
- GAGAL: PF in-sample 1.05 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 63% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.31 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 21 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.59 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.85 < buy&hold 0.65: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 18 trade OOS (16.7/100 trade)
- PERINGATAN: parameter tidak stabil antar fold (40%)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 32 | 18 | 18 |
| Profit factor | 1.05 | 0.39 | 0.31 |
| Win rate | 58.8% | 33.3% | 33.3% |
| Expectancy (R) | 0.00 | -0.22 | -0.27 |
| Sharpe | 0.02 | -0.85 | -1.01 |
| Max DD | -2.9% | -5.4% | -5.9% |
| CAGR | 0.0% | -1.5% | -1.7% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 21 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.59 (harus < 0.5)
- Buy & hold jendela OOS: return +82.6%, Sharpe 0.65, maxDD -72.0% | strategi: return -4.0%, Sharpe -0.85, maxDD -5.4%
- Stabilitas parameter antar fold: 40%
- Monte Carlo max DD: median -4.7%, p95 -5.8%
- Parameter terpilih (fold terakhir): {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 0} | 1.10 | 0.00 | 0 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 0} | 1.09 | inf | 4 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 0} | 1.34 | 0.37 | 7 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 1.04 | 0.00 | 3 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 0.70 | 0.00 | 4 |