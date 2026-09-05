## Validasi tsmom @ BTC/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 14 < 30: belum cukup bukti
- GAGAL: PBO 0.76 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: deflated Sharpe prob 0.42 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 14 trade OOS (14.3/100 trade)
- PERINGATAN: parameter tidak stabil antar fold (40%)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 18 | 14 | 14 |
| Profit factor | 3.57 | 3.73 | 3.47 |
| Win rate | 42.3% | 42.9% | 42.9% |
| Expectancy (R) | 1.10 | 0.91 | 0.87 |
| Sharpe | 1.03 | 1.04 | 1.00 |
| Max DD | -19.0% | -13.7% | -14.1% |
| CAGR | 16.2% | 17.3% | 16.6% |

- Deflated Sharpe prob (n_trials=30): 0.42
- Timing vs entry acak: persentil 95 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.76 (harus < 0.5)
- Buy & hold jendela OOS: return +180.1%, Sharpe 0.92, maxDD -53.0% | strategi: return +68.4%, Sharpe 1.04, maxDD -13.7%
- Stabilitas parameter antar fold: 40%
- Monte Carlo max DD: median -8.1%, p95 -14.1%
- Parameter terpilih (fold terakhir): {'lookback': 60, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2017-10-19→2023-05-28 | 2023-05-29→2024-01-21 | {'lookback': 250, 'rebalance': 10} | 3.85 | 2.40 | 5 |
| 2 | 2018-06-21→2024-01-21 | 2024-01-22→2024-09-15 | {'lookback': 120, 'rebalance': 10} | 4.04 | 20.08 | 2 |
| 3 | 2019-02-14→2024-09-15 | 2024-09-16→2025-05-11 | {'lookback': 60, 'rebalance': 10} | 2.70 | 13.33 | 3 |
| 4 | 2019-10-10→2025-05-11 | 2025-05-12→2026-01-04 | {'lookback': 60, 'rebalance': 21} | 3.97 | 1.18 | 3 |
| 5 | 2020-06-04→2026-01-04 | 2026-01-05→2026-08-30 | {'lookback': 60, 'rebalance': 10} | 3.28 | 0.00 | 1 |