## Validasi tsmom @ UNTR

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 10 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.73 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- PERINGATAN: deflated Sharpe prob 0.04 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 10 trade OOS (20.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 15 | 10 | 10 |
| Profit factor | 0.73 | 1.30 | 1.10 |
| Win rate | 16.0% | 30.0% | 20.0% |
| Expectancy (R) | -0.21 | 0.20 | 0.08 |
| Sharpe | -0.15 | 0.21 | 0.11 |
| Max DD | -23.3% | -12.2% | -13.1% |
| CAGR | -1.9% | 2.0% | 0.5% |

- Deflated Sharpe prob (n_trials=30): 0.04
- Timing vs entry acak: persentil 77 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.24 (harus < 0.5)
- Buy & hold jendela OOS: return -3.3%, Sharpe 0.13, maxDD -35.8% | strategi: return +5.6%, Sharpe 0.21, maxDD -12.2%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -15.9%, p95 -21.7%
- Parameter terpilih (fold terakhir): {'lookback': 250, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-25 | 2023-10-26→2024-05-30 | {'lookback': 60, 'rebalance': 10} | 0.87 | 0.00 | 1 |
| 2 | 2019-03-13→2024-05-30 | 2024-05-31→2024-12-12 | {'lookback': 60, 'rebalance': 10} | 0.76 | inf | 2 |
| 3 | 2019-09-20→2024-12-12 | 2024-12-13→2025-07-23 | {'lookback': 250, 'rebalance': 10} | 0.66 | 0.00 | 3 |
| 4 | 2020-04-06→2025-07-23 | 2025-07-24→2026-02-09 | {'lookback': 60, 'rebalance': 10} | 0.43 | 2.16 | 2 |
| 5 | 2020-11-02→2026-02-09 | 2026-02-10→2026-09-03 | {'lookback': 250, 'rebalance': 10} | 0.94 | 0.00 | 2 |