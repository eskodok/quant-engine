## Validasi rsi2_reversion @ ASII

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 2 < 30: belum cukup bukti
- GAGAL: PF OOS 0.70 < 1.15
- GAGAL: PF OOS dengan biaya x2.0 = 0.60 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 54 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.60 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.20 < buy&hold -0.02: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 2 trade OOS (150.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 16 | 2 | 2 |
| Profit factor | 1.15 | 0.70 | 0.60 |
| Win rate | 51.9% | 50.0% | 50.0% |
| Expectancy (R) | 0.02 | -0.15 | -0.24 |
| Sharpe | 0.07 | -0.20 | -0.28 |
| Max DD | -1.7% | -1.0% | -1.0% |
| CAGR | 0.1% | -0.1% | -0.1% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 54 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.60 (harus < 0.5)
- Buy & hold jendela OOS: return -15.3%, Sharpe -0.02, maxDD -41.1% | strategi: return -0.3%, Sharpe -0.20, maxDD -1.0%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 1}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 0.82 | 0.00 | 0 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 0.82 | 0.00 | 0 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 1.30 | 0.00 | 0 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 1.38 | inf | 1 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 1} | 1.43 | 0.00 | 1 |