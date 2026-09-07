## Validasi tsmom @ PGAS

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 18 < 30: belum cukup bukti
- GAGAL: PF OOS 0.44 < 1.15
- GAGAL: PF in-sample 0.47 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.34 < 1: edge habis dimakan biaya
- GAGAL: PBO 0.77 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.64 < buy&hold 0.36: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 18 trade OOS (11.1/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 12 | 18 | 18 |
| Profit factor | 0.47 | 0.44 | 0.34 |
| Win rate | 15.4% | 22.2% | 22.2% |
| Expectancy (R) | -0.28 | -0.23 | -0.31 |
| Sharpe | -0.33 | -0.64 | -0.87 |
| Max DD | -23.1% | -20.3% | -23.9% |
| CAGR | -2.8% | -6.5% | -8.7% |

- Deflated Sharpe prob (n_trials=30): 0.00
- Timing vs entry acak: persentil 82 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.77 (harus < 0.5)
- Buy & hold jendela OOS: return +19.7%, Sharpe 0.36, maxDD -44.3% | strategi: return -17.1%, Sharpe -0.64, maxDD -20.3%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -21.5%, p95 -27.4%
- Parameter terpilih (fold terakhir): {'lookback': 120, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'lookback': 60, 'rebalance': 10} | 0.23 | 0.52 | 2 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'lookback': 60, 'rebalance': 10} | 1.41 | 0.25 | 4 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'lookback': 120, 'rebalance': 10} | 0.18 | 0.00 | 4 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'lookback': 120, 'rebalance': 10} | 0.08 | 2.21 | 4 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'lookback': 120, 'rebalance': 10} | 0.45 | 0.00 | 4 |