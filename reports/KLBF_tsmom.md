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
| Profit factor | 1.11 | 0.00 | 0.00 |
| Win rate | 24.0% | 0.0% | 0.0% |
| Expectancy (R) | 0.10 | -0.35 | -0.43 |
| Sharpe | 0.08 | -0.20 | -0.27 |
| Max DD | -15.5% | -8.6% | -9.5% |
| CAGR | 0.3% | -1.8% | -2.2% |

- Deflated Sharpe prob (n_trials=30): 0.01
- Timing vs entry acak: persentil 0 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.23 (harus < 0.5)
- Buy & hold jendela OOS: return -55.8%, Sharpe -0.64, maxDD -62.1% | strategi: return -4.8%, Sharpe -0.20, maxDD -8.6%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'lookback': 60, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'lookback': 60, 'rebalance': 10} | 0.80 | 0.00 | 0 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'lookback': 60, 'rebalance': 10} | 0.84 | 0.00 | 1 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'lookback': 60, 'rebalance': 10} | 0.74 | 0.00 | 1 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'lookback': 60, 'rebalance': 10} | 1.54 | 0.00 | 1 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'lookback': 60, 'rebalance': 10} | 1.63 | 0.00 | 0 |