## Validasi tsmom @ TLKM

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 6 < 30: belum cukup bukti
- GAGAL: PF OOS 0.32 < 1.15
- GAGAL: PF in-sample 0.84 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 61% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.17 < 1: edge habis dimakan biaya
- PERINGATAN: PBO 0.33 agak tinggi
- PERINGATAN: Sharpe OOS -0.14 < buy&hold -0.09: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 6 trade OOS (33.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 11 | 6 | 6 |
| Profit factor | 0.84 | 0.32 | 0.17 |
| Win rate | 21.4% | 33.3% | 33.3% |
| Expectancy (R) | -0.05 | -0.15 | -0.24 |
| Sharpe | -0.04 | -0.14 | -0.24 |
| Max DD | -20.5% | -10.3% | -12.0% |
| CAGR | -0.7% | -1.5% | -2.3% |

- Deflated Sharpe prob (n_trials=30): 0.01
- Timing vs entry acak: persentil 79 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.33 (harus < 0.5)
- Buy & hold jendela OOS: return -23.7%, Sharpe -0.09, maxDD -45.6% | strategi: return -4.1%, Sharpe -0.14, maxDD -10.3%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -5.2%, p95 -6.0%
- Parameter terpilih (fold terakhir): {'lookback': 120, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'lookback': 60, 'rebalance': 10} | 0.77 | 0.00 | 1 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'lookback': 60, 'rebalance': 10} | 0.51 | 0.00 | 0 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'lookback': 60, 'rebalance': 10} | 1.14 | 0.00 | 2 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'lookback': 60, 'rebalance': 10} | 0.65 | inf | 2 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'lookback': 120, 'rebalance': 10} | 1.10 | 0.00 | 1 |