## Validasi rsi2_reversion @ ETH/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 20 < 30: belum cukup bukti
- GAGAL: PF OOS 0.93 < 1.15
- GAGAL: PF OOS dengan biaya x2.0 = 0.80 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 41 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: PBO 0.44 agak tinggi
- PERINGATAN: Sharpe OOS -0.06 < buy&hold 0.47: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 20 trade OOS (15.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 25 | 20 | 20 |
| Profit factor | 1.44 | 0.93 | 0.80 |
| Win rate | 72.3% | 60.0% | 60.0% |
| Expectancy (R) | 0.05 | -0.01 | -0.04 |
| Sharpe | 0.19 | -0.06 | -0.17 |
| Max DD | -2.0% | -2.2% | -2.6% |
| CAGR | 0.2% | -0.1% | -0.3% |

- Deflated Sharpe prob (n_trials=60): 0.01
- Timing vs entry acak: persentil 41 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.44 (harus < 0.5)
- Buy & hold jendela OOS: return +36.8%, Sharpe 0.47, maxDD -67.5% | strategi: return -0.3%, Sharpe -0.06, maxDD -2.2%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -2.1%, p95 -3.1%
- Parameter terpilih (fold terakhir): {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 1}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2017-11-09→2023-06-06 | 2023-06-07→2024-01-29 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 1} | 1.54 | 0.28 | 6 |
| 2 | 2018-07-10→2024-01-29 | 2024-01-30→2024-09-22 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 1} | 1.24 | 0.61 | 9 |
| 3 | 2019-03-04→2024-09-22 | 2024-09-23→2025-05-17 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 1} | 1.13 | inf | 2 |
| 4 | 2019-10-27→2025-05-17 | 2025-05-18→2026-01-09 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 1} | 1.53 | 7.42 | 3 |
| 5 | 2020-06-20→2026-01-09 | 2026-01-10→2026-09-03 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 1} | 1.76 | 0.00 | 0 |