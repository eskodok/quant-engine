## Validasi trend_pullback @ MAPI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 6 < 30: belum cukup bukti
- GAGAL: PF OOS 0.53 < 1.15
- GAGAL: PF in-sample 0.97 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 46% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.42 < 1: edge habis dimakan biaya
- GAGAL: PBO 0.61 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.22 < buy&hold 0.06: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 6 trade OOS (50.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 17 | 6 | 6 |
| Profit factor | 0.97 | 0.53 | 0.42 |
| Win rate | 23.1% | 16.7% | 16.7% |
| Expectancy (R) | -0.01 | -0.20 | -0.28 |
| Sharpe | -0.01 | -0.22 | -0.33 |
| Max DD | -3.5% | -2.3% | -2.5% |
| CAGR | -0.0% | -0.4% | -0.6% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Timing vs entry acak: persentil 81 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.61 (harus < 0.5)
- Buy & hold jendela OOS: return -20.8%, Sharpe 0.06, maxDD -46.0% | strategi: return -1.2%, Sharpe -0.22, maxDD -2.3%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -2.0%, p95 -2.5%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 2.0} | 1.09 | 0.00 | 1 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 0.92 | 0.00 | 1 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 2.0} | 0.92 | 0.00 | 0 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 2.0} | 0.95 | 0.00 | 0 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 0.98 | 0.72 | 4 |