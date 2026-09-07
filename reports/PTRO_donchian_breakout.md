## Validasi donchian_breakout @ PTRO

**Verdict: FIX**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 14 < 30: belum cukup bukti
- PERINGATAN: Sharpe OOS 1.38 < buy&hold 1.52: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.52 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 14 trade OOS (14.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 17 | 14 | 14 |
| Profit factor | 2.31 | 3.79 | 3.47 |
| Win rate | 45.8% | 64.3% | 64.3% |
| Expectancy (R) | 0.55 | 1.00 | 0.92 |
| Sharpe | 0.66 | 1.38 | 1.31 |
| Max DD | -3.4% | -3.9% | -3.9% |
| CAGR | 1.9% | 4.9% | 4.5% |

- Deflated Sharpe prob (n_trials=45): 0.52
- Timing vs entry acak: persentil 95 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.00 (harus < 0.5)
- Buy & hold jendela OOS: return +1260.8%, Sharpe 1.52, maxDD -73.2% | strategi: return +14.2%, Sharpe 1.38, maxDD -3.9%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -2.2%, p95 -3.6%
- Parameter terpilih (fold terakhir): {'donchian_n': 20, 'rr': 3.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'donchian_n': 40, 'rr': 1.5} | 0.64 | 1.90 | 3 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'donchian_n': 40, 'rr': 3.0} | 1.95 | inf | 3 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'donchian_n': 20, 'rr': 3.0} | 2.62 | 0.95 | 4 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'donchian_n': 20, 'rr': 3.0} | 2.69 | 8.58 | 4 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'donchian_n': 20, 'rr': 3.0} | 3.64 | 0.00 | 0 |