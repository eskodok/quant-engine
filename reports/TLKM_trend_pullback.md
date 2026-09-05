## Validasi trend_pullback @ TLKM

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 5 < 30: belum cukup bukti
- GAGAL: PF OOS 0.44 < 1.15
- GAGAL: PF in-sample 0.78 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 43% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.30 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 48 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.69 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.35 < buy&hold -0.11: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 5 trade OOS (60.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 14 | 5 | 5 |
| Profit factor | 0.78 | 0.44 | 0.30 |
| Win rate | 25.3% | 20.0% | 20.0% |
| Expectancy (R) | -0.14 | -0.20 | -0.32 |
| Sharpe | -0.17 | -0.35 | -0.52 |
| Max DD | -2.9% | -2.0% | -2.4% |
| CAGR | -0.3% | -0.4% | -0.6% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Timing vs entry acak: persentil 48 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.69 (harus < 0.5)
- Buy & hold jendela OOS: return -25.3%, Sharpe -0.11, maxDD -45.6% | strategi: return -1.1%, Sharpe -0.35, maxDD -2.0%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -1.7%, p95 -1.9%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-25 | 2023-10-26→2024-05-30 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.51 | 11.75 | 2 |
| 2 | 2019-03-13→2024-05-30 | 2024-05-31→2024-12-12 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.93 | 0.00 | 0 |
| 3 | 2019-09-20→2024-12-12 | 2024-12-13→2025-07-23 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.93 | 0.00 | 0 |
| 4 | 2020-04-06→2025-07-23 | 2025-07-24→2026-02-09 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.92 | 0.00 | 2 |
| 5 | 2020-11-02→2026-02-09 | 2026-02-10→2026-09-03 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.61 | 0.00 | 1 |