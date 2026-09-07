## Validasi tsmom @ ENRG

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 9 < 30: belum cukup bukti
- GAGAL: timing entry tidak lebih baik dari acak (persentil 56 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.90 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS 0.54 < buy&hold 1.18: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.12 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 9 trade OOS (22.2/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 14 | 9 | 9 |
| Profit factor | 2.89 | 2.19 | 2.01 |
| Win rate | 30.1% | 44.4% | 44.4% |
| Expectancy (R) | 0.69 | 0.77 | 0.72 |
| Sharpe | 0.55 | 0.54 | 0.48 |
| Max DD | -18.3% | -12.9% | -13.6% |
| CAGR | 6.8% | 5.7% | 5.0% |

- Deflated Sharpe prob (n_trials=30): 0.12
- Timing vs entry acak: persentil 56 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.90 (harus < 0.5)
- Buy & hold jendela OOS: return +449.2%, Sharpe 1.18, maxDD -57.1% | strategi: return +16.6%, Sharpe 0.54, maxDD -12.9%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -8.3%, p95 -14.0%
- Parameter terpilih (fold terakhir): {'lookback': 60, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'lookback': 60, 'rebalance': 10} | 3.55 | 0.00 | 0 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'lookback': 60, 'rebalance': 10} | 2.35 | 0.08 | 2 |
| 3 | 2019-09-24→2024-12-16 | 2024-12-17→2025-07-25 | {'lookback': 120, 'rebalance': 10} | 2.63 | 1.37 | 3 |
| 4 | 2020-04-08→2025-07-25 | 2025-07-28→2026-02-11 | {'lookback': 120, 'rebalance': 10} | 0.76 | inf | 2 |
| 5 | 2020-11-04→2026-02-11 | 2026-02-12→2026-09-04 | {'lookback': 60, 'rebalance': 10} | 5.16 | 0.00 | 2 |