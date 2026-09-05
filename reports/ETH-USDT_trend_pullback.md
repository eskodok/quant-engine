## Validasi trend_pullback @ ETH/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 16 < 30: belum cukup bukti
- GAGAL: PF OOS 0.64 < 1.15
- GAGAL: degradasi IS→OOS 68% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.59 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 19 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.87 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.28 < buy&hold 0.43: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 16 trade OOS (18.8/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 28 | 16 | 16 |
| Profit factor | 2.02 | 0.64 | 0.59 |
| Win rate | 35.5% | 18.8% | 18.8% |
| Expectancy (R) | 0.34 | -0.16 | -0.18 |
| Sharpe | 0.64 | -0.28 | -0.34 |
| Max DD | -5.4% | -5.5% | -5.7% |
| CAGR | 1.7% | -0.8% | -0.9% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Timing vs entry acak: persentil 19 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.87 (harus < 0.5)
- Buy & hold jendela OOS: return +26.9%, Sharpe 0.43, maxDD -67.5% | strategi: return -2.5%, Sharpe -0.28, maxDD -5.5%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -4.5%, p95 -6.1%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 25.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2017-11-09→2023-06-05 | 2023-06-06→2024-01-28 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 2.32 | 13.89 | 3 |
| 2 | 2018-07-10→2024-01-28 | 2024-01-29→2024-09-21 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0} | 2.93 | 0.00 | 6 |
| 3 | 2019-03-04→2024-09-21 | 2024-09-22→2025-05-16 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 1.73 | 0.00 | 4 |
| 4 | 2019-10-27→2025-05-16 | 2025-05-17→2026-01-08 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 1.65 | 0.90 | 3 |
| 5 | 2020-06-20→2026-01-08 | 2026-01-09→2026-09-02 | {'rsi_pb': 40.0, 'adx_min': 25.0, 'rr': 1.5} | 1.46 | 0.00 | 0 |