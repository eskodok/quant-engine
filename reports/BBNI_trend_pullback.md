## Validasi trend_pullback @ BBNI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: PF OOS 1.04 < 1.15
- GAGAL: PF OOS dengan biaya x2.0 = 0.79 < 1: edge habis dimakan biaya
- GAGAL: PBO 0.74 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 7 trade OOS (42.9/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 20 | 7 | 7 |
| Profit factor | 1.25 | 1.04 | 0.79 |
| Win rate | 33.6% | 28.6% | 28.6% |
| Expectancy (R) | 0.09 | -0.04 | -0.18 |
| Sharpe | 0.22 | 0.03 | -0.20 |
| Max DD | -3.7% | -3.1% | -3.6% |
| CAGR | 0.4% | 0.0% | -0.3% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Timing vs entry acak: persentil 84 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.74 (harus < 0.5)
- Buy & hold jendela OOS: return -18.8%, Sharpe -0.05, maxDD -51.6% | strategi: return +0.1%, Sharpe 0.03, maxDD -3.1%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -2.4%, p95 -3.5%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 1.00 | 2.42 | 4 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 2.0} | 1.26 | 0.00 | 1 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 1.20 | 0.00 | 0 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 2.0} | 1.30 | 0.00 | 1 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 1.48 | 0.00 | 1 |