## Validasi rsi2_reversion @ TLKM

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 14 < 30: belum cukup bukti
- GAGAL: PF OOS 0.40 < 1.15
- GAGAL: degradasi IS→OOS 89% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.24 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 40 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: PBO 0.46 agak tinggi
- PERINGATAN: Sharpe OOS -0.77 < buy&hold -0.11: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 14 trade OOS (21.4/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 26 | 14 | 14 |
| Profit factor | 3.83 | 0.40 | 0.24 |
| Win rate | 62.8% | 42.9% | 42.9% |
| Expectancy (R) | 0.18 | -0.21 | -0.30 |
| Sharpe | 0.54 | -0.77 | -1.12 |
| Max DD | -1.4% | -3.1% | -4.1% |
| CAGR | 0.8% | -1.0% | -1.5% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 40 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.46 (harus < 0.5)
- Buy & hold jendela OOS: return -25.3%, Sharpe -0.11, maxDD -45.6% | strategi: return -2.8%, Sharpe -0.77, maxDD -3.1%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -3.4%, p95 -4.2%
- Parameter terpilih (fold terakhir): {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 1}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-25 | 2023-10-26→2024-05-30 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 8.09 | 0.00 | 3 |
| 2 | 2019-03-13→2024-05-30 | 2024-05-31→2024-12-12 | {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 1} | 2.89 | 0.00 | 0 |
| 3 | 2019-09-20→2024-12-12 | 2024-12-13→2025-07-23 | {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 1} | 2.89 | 0.00 | 0 |
| 4 | 2020-04-06→2025-07-23 | 2025-07-24→2026-02-09 | {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 1} | 2.80 | 2.07 | 10 |
| 5 | 2020-11-02→2026-02-09 | 2026-02-10→2026-09-03 | {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 1} | 2.49 | 0.00 | 1 |