## Validasi tsmom @ BNB/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 13 < 30: belum cukup bukti
- GAGAL: timing entry tidak lebih baik dari acak (persentil 70 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.93 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS 0.74 < buy&hold 0.85: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.18 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 13 trade OOS (15.4/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 18 | 13 | 13 |
| Profit factor | 2.09 | 2.60 | 2.44 |
| Win rate | 30.5% | 30.8% | 30.8% |
| Expectancy (R) | 0.68 | 0.52 | 0.48 |
| Sharpe | 0.66 | 0.74 | 0.70 |
| Max DD | -27.0% | -26.1% | -26.5% |
| CAGR | 10.2% | 13.2% | 12.4% |

- Deflated Sharpe prob (n_trials=30): 0.18
- Timing vs entry acak: persentil 70 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.93 (harus < 0.5)
- Buy & hold jendela OOS: return +126.0%, Sharpe 0.85, maxDD -58.2% | strategi: return +38.2%, Sharpe 0.74, maxDD -26.1%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -11.4%, p95 -19.4%
- Parameter terpilih (fold terakhir): {'lookback': 60, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2019-06-19→2024-01-25 | 2024-01-26→2024-08-02 | {'lookback': 60, 'rebalance': 21} | 1.69 | 5.04 | 4 |
| 2 | 2019-12-26→2024-08-02 | 2024-08-03→2025-02-08 | {'lookback': 60, 'rebalance': 10} | 2.87 | 0.51 | 3 |
| 3 | 2020-07-03→2025-02-08 | 2025-02-09→2025-08-17 | {'lookback': 60, 'rebalance': 10} | 2.15 | 7.94 | 2 |
| 4 | 2021-01-09→2025-08-17 | 2025-08-18→2026-02-23 | {'lookback': 250, 'rebalance': 21} | 1.88 | 0.00 | 3 |
| 5 | 2021-07-18→2026-02-23 | 2026-02-24→2026-09-01 | {'lookback': 60, 'rebalance': 10} | 1.88 | 0.00 | 1 |