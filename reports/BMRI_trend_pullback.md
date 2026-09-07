## Validasi trend_pullback @ BMRI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 9 < 30: belum cukup bukti
- GAGAL: PF OOS 0.24 < 1.15
- GAGAL: PF in-sample 0.69 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 65% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.18 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 19 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.60 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -1.03 < buy&hold -0.11: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 9 trade OOS (33.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 18 | 9 | 9 |
| Profit factor | 0.69 | 0.24 | 0.18 |
| Win rate | 33.6% | 11.1% | 11.1% |
| Expectancy (R) | -0.12 | -0.48 | -0.61 |
| Sharpe | -0.24 | -1.03 | -1.27 |
| Max DD | -4.2% | -4.6% | -5.0% |
| CAGR | -0.4% | -1.5% | -1.8% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Timing vs entry acak: persentil 19 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.60 (harus < 0.5)
- Buy & hold jendela OOS: return -22.5%, Sharpe -0.11, maxDD -50.2% | strategi: return -4.1%, Sharpe -1.03, maxDD -4.6%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -4.3%, p95 -5.4%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.59 | 0.30 | 8 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 0.74 | 0.00 | 0 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 0.84 | 0.00 | 0 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 0.60 | 0.00 | 0 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.68 | 0.00 | 1 |