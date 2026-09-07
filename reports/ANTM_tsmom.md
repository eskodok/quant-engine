## Validasi tsmom @ ANTM

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 15 < 30: belum cukup bukti
- GAGAL: PF OOS 0.68 < 1.15
- GAGAL: PF in-sample 0.78 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.60 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 69 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.99 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.35 < buy&hold 0.68: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 15 trade OOS (13.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 14 | 15 | 15 |
| Profit factor | 0.78 | 0.68 | 0.60 |
| Win rate | 18.7% | 13.3% | 13.3% |
| Expectancy (R) | -0.03 | -0.13 | -0.18 |
| Sharpe | -0.14 | -0.35 | -0.49 |
| Max DD | -25.0% | -15.5% | -16.9% |
| CAGR | -0.9% | -4.0% | -5.3% |

- Deflated Sharpe prob (n_trials=30): 0.00
- Timing vs entry acak: persentil 69 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.99 (harus < 0.5)
- Buy & hold jendela OOS: return +80.9%, Sharpe 0.68, maxDD -46.8% | strategi: return -10.6%, Sharpe -0.35, maxDD -15.5%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -21.9%, p95 -29.1%
- Parameter terpilih (fold terakhir): {'lookback': 120, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'lookback': 60, 'rebalance': 10} | 1.60 | 0.00 | 1 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'lookback': 120, 'rebalance': 10} | 1.06 | 0.00 | 2 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'lookback': 60, 'rebalance': 10} | 0.54 | 1.34 | 6 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'lookback': 60, 'rebalance': 10} | 0.22 | 0.61 | 5 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'lookback': 120, 'rebalance': 10} | 0.51 | 0.00 | 1 |