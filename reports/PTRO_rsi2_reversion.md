## Validasi rsi2_reversion @ PTRO

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 25 < 30: belum cukup bukti
- GAGAL: PF OOS 0.47 < 1.15
- GAGAL: degradasi IS→OOS 62% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.38 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 1 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: Sharpe OOS -0.99 < buy&hold 1.52: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 25 trade OOS (12.0/100 trade)
- PERINGATAN: parameter tidak stabil antar fold (40%)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 49 | 25 | 25 |
| Profit factor | 1.25 | 0.47 | 0.38 |
| Win rate | 65.3% | 56.0% | 56.0% |
| Expectancy (R) | 0.05 | -0.20 | -0.24 |
| Sharpe | 0.26 | -0.99 | -1.21 |
| Max DD | -2.6% | -5.7% | -6.4% |
| CAGR | 0.4% | -1.7% | -2.1% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 1 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.24 (harus < 0.5)
- Buy & hold jendela OOS: return +1260.8%, Sharpe 1.52, maxDD -73.2% | strategi: return -4.8%, Sharpe -0.99, maxDD -5.7%
- Stabilitas parameter antar fold: 40%
- Monte Carlo max DD: median -5.8%, p95 -7.2%
- Parameter terpilih (fold terakhir): {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 1.20 | 0.84 | 6 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 1.32 | 1.06 | 3 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 1.42 | 0.29 | 6 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 0} | 1.25 | 0.42 | 8 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 0} | 1.08 | 0.09 | 2 |