## Validasi tsmom @ ETH/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 14 < 30: belum cukup bukti
- GAGAL: degradasi IS→OOS 58% > 40%: indikasi overfit
- GAGAL: PBO 0.76 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS 0.44 < buy&hold 0.47: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.10 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 14 trade OOS (14.3/100 trade)
- PERINGATAN: parameter tidak stabil antar fold (40%)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 17 | 14 | 14 |
| Profit factor | 3.98 | 1.67 | 1.60 |
| Win rate | 38.2% | 35.7% | 35.7% |
| Expectancy (R) | 1.15 | 0.33 | 0.30 |
| Sharpe | 0.99 | 0.44 | 0.41 |
| Max DD | -18.2% | -31.3% | -31.7% |
| CAGR | 16.3% | 5.6% | 5.1% |

- Deflated Sharpe prob (n_trials=30): 0.10
- Timing vs entry acak: persentil 84 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.76 (harus < 0.5)
- Buy & hold jendela OOS: return +36.8%, Sharpe 0.47, maxDD -67.5% | strategi: return +19.2%, Sharpe 0.44, maxDD -31.3%
- Stabilitas parameter antar fold: 40%
- Monte Carlo max DD: median -14.3%, p95 -22.5%
- Parameter terpilih (fold terakhir): {'lookback': 60, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2017-11-09→2023-06-06 | 2023-06-07→2024-01-29 | {'lookback': 120, 'rebalance': 10} | 3.06 | 1.52 | 3 |
| 2 | 2018-07-10→2024-01-29 | 2024-01-30→2024-09-22 | {'lookback': 60, 'rebalance': 21} | 5.04 | 0.85 | 4 |
| 3 | 2019-03-04→2024-09-22 | 2024-09-23→2025-05-17 | {'lookback': 120, 'rebalance': 10} | 3.85 | 0.00 | 2 |
| 4 | 2019-10-27→2025-05-17 | 2025-05-18→2026-01-09 | {'lookback': 60, 'rebalance': 10} | 5.06 | 4.30 | 4 |
| 5 | 2020-06-20→2026-01-09 | 2026-01-10→2026-09-03 | {'lookback': 60, 'rebalance': 10} | 2.90 | inf | 1 |