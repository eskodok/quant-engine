## Validasi trend_pullback @ ENRG

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 11 < 30: belum cukup bukti
- GAGAL: PF OOS 0.83 < 1.15
- GAGAL: PF in-sample 0.83 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.70 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 31 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.60 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.12 < buy&hold 1.18: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 11 trade OOS (27.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 21 | 11 | 11 |
| Profit factor | 0.83 | 0.83 | 0.70 |
| Win rate | 20.3% | 36.4% | 36.4% |
| Expectancy (R) | -0.06 | -0.06 | -0.11 |
| Sharpe | -0.15 | -0.12 | -0.23 |
| Max DD | -5.3% | -2.7% | -2.8% |
| CAGR | -0.3% | -0.2% | -0.4% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Timing vs entry acak: persentil 31 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.60 (harus < 0.5)
- Buy & hold jendela OOS: return +449.2%, Sharpe 1.18, maxDD -57.1% | strategi: return -0.6%, Sharpe -0.12, maxDD -2.7%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -2.4%, p95 -3.4%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.82 | 0.00 | 0 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.77 | 0.00 | 2 |
| 3 | 2019-09-24→2024-12-16 | 2024-12-17→2025-07-25 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.86 | 0.00 | 1 |
| 4 | 2020-04-08→2025-07-25 | 2025-07-28→2026-02-11 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.73 | 1.93 | 3 |
| 5 | 2020-11-04→2026-02-11 | 2026-02-12→2026-09-04 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 0.97 | 0.28 | 5 |