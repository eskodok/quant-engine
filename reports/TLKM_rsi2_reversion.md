## Validasi rsi2_reversion @ TLKM

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 10 < 30: belum cukup bukti
- GAGAL: PF OOS 0.31 < 1.15
- GAGAL: degradasi IS→OOS 91% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.19 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 35 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: PBO 0.43 agak tinggi
- PERINGATAN: Sharpe OOS -0.89 < buy&hold -0.09: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 10 trade OOS (30.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 25 | 10 | 10 |
| Profit factor | 3.64 | 0.31 | 0.19 |
| Win rate | 63.2% | 40.0% | 40.0% |
| Expectancy (R) | 0.18 | -0.29 | -0.39 |
| Sharpe | 0.54 | -0.89 | -1.15 |
| Max DD | -1.4% | -3.0% | -3.8% |
| CAGR | 0.7% | -1.0% | -1.4% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 35 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.43 (harus < 0.5)
- Buy & hold jendela OOS: return -23.7%, Sharpe -0.09, maxDD -45.6% | strategi: return -2.9%, Sharpe -0.89, maxDD -3.0%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -3.3%, p95 -3.9%
- Parameter terpilih (fold terakhir): {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 1}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 5.64 | 0.00 | 3 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 1} | 2.89 | 0.00 | 0 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 1} | 2.89 | 0.00 | 0 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 1} | 4.04 | 3.65 | 6 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 1} | 2.75 | 0.00 | 1 |