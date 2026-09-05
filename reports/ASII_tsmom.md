## Validasi tsmom @ ASII

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.30 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: timing entry tidak lebih baik dari acak (persentil 62 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.79 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: deflated Sharpe prob 0.04 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 7 trade OOS (28.6/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 11 | 7 | 7 |
| Profit factor | 0.30 | 1.23 | 1.08 |
| Win rate | 20.5% | 14.3% | 14.3% |
| Expectancy (R) | -0.34 | 0.42 | 0.29 |
| Sharpe | -0.41 | 0.17 | 0.07 |
| Max DD | -23.4% | -10.6% | -11.0% |
| CAGR | -3.4% | 1.2% | 0.2% |

- Deflated Sharpe prob (n_trials=30): 0.04
- Timing vs entry acak: persentil 62 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.79 (harus < 0.5)
- Buy & hold jendela OOS: return -11.8%, Sharpe 0.03, maxDD -41.1% | strategi: return +3.3%, Sharpe 0.17, maxDD -10.6%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -15.2%, p95 -19.7%
- Parameter terpilih (fold terakhir): {'lookback': 60, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-25 | 2023-10-26→2024-05-30 | {'lookback': 60, 'rebalance': 10} | 0.16 | 0.00 | 0 |
| 2 | 2019-03-13→2024-05-30 | 2024-05-31→2024-12-12 | {'lookback': 60, 'rebalance': 10} | 0.40 | 0.00 | 4 |
| 3 | 2019-09-20→2024-12-12 | 2024-12-13→2025-07-23 | {'lookback': 60, 'rebalance': 10} | 0.23 | 0.00 | 0 |
| 4 | 2020-04-06→2025-07-23 | 2025-07-24→2026-02-09 | {'lookback': 60, 'rebalance': 10} | 0.13 | 2.52 | 2 |
| 5 | 2020-11-02→2026-02-09 | 2026-02-10→2026-09-03 | {'lookback': 60, 'rebalance': 10} | 0.56 | 0.00 | 1 |