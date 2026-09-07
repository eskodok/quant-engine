## Validasi tsmom @ ICBP

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 5 < 30: belum cukup bukti
- GAGAL: PF OOS 0.87 < 1.15
- GAGAL: PF in-sample 0.18 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.60 < 1: edge habis dimakan biaya
- PERINGATAN: PBO 0.40 agak tinggi
- PERINGATAN: deflated Sharpe prob 0.02 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 5 trade OOS (40.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 12 | 5 | 5 |
| Profit factor | 0.18 | 0.87 | 0.60 |
| Win rate | 16.7% | 40.0% | 20.0% |
| Expectancy (R) | -0.45 | -0.16 | -0.27 |
| Sharpe | -0.51 | -0.01 | -0.13 |
| Max DD | -23.9% | -11.7% | -12.9% |
| CAGR | -4.5% | -0.5% | -1.4% |

- Deflated Sharpe prob (n_trials=30): 0.02
- Timing vs entry acak: persentil 88 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.40 (harus < 0.5)
- Buy & hold jendela OOS: return -27.8%, Sharpe -0.26, maxDD -53.1% | strategi: return -1.2%, Sharpe -0.01, maxDD -11.7%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -6.1%, p95 -7.1%
- Parameter terpilih (fold terakhir): {'lookback': 120, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-30 | {'lookback': 120, 'rebalance': 10} | 0.18 | 0.01 | 2 |
| 2 | 2019-03-15→2024-05-30 | 2024-05-31→2024-12-11 | {'lookback': 60, 'rebalance': 10} | 0.08 | inf | 1 |
| 3 | 2019-09-23→2024-12-11 | 2024-12-12→2025-07-21 | {'lookback': 120, 'rebalance': 10} | 0.18 | 0.00 | 2 |
| 4 | 2020-04-06→2025-07-21 | 2025-07-22→2026-02-04 | {'lookback': 120, 'rebalance': 21} | 0.28 | 0.00 | 0 |
| 5 | 2020-10-27→2026-02-04 | 2026-02-05→2026-08-31 | {'lookback': 120, 'rebalance': 10} | 0.19 | 0.00 | 0 |