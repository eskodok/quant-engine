## Validasi tsmom @ BBRI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 5 < 30: belum cukup bukti
- GAGAL: PF OOS 0.11 < 1.15
- GAGAL: PF in-sample 0.44 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 75% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.05 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 25 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: PBO 0.49 agak tinggi
- PERINGATAN: Sharpe OOS -0.45 < buy&hold -0.31: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 5 trade OOS (40.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 13 | 5 | 5 |
| Profit factor | 0.44 | 0.11 | 0.05 |
| Win rate | 23.3% | 20.0% | 20.0% |
| Expectancy (R) | -0.26 | -0.42 | -0.52 |
| Sharpe | -0.23 | -0.45 | -0.58 |
| Max DD | -22.0% | -13.6% | -15.0% |
| CAGR | -2.9% | -2.7% | -3.4% |

- Deflated Sharpe prob (n_trials=30): 0.00
- Timing vs entry acak: persentil 25 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.49 (harus < 0.5)
- Buy & hold jendela OOS: return -34.5%, Sharpe -0.31, maxDD -59.5% | strategi: return -7.2%, Sharpe -0.45, maxDD -13.6%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -7.4%, p95 -8.3%
- Parameter terpilih (fold terakhir): {'lookback': 60, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'lookback': 250, 'rebalance': 10} | 0.24 | 0.53 | 2 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'lookback': 60, 'rebalance': 10} | 0.50 | 0.00 | 2 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'lookback': 250, 'rebalance': 10} | 0.46 | 0.00 | 0 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'lookback': 60, 'rebalance': 10} | 0.48 | 0.00 | 1 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'lookback': 60, 'rebalance': 10} | 0.51 | 0.00 | 0 |