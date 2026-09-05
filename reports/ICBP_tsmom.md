## Validasi tsmom @ ICBP

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 5 < 30: belum cukup bukti
- GAGAL: PF OOS 0.55 < 1.15
- GAGAL: PF in-sample 0.26 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.41 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 5 trade OOS (40.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 12 | 5 | 5 |
| Profit factor | 0.26 | 0.55 | 0.41 |
| Win rate | 20.3% | 20.0% | 20.0% |
| Expectancy (R) | -0.37 | -0.40 | -0.50 |
| Sharpe | -0.42 | -0.18 | -0.29 |
| Max DD | -21.9% | -11.6% | -12.9% |
| CAGR | -3.7% | -2.0% | -2.9% |

- Deflated Sharpe prob (n_trials=30): 0.01
- Timing vs entry acak: persentil 90 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.17 (harus < 0.5)
- Buy & hold jendela OOS: return -29.4%, Sharpe -0.29, maxDD -53.1% | strategi: return -5.4%, Sharpe -0.18, maxDD -11.6%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -9.3%, p95 -11.1%
- Parameter terpilih (fold terakhir): {'lookback': 120, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'lookback': 120, 'rebalance': 10} | 0.23 | 0.00 | 2 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'lookback': 60, 'rebalance': 10} | 0.10 | inf | 1 |
| 3 | 2019-09-20→2024-12-11 | 2024-12-12→2025-07-22 | {'lookback': 120, 'rebalance': 10} | 0.40 | 0.00 | 2 |
| 4 | 2020-04-06→2025-07-22 | 2025-07-23→2026-02-06 | {'lookback': 120, 'rebalance': 21} | 0.28 | 0.00 | 0 |
| 5 | 2020-11-02→2026-02-06 | 2026-02-09→2026-09-03 | {'lookback': 120, 'rebalance': 10} | 0.31 | 0.00 | 0 |