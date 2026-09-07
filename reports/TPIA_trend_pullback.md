## Validasi trend_pullback @ TPIA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: PBO 0.71 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: deflated Sharpe prob 0.03 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 7 trade OOS (42.9/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 17 | 7 | 7 |
| Profit factor | 1.63 | 2.69 | 2.04 |
| Win rate | 30.6% | 42.9% | 42.9% |
| Expectancy (R) | 0.18 | 0.30 | 0.21 |
| Sharpe | 0.26 | 0.50 | 0.38 |
| Max DD | -4.4% | -2.0% | -2.2% |
| CAGR | 0.6% | 0.7% | 0.5% |

- Deflated Sharpe prob (n_trials=135): 0.03
- Timing vs entry acak: persentil 89 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.71 (harus < 0.5)
- Buy & hold jendela OOS: return -30.0%, Sharpe 0.22, maxDD -87.7% | strategi: return +1.9%, Sharpe 0.50, maxDD -2.0%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -0.7%, p95 -1.1%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 0.65 | 6.81 | 3 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0} | 1.60 | 2.57 | 3 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0} | 2.43 | 0.00 | 1 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0} | 1.73 | 0.00 | 0 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-07 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0} | 1.77 | 0.00 | 0 |