## Validasi tsmom @ TLKM

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 5 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.72 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- PERINGATAN: deflated Sharpe prob 0.03 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 5 trade OOS (40.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 12 | 5 | 5 |
| Profit factor | 0.72 | 1.58 | 1.09 |
| Win rate | 13.2% | 40.0% | 40.0% |
| Expectancy (R) | -0.04 | 0.11 | 0.01 |
| Sharpe | -0.11 | 0.14 | 0.06 |
| Max DD | -21.1% | -10.3% | -11.5% |
| CAGR | -1.4% | 0.9% | 0.1% |

- Deflated Sharpe prob (n_trials=30): 0.03
- Timing vs entry acak: persentil 100 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.09 (harus < 0.5)
- Buy & hold jendela OOS: return -25.3%, Sharpe -0.11, maxDD -45.6% | strategi: return +2.6%, Sharpe 0.14, maxDD -10.3%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -3.4%, p95 -5.0%
- Parameter terpilih (fold terakhir): {'lookback': 60, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-25 | 2023-10-26→2024-05-30 | {'lookback': 60, 'rebalance': 10} | 0.48 | 0.00 | 1 |
| 2 | 2019-03-13→2024-05-30 | 2024-05-31→2024-12-12 | {'lookback': 60, 'rebalance': 10} | 1.04 | 0.00 | 0 |
| 3 | 2019-09-20→2024-12-12 | 2024-12-13→2025-07-23 | {'lookback': 60, 'rebalance': 10} | 0.61 | 0.00 | 2 |
| 4 | 2020-04-06→2025-07-23 | 2025-07-24→2026-02-09 | {'lookback': 60, 'rebalance': 10} | 0.45 | inf | 2 |
| 5 | 2020-11-02→2026-02-09 | 2026-02-10→2026-09-03 | {'lookback': 60, 'rebalance': 10} | 1.03 | 0.00 | 0 |