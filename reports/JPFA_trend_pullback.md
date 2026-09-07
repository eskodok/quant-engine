## Validasi trend_pullback @ JPFA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 18 < 30: belum cukup bukti
- GAGAL: PF OOS 0.77 < 1.15
- GAGAL: PF in-sample 0.52 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.64 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 44 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.94 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.27 < buy&hold 0.75: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 18 trade OOS (16.7/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 12 | 18 | 18 |
| Profit factor | 0.52 | 0.77 | 0.64 |
| Win rate | 25.3% | 33.3% | 27.8% |
| Expectancy (R) | -0.27 | -0.10 | -0.18 |
| Sharpe | -0.34 | -0.27 | -0.50 |
| Max DD | -4.4% | -4.7% | -5.1% |
| CAGR | -0.6% | -0.7% | -1.2% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Timing vs entry acak: persentil 44 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.94 (harus < 0.5)
- Buy & hold jendela OOS: return +88.6%, Sharpe 0.75, maxDD -39.2% | strategi: return -1.8%, Sharpe -0.27, maxDD -4.7%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -4.4%, p95 -6.4%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.29 | 0.00 | 0 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.29 | 1.08 | 8 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 0.80 | 0.82 | 4 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.58 | 0.51 | 2 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.63 | 0.00 | 4 |