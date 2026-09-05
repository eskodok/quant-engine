## Validasi tsmom @ KLBF

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 3 < 30: belum cukup bukti
- GAGAL: PF OOS 0.00 < 1.15
- GAGAL: degradasi IS→OOS 100% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.00 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 0 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 3 trade OOS (66.7/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 12 | 3 | 3 |
| Profit factor | 1.81 | 0.00 | 0.00 |
| Win rate | 22.2% | 0.0% | 0.0% |
| Expectancy (R) | 0.18 | -0.29 | -0.37 |
| Sharpe | 0.22 | -0.19 | -0.25 |
| Max DD | -14.1% | -8.0% | -8.9% |
| CAGR | 1.7% | -1.7% | -2.2% |

- Deflated Sharpe prob (n_trials=30): 0.01
- Timing vs entry acak: persentil 0 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.16 (harus < 0.5)
- Buy & hold jendela OOS: return -57.1%, Sharpe -0.67, maxDD -62.2% | strategi: return -4.7%, Sharpe -0.19, maxDD -8.0%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'lookback': 60, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'lookback': 60, 'rebalance': 10} | 1.66 | 0.00 | 0 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'lookback': 60, 'rebalance': 10} | 0.69 | 0.00 | 1 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'lookback': 60, 'rebalance': 10} | 1.24 | 0.00 | 1 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'lookback': 60, 'rebalance': 10} | 1.86 | 0.00 | 1 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'lookback': 60, 'rebalance': 10} | 3.58 | 0.00 | 0 |