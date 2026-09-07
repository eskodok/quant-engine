## Validasi tsmom @ PTRO

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 12 < 30: belum cukup bukti
- GAGAL: timing entry tidak lebih baik dari acak (persentil 73 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.79 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS 0.80 < buy&hold 1.52: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.23 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 12 trade OOS (16.7/100 trade)
- PERINGATAN: parameter tidak stabil antar fold (40%)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 17 | 12 | 12 |
| Profit factor | 2.96 | 3.59 | 3.31 |
| Win rate | 38.3% | 50.0% | 50.0% |
| Expectancy (R) | 0.90 | 0.98 | 0.93 |
| Sharpe | 0.64 | 0.80 | 0.76 |
| Max DD | -20.2% | -20.7% | -20.9% |
| CAGR | 10.8% | 14.1% | 13.2% |

- Deflated Sharpe prob (n_trials=30): 0.23
- Timing vs entry acak: persentil 73 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.79 (harus < 0.5)
- Buy & hold jendela OOS: return +1260.8%, Sharpe 1.52, maxDD -73.2% | strategi: return +44.1%, Sharpe 0.80, maxDD -20.7%
- Stabilitas parameter antar fold: 40%
- Monte Carlo max DD: median -7.1%, p95 -11.9%
- Parameter terpilih (fold terakhir): {'lookback': 60, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'lookback': 60, 'rebalance': 10} | 0.36 | 1.47 | 4 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'lookback': 120, 'rebalance': 10} | 3.39 | inf | 2 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'lookback': 250, 'rebalance': 21} | 3.55 | 0.36 | 3 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'lookback': 120, 'rebalance': 10} | 4.22 | 5.61 | 3 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'lookback': 60, 'rebalance': 10} | 3.27 | 0.00 | 0 |