## Validasi trend_pullback @ SCMA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 8 < 30: belum cukup bukti
- GAGAL: PF in-sample 1.08 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PBO 0.90 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: deflated Sharpe prob 0.11 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 8 trade OOS (37.5/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 7 | 8 | 8 |
| Profit factor | 1.08 | 3.86 | 3.23 |
| Win rate | 20.4% | 50.0% | 50.0% |
| Expectancy (R) | -0.18 | 0.52 | 0.46 |
| Sharpe | -0.31 | 0.98 | 0.89 |
| Max DD | -2.8% | -1.2% | -1.3% |
| CAGR | -0.3% | 1.5% | 1.3% |

- Deflated Sharpe prob (n_trials=135): 0.11
- Timing vs entry acak: persentil 97 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.90 (harus < 0.5)
- Buy & hold jendela OOS: return +37.8%, Sharpe 0.48, maxDD -61.1% | strategi: return +4.2%, Sharpe 0.98, maxDD -1.2%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -0.9%, p95 -1.4%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.30 | 0.00 | 0 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.24 | 0.00 | 0 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.21 | 1.69 | 4 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.80 | 9.87 | 4 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 3.86 | 0.00 | 0 |