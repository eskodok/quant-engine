## Validasi tsmom @ UNVR

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 1 < 30: belum cukup bukti
- GAGAL: PF OOS 0.00 < 1.15
- GAGAL: PF in-sample 0.07 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 100% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.00 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 0 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: PBO 0.39 agak tinggi
- PERINGATAN: Sharpe OOS -0.60 < buy&hold -0.45: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 1 trade OOS (200.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 10 | 1 | 1 |
| Profit factor | 0.07 | 0.00 | 0.00 |
| Win rate | 9.2% | 0.0% | 0.0% |
| Expectancy (R) | -0.50 | -1.03 | -1.06 |
| Sharpe | -0.76 | -0.60 | -0.62 |
| Max DD | -21.7% | -3.6% | -3.6% |
| CAGR | -4.2% | -1.1% | -1.2% |

- Deflated Sharpe prob (n_trials=30): 0.00
- Timing vs entry acak: persentil 0 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.39 (harus < 0.5)
- Buy & hold jendela OOS: return -57.7%, Sharpe -0.45, maxDD -74.5% | strategi: return -3.1%, Sharpe -0.60, maxDD -3.6%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'lookback': 60, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'lookback': 60, 'rebalance': 10} | 0.04 | 0.00 | 0 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'lookback': 60, 'rebalance': 10} | 0.08 | 0.00 | 0 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'lookback': 120, 'rebalance': 10} | 0.00 | 0.00 | 0 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'lookback': 250, 'rebalance': 10} | 0.00 | 0.00 | 1 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'lookback': 60, 'rebalance': 10} | 0.25 | 0.00 | 0 |