## Validasi trend_pullback @ PGAS

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 17 < 30: belum cukup bukti
- GAGAL: PF OOS 0.48 < 1.15
- GAGAL: PF in-sample 0.52 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.31 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 37 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.60 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.55 < buy&hold 0.36: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 17 trade OOS (17.6/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 18 | 17 | 17 |
| Profit factor | 0.52 | 0.48 | 0.31 |
| Win rate | 22.3% | 29.4% | 23.5% |
| Expectancy (R) | -0.18 | -0.19 | -0.30 |
| Sharpe | -0.44 | -0.55 | -0.92 |
| Max DD | -5.3% | -5.4% | -6.7% |
| CAGR | -0.6% | -1.1% | -1.9% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Timing vs entry acak: persentil 37 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.60 (harus < 0.5)
- Buy & hold jendela OOS: return +19.7%, Sharpe 0.36, maxDD -44.3% | strategi: return -3.1%, Sharpe -0.55, maxDD -5.4%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -4.1%, p95 -5.4%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.55 | 0.00 | 0 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.55 | 0.07 | 4 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.45 | 0.62 | 5 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.51 | 0.13 | 5 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 0.54 | 2.11 | 3 |