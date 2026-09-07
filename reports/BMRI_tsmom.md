## Validasi tsmom @ BMRI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 6 < 30: belum cukup bukti
- GAGAL: PF OOS 0.58 < 1.15
- GAGAL: degradasi IS→OOS 54% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.44 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 69 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: Sharpe OOS -0.14 < buy&hold -0.11: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 6 trade OOS (33.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 12 | 6 | 6 |
| Profit factor | 1.24 | 0.58 | 0.44 |
| Win rate | 39.8% | 16.7% | 16.7% |
| Expectancy (R) | 0.08 | -0.22 | -0.31 |
| Sharpe | 0.09 | -0.14 | -0.23 |
| Max DD | -18.1% | -21.6% | -23.3% |
| CAGR | 0.4% | -1.7% | -2.6% |

- Deflated Sharpe prob (n_trials=30): 0.01
- Timing vs entry acak: persentil 69 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.24 (harus < 0.5)
- Buy & hold jendela OOS: return -22.5%, Sharpe -0.11, maxDD -50.2% | strategi: return -4.7%, Sharpe -0.14, maxDD -21.6%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -9.0%, p95 -10.7%
- Parameter terpilih (fold terakhir): {'lookback': 120, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'lookback': 120, 'rebalance': 10} | 1.08 | 5.42 | 2 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'lookback': 60, 'rebalance': 10} | 0.69 | 0.00 | 1 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'lookback': 60, 'rebalance': 10} | 0.80 | 0.00 | 0 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'lookback': 60, 'rebalance': 10} | 2.37 | 0.00 | 2 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'lookback': 120, 'rebalance': 10} | 1.25 | 0.00 | 1 |