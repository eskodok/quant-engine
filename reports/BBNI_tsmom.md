## Validasi tsmom @ BBNI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 6 < 30: belum cukup bukti
- GAGAL: PF OOS 0.20 < 1.15
- GAGAL: degradasi IS→OOS 86% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.14 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 27 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: PBO 0.33 agak tinggi
- PERINGATAN: Sharpe OOS -0.54 < buy&hold -0.09: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 6 trade OOS (33.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 14 | 6 | 6 |
| Profit factor | 1.45 | 0.20 | 0.14 |
| Win rate | 24.9% | 16.7% | 16.7% |
| Expectancy (R) | 0.23 | -0.38 | -0.47 |
| Sharpe | 0.24 | -0.54 | -0.67 |
| Max DD | -18.0% | -22.4% | -24.4% |
| CAGR | 2.2% | -4.1% | -5.1% |

- Deflated Sharpe prob (n_trials=30): 0.00
- Timing vs entry acak: persentil 27 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.33 (harus < 0.5)
- Buy & hold jendela OOS: return -21.5%, Sharpe -0.09, maxDD -51.6% | strategi: return -11.0%, Sharpe -0.54, maxDD -22.4%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -11.2%, p95 -14.0%
- Parameter terpilih (fold terakhir): {'lookback': 120, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'lookback': 120, 'rebalance': 10} | 0.93 | inf | 1 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'lookback': 120, 'rebalance': 10} | 1.13 | 0.00 | 2 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'lookback': 250, 'rebalance': 10} | 1.92 | 0.00 | 0 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'lookback': 250, 'rebalance': 10} | 2.28 | 0.00 | 2 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'lookback': 120, 'rebalance': 10} | 1.01 | 0.00 | 1 |