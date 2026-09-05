## Validasi tsmom @ BMRI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 6 < 30: belum cukup bukti
- GAGAL: PF OOS 0.00 < 1.15
- GAGAL: degradasi IS→OOS 100% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.00 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 0 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.50 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.50 < buy&hold -0.15: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 6 trade OOS (33.3/100 trade)
- PERINGATAN: parameter tidak stabil antar fold (40%)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 12 | 6 | 6 |
| Profit factor | 1.03 | 0.00 | 0.00 |
| Win rate | 33.1% | 0.0% | 0.0% |
| Expectancy (R) | 0.08 | -0.47 | -0.56 |
| Sharpe | 0.10 | -0.50 | -0.62 |
| Max DD | -20.3% | -19.5% | -21.0% |
| CAGR | 0.5% | -4.4% | -5.4% |

- Deflated Sharpe prob (n_trials=30): 0.00
- Timing vs entry acak: persentil 0 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.50 (harus < 0.5)
- Buy & hold jendela OOS: return -25.5%, Sharpe -0.15, maxDD -50.2% | strategi: return -11.7%, Sharpe -0.50, maxDD -19.5%
- Stabilitas parameter antar fold: 40%
- Monte Carlo max DD: median -12.1%, p95 -12.1%
- Parameter terpilih (fold terakhir): {'lookback': 120, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'lookback': 60, 'rebalance': 10} | 0.76 | 0.00 | 2 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'lookback': 60, 'rebalance': 10} | 0.41 | 0.00 | 1 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'lookback': 120, 'rebalance': 21} | 1.46 | 0.00 | 0 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'lookback': 120, 'rebalance': 10} | 1.20 | 0.00 | 2 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'lookback': 120, 'rebalance': 10} | 1.33 | 0.00 | 1 |