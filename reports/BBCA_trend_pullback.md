## Validasi trend_pullback @ BBCA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: PF OOS 0.69 < 1.15
- GAGAL: degradasi IS→OOS 60% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.49 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 67 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: Sharpe OOS -0.35 < buy&hold -0.21: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 7 trade OOS (42.9/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 18 | 7 | 7 |
| Profit factor | 1.73 | 0.69 | 0.49 |
| Win rate | 42.2% | 28.6% | 28.6% |
| Expectancy (R) | 0.30 | -0.07 | -0.21 |
| Sharpe | 0.40 | -0.35 | -0.68 |
| Max DD | -2.7% | -2.7% | -3.2% |
| CAGR | 0.6% | -0.3% | -0.6% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Timing vs entry acak: persentil 67 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.19 (harus < 0.5)
- Buy & hold jendela OOS: return -23.9%, Sharpe -0.21, maxDD -55.7% | strategi: return -0.8%, Sharpe -0.35, maxDD -2.7%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -2.0%, p95 -2.8%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 2.39 | 0.85 | 6 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 2.0} | 1.84 | 0.00 | 1 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 2.0} | 1.80 | 0.00 | 0 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 1.42 | 0.00 | 0 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-07 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 1.18 | 0.00 | 0 |