## Validasi trend_pullback @ TLKM

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 4 < 30: belum cukup bukti
- GAGAL: PF OOS 0.49 < 1.15
- GAGAL: PF in-sample 0.80 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.34 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 49 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.71 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.30 < buy&hold -0.09: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 4 trade OOS (75.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 14 | 4 | 4 |
| Profit factor | 0.80 | 0.49 | 0.34 |
| Win rate | 25.7% | 25.0% | 25.0% |
| Expectancy (R) | -0.14 | -0.21 | -0.34 |
| Sharpe | -0.16 | -0.30 | -0.45 |
| Max DD | -2.9% | -1.8% | -2.2% |
| CAGR | -0.3% | -0.3% | -0.5% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Timing vs entry acak: persentil 49 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.71 (harus < 0.5)
- Buy & hold jendela OOS: return -23.7%, Sharpe -0.09, maxDD -45.6% | strategi: return -0.9%, Sharpe -0.30, maxDD -1.8%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.51 | 11.75 | 2 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.93 | 0.00 | 0 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.93 | 0.00 | 0 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 1.01 | 0.00 | 2 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.61 | 0.00 | 0 |