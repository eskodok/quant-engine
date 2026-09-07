## Validasi trend_pullback @ BUMI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 11 < 30: belum cukup bukti
- GAGAL: PF OOS 0.32 < 1.15
- GAGAL: PF in-sample 0.34 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.26 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 9 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.56 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.75 < buy&hold 0.65: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 11 trade OOS (27.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 9 | 11 | 11 |
| Profit factor | 0.34 | 0.32 | 0.26 |
| Win rate | 20.6% | 18.2% | 18.2% |
| Expectancy (R) | -0.29 | -0.24 | -0.28 |
| Sharpe | -0.60 | -0.75 | -0.90 |
| Max DD | -4.2% | -3.5% | -3.8% |
| CAGR | -0.6% | -0.9% | -1.1% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Timing vs entry acak: persentil 9 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.56 (harus < 0.5)
- Buy & hold jendela OOS: return +82.6%, Sharpe 0.65, maxDD -72.0% | strategi: return -2.6%, Sharpe -0.75, maxDD -3.5%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -3.1%, p95 -3.8%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.57 | 0.00 | 0 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.57 | 0.00 | 2 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.37 | 0.00 | 3 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.01 | 1.11 | 2 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.20 | 0.08 | 4 |