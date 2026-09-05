## Validasi donchian_breakout @ BMRI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 5 < 30: belum cukup bukti
- PERINGATAN: deflated Sharpe prob 0.06 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 5 trade OOS (40.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 16 | 5 | 5 |
| Profit factor | 1.57 | 1.83 | 1.45 |
| Win rate | 41.4% | 60.0% | 60.0% |
| Expectancy (R) | 0.01 | 0.37 | 0.22 |
| Sharpe | 0.27 | 0.38 | 0.23 |
| Max DD | -3.9% | -2.3% | -2.5% |
| CAGR | 0.6% | 0.6% | 0.4% |

- Deflated Sharpe prob (n_trials=45): 0.06
- Timing vs entry acak: persentil 93 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.10 (harus < 0.5)
- Buy & hold jendela OOS: return -25.5%, Sharpe -0.15, maxDD -50.2% | strategi: return +1.8%, Sharpe 0.38, maxDD -2.3%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -1.1%, p95 -2.2%
- Parameter terpilih (fold terakhir): {'donchian_n': 40, 'rr': 2.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'donchian_n': 40, 'rr': 2.0} | 0.82 | inf | 2 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'donchian_n': 20, 'rr': 1.5} | 0.96 | 0.91 | 2 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'donchian_n': 55, 'rr': 2.0} | 2.01 | 0.00 | 0 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'donchian_n': 40, 'rr': 2.0} | 2.00 | 0.00 | 0 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'donchian_n': 40, 'rr': 2.0} | 2.05 | 0.00 | 1 |