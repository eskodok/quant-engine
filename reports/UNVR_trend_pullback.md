## Validasi trend_pullback @ UNVR

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 2 < 30: belum cukup bukti
- GAGAL: PF OOS 0.00 < 1.15
- GAGAL: PF in-sample 0.00 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.00 < 1: edge habis dimakan biaya
- GAGAL: PBO 1.00 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.74 < buy&hold -0.45: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 2 trade OOS (150.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 6 | 2 | 2 |
| Profit factor | 0.00 | 0.00 | 0.00 |
| Win rate | 0.0% | 0.0% | 0.0% |
| Expectancy (R) | -0.48 | -0.70 | -0.78 |
| Sharpe | -0.96 | -0.74 | -0.81 |
| Max DD | -2.8% | -1.7% | -1.8% |
| CAGR | -0.5% | -0.5% | -0.6% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Timing vs entry acak: persentil nan (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 1.00 (harus < 0.5)
- Buy & hold jendela OOS: return -57.7%, Sharpe -0.45, maxDD -74.5% | strategi: return -1.4%, Sharpe -0.74, maxDD -1.7%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.00 | 0.00 | 0 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.00 | 0.00 | 0 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.00 | 0.00 | 0 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.00 | 0.00 | 1 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.00 | 0.00 | 1 |