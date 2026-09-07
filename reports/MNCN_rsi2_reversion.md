## Validasi rsi2_reversion @ MNCN

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 5 < 30: belum cukup bukti
- GAGAL: PF OOS 0.02 < 1.15
- GAGAL: PF in-sample 1.04 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 98% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.00 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 1 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: PBO 0.47 agak tinggi
- PERINGATAN: Sharpe OOS -1.30 < buy&hold -0.60: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 5 trade OOS (60.0/100 trade)
- PERINGATAN: parameter tidak stabil antar fold (40%)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 18 | 5 | 5 |
| Profit factor | 1.04 | 0.02 | 0.00 |
| Win rate | 62.3% | 20.0% | 0.0% |
| Expectancy (R) | -0.03 | -0.66 | -0.72 |
| Sharpe | -0.06 | -1.30 | -1.37 |
| Max DD | -2.2% | -3.3% | -3.6% |
| CAGR | -0.1% | -1.2% | -1.3% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 1 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.47 (harus < 0.5)
- Buy & hold jendela OOS: return -57.7%, Sharpe -0.60, maxDD -59.7% | strategi: return -3.3%, Sharpe -1.30, maxDD -3.3%
- Stabilitas parameter antar fold: 40%
- Monte Carlo max DD: median -3.3%, p95 -3.3%
- Parameter terpilih (fold terakhir): {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 1} | 1.05 | 0.00 | 0 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 0} | 0.94 | 0.00 | 0 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 0} | 1.12 | 0.00 | 0 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 0} | 1.79 | 0.00 | 3 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 0} | 0.32 | 0.06 | 2 |