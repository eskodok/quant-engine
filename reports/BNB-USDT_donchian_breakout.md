## Validasi donchian_breakout @ BNB/USDT

**Verdict: FIX**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 11 < 30: belum cukup bukti
- PERINGATAN: PBO 0.46 agak tinggi
- PERINGATAN: deflated Sharpe prob 0.45 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 11 trade OOS (18.2/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 15 | 11 | 11 |
| Profit factor | 3.51 | 2.95 | 2.80 |
| Win rate | 56.9% | 54.5% | 54.5% |
| Expectancy (R) | 1.01 | 0.95 | 0.90 |
| Sharpe | 1.05 | 1.31 | 1.26 |
| Max DD | -3.0% | -2.5% | -2.6% |
| CAGR | 3.5% | 4.0% | 3.8% |

- Deflated Sharpe prob (n_trials=45): 0.45
- Timing vs entry acak: persentil 91 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.46 (harus < 0.5)
- Buy & hold jendela OOS: return +136.8%, Sharpe 0.89, maxDD -58.2% | strategi: return +10.8%, Sharpe 1.31, maxDD -2.5%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -2.1%, p95 -4.0%
- Parameter terpilih (fold terakhir): {'donchian_n': 20, 'rr': 2.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2019-06-19→2024-01-24 | 2024-01-25→2024-08-01 | {'donchian_n': 40, 'rr': 3.0} | 3.54 | 2.77 | 4 |
| 2 | 2019-12-26→2024-08-01 | 2024-08-02→2025-02-07 | {'donchian_n': 40, 'rr': 3.0} | 4.85 | 2.81 | 2 |
| 3 | 2020-07-03→2025-02-07 | 2025-02-08→2025-08-16 | {'donchian_n': 40, 'rr': 3.0} | 5.08 | 2.73 | 2 |
| 4 | 2021-01-09→2025-08-16 | 2025-08-17→2026-02-22 | {'donchian_n': 40, 'rr': 2.0} | 1.87 | 3.65 | 3 |
| 5 | 2021-07-18→2026-02-22 | 2026-02-23→2026-08-31 | {'donchian_n': 20, 'rr': 2.0} | 2.24 | 0.00 | 0 |