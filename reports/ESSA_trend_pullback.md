## Validasi trend_pullback @ ESSA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 6 < 30: belum cukup bukti
- GAGAL: PF OOS 0.15 < 1.15
- GAGAL: PF in-sample 0.77 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 81% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.09 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 35 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.74 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.77 < buy&hold 0.28: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 6 trade OOS (50.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 17 | 6 | 6 |
| Profit factor | 0.77 | 0.15 | 0.09 |
| Win rate | 16.9% | 16.7% | 16.7% |
| Expectancy (R) | -0.13 | -0.30 | -0.37 |
| Sharpe | -0.21 | -0.77 | -0.93 |
| Max DD | -5.5% | -1.9% | -2.2% |
| CAGR | -0.5% | -0.6% | -0.8% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Timing vs entry acak: persentil 35 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.74 (harus < 0.5)
- Buy & hold jendela OOS: return +3.2%, Sharpe 0.28, maxDD -47.7% | strategi: return -1.8%, Sharpe -0.77, maxDD -1.9%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -1.8%, p95 -2.1%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-30 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0} | 0.79 | 0.00 | 1 |
| 2 | 2019-03-15→2024-05-30 | 2024-05-31→2024-12-11 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0} | 0.78 | 0.00 | 3 |
| 3 | 2019-09-23→2024-12-11 | 2024-12-12→2025-07-21 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0} | 0.67 | 1.91 | 2 |
| 4 | 2020-04-06→2025-07-21 | 2025-07-22→2026-02-04 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0} | 0.75 | 0.00 | 0 |
| 5 | 2020-10-27→2026-02-04 | 2026-02-05→2026-08-31 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0} | 0.85 | 0.00 | 0 |