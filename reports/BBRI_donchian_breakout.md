## Validasi donchian_breakout @ BBRI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 2 < 30: belum cukup bukti
- GAGAL: PBO 0.60 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
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
- Probability of Backtest Overfitting (CSCV): 0.60 (harus < 0.5)
- Buy & hold jendela OOS: return -34.5%, Sharpe -0.31, maxDD -59.5% | strategi: return +2.0%, Sharpe 0.63, maxDD -0.9%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'donchian_n': 20, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'donchian_n': 20, 'rr': 1.5} | 0.53 | inf | 2 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'donchian_n': 20, 'rr': 1.5} | 1.22 | 0.00 | 0 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'donchian_n': 20, 'rr': 1.5} | 1.06 | 0.00 | 0 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'donchian_n': 20, 'rr': 1.5} | 1.00 | 0.00 | 0 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'donchian_n': 20, 'rr': 1.5} | 1.19 | 0.00 | 0 |