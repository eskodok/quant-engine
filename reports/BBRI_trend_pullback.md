## Validasi trend_pullback @ BBRI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 5 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.52 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PBO 0.56 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 5 trade OOS (60.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 24 | 5 | 5 |
| Profit factor | 0.52 | 1.49 | 1.11 |
| Win rate | 24.8% | 60.0% | 60.0% |
| Expectancy (R) | -0.19 | 0.58 | 0.30 |
| Sharpe | -0.60 | 0.29 | 0.08 |
| Max DD | -5.8% | -1.2% | -1.3% |
| CAGR | -1.0% | 0.3% | 0.1% |

- Deflated Sharpe prob (n_trials=135): 0.01
- Timing vs entry acak: persentil 82 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.56 (harus < 0.5)
- Buy & hold jendela OOS: return -32.2%, Sharpe -0.27, maxDD -59.5% | strategi: return +0.8%, Sharpe 0.29, maxDD -1.2%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -1.1%, p95 -1.6%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 0.28 | 1.49 | 5 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 0.53 | 0.00 | 0 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 0.62 | 0.00 | 0 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 0.60 | 0.00 | 0 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 0.60 | 0.00 | 0 |