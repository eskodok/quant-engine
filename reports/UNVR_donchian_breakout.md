## Validasi donchian_breakout @ UNVR

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 3 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.04 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PBO 1.00 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: deflated Sharpe prob 0.04 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 3 trade OOS (66.7/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 4 | 3 | 3 |
| Profit factor | 0.04 | 2.54 | 2.23 |
| Win rate | 3.3% | 66.7% | 66.7% |
| Expectancy (R) | -1.10 | 0.57 | 0.48 |
| Sharpe | -0.86 | 0.43 | 0.37 |
| Max DD | -4.7% | -1.1% | -1.1% |
| CAGR | -0.9% | 0.6% | 0.5% |

- Deflated Sharpe prob (n_trials=45): 0.04
- Timing vs entry acak: persentil 89 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 1.00 (harus < 0.5)
- Buy & hold jendela OOS: return -57.7%, Sharpe -0.45, maxDD -74.5% | strategi: return +1.7%, Sharpe 0.43, maxDD -1.1%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'donchian_n': 20, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'donchian_n': 20, 'rr': 1.5} | 0.00 | 0.00 | 0 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'donchian_n': 20, 'rr': 1.5} | 0.00 | 0.00 | 0 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'donchian_n': 20, 'rr': 1.5} | 0.00 | 0.00 | 0 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'donchian_n': 20, 'rr': 1.5} | 0.00 | 2.54 | 3 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'donchian_n': 20, 'rr': 1.5} | 0.21 | 0.00 | 0 |