## Validasi tsmom @ INDF

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 8 < 30: belum cukup bukti
- GAGAL: PF OOS 0.81 < 1.15
- GAGAL: PF in-sample 0.33 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.64 < 1: edge habis dimakan biaya
- PERINGATAN: Sharpe OOS -0.17 < buy&hold 0.21: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 8 trade OOS (25.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 14 | 8 | 8 |
| Profit factor | 0.33 | 0.81 | 0.64 |
| Win rate | 13.1% | 25.0% | 25.0% |
| Expectancy (R) | -0.28 | -0.17 | -0.29 |
| Sharpe | -0.37 | -0.17 | -0.33 |
| Max DD | -24.0% | -17.1% | -20.2% |
| CAGR | -3.5% | -2.2% | -3.9% |

- Deflated Sharpe prob (n_trials=30): 0.01
- Timing vs entry acak: persentil 91 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.21 (harus < 0.5)
- Buy & hold jendela OOS: return +6.3%, Sharpe 0.21, maxDD -30.8% | strategi: return -6.0%, Sharpe -0.17, maxDD -17.1%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -15.7%, p95 -21.0%
- Parameter terpilih (fold terakhir): {'lookback': 120, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'lookback': 60, 'rebalance': 10} | 0.30 | 0.00 | 1 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'lookback': 60, 'rebalance': 10} | 0.00 | inf | 1 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'lookback': 60, 'rebalance': 10} | 0.92 | 0.06 | 3 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'lookback': 120, 'rebalance': 10} | 0.17 | 0.00 | 2 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'lookback': 120, 'rebalance': 10} | 0.27 | 0.00 | 1 |