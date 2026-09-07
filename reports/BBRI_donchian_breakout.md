## Validasi donchian_breakout @ BBRI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 2 < 30: belum cukup bukti
- GAGAL: PF in-sample 1.00 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PBO 0.66 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: deflated Sharpe prob 0.10 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 2 trade OOS (100.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 11 | 2 | 2 |
| Profit factor | 1.00 | inf | inf |
| Win rate | 51.4% | 100.0% | 100.0% |
| Expectancy (R) | 0.01 | 1.00 | 0.84 |
| Sharpe | -0.02 | 0.63 | 0.56 |
| Max DD | -4.7% | -0.9% | -0.9% |
| CAGR | -0.1% | 0.7% | 0.6% |

- Deflated Sharpe prob (n_trials=45): 0.10
- Timing vs entry acak: persentil 98 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.66 (harus < 0.5)
- Buy & hold jendela OOS: return -32.2%, Sharpe -0.27, maxDD -59.5% | strategi: return +2.0%, Sharpe 0.63, maxDD -0.9%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'donchian_n': 20, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'donchian_n': 20, 'rr': 1.5} | 0.53 | inf | 2 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'donchian_n': 20, 'rr': 1.5} | 1.22 | 0.00 | 0 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'donchian_n': 20, 'rr': 1.5} | 1.06 | 0.00 | 0 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'donchian_n': 20, 'rr': 1.5} | 1.00 | 0.00 | 0 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'donchian_n': 20, 'rr': 1.5} | 1.19 | 0.00 | 0 |