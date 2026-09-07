## Validasi trend_pullback @ MNCN

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 0 < 30: belum cukup bukti
- GAGAL: PF OOS 0.00 < 1.15
- GAGAL: PF in-sample 0.48 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 100% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.00 < 1: edge habis dimakan biaya
- GAGAL: PBO 0.53 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 0 trade OOS (300.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 8 | 0 | 0 |
| Profit factor | 0.48 | 0.00 | 0.00 |
| Win rate | 26.8% | 0.0% | 0.0% |
| Expectancy (R) | -0.23 | 0.00 | 0.00 |
| Sharpe | -0.31 | 0.00 | 0.00 |
| Max DD | -2.7% | 0.0% | 0.0% |
| CAGR | -0.3% | 0.0% | 0.0% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Timing vs entry acak: persentil nan (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.53 (harus < 0.5)
- Buy & hold jendela OOS: return -57.7%, Sharpe -0.60, maxDD -59.7% | strategi: return +0.0%, Sharpe 0.00, maxDD 0.0%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 1.06 | 0.00 | 0 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.23 | 0.00 | 0 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.27 | 0.00 | 0 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.44 | 0.00 | 0 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.38 | 0.00 | 0 |