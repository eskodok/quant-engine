## Validasi rsi2_reversion @ SOL/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 16 < 30: belum cukup bukti
- GAGAL: PF OOS 0.68 < 1.15
- GAGAL: PF in-sample 0.98 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.64 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 54 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.74 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.49 < buy&hold -0.23: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 16 trade OOS (18.8/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 25 | 16 | 16 |
| Profit factor | 0.98 | 0.68 | 0.64 |
| Win rate | 65.8% | 56.2% | 56.2% |
| Expectancy (R) | -0.00 | -0.09 | -0.10 |
| Sharpe | -0.02 | -0.49 | -0.57 |
| Max DD | -2.7% | -2.4% | -2.5% |
| CAGR | -0.0% | -0.8% | -0.9% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 54 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.74 (harus < 0.5)
- Buy & hold jendela OOS: return -56.6%, Sharpe -0.23, maxDD -76.2% | strategi: return -1.4%, Sharpe -0.49, maxDD -2.4%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -2.7%, p95 -3.8%
- Parameter terpilih (fold terakhir): {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2021-08-04→2024-11-29 | 2024-11-30→2025-04-06 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 0} | 0.83 | 0.72 | 9 |
| 2 | 2021-12-10→2025-04-06 | 2025-04-07→2025-08-12 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 1.13 | 0.00 | 2 |
| 3 | 2022-04-17→2025-08-12 | 2025-08-13→2025-12-18 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 0.99 | 0.74 | 5 |
| 4 | 2022-08-23→2025-12-18 | 2025-12-19→2026-04-25 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 0.97 | 0.00 | 0 |
| 5 | 2022-12-29→2026-04-25 | 2026-04-26→2026-08-31 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 0.98 | 0.00 | 0 |