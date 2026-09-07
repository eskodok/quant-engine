## Validasi tsmom @ JPFA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 8 < 30: belum cukup bukti
- GAGAL: PBO 0.54 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS 0.29 < buy&hold 0.75: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.06 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 8 trade OOS (25.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 10 | 8 | 8 |
| Profit factor | 1.28 | 1.66 | 1.50 |
| Win rate | 26.8% | 50.0% | 50.0% |
| Expectancy (R) | 0.16 | 0.32 | 0.26 |
| Sharpe | 0.16 | 0.29 | 0.23 |
| Max DD | -16.5% | -17.6% | -18.2% |
| CAGR | 1.0% | 2.9% | 2.1% |

- Deflated Sharpe prob (n_trials=30): 0.06
- Timing vs entry acak: persentil 88 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.54 (harus < 0.5)
- Buy & hold jendela OOS: return +88.6%, Sharpe 0.75, maxDD -39.2% | strategi: return +8.3%, Sharpe 0.29, maxDD -17.6%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -8.9%, p95 -13.2%
- Parameter terpilih (fold terakhir): {'lookback': 120, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'lookback': 120, 'rebalance': 10} | 1.29 | inf | 1 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'lookback': 120, 'rebalance': 10} | 1.44 | inf | 1 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'lookback': 60, 'rebalance': 10} | 1.75 | 0.00 | 3 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'lookback': 120, 'rebalance': 10} | 0.58 | inf | 1 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'lookback': 120, 'rebalance': 10} | 1.36 | 0.52 | 2 |