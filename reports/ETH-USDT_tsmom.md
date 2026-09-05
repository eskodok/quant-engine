## Validasi tsmom @ ETH/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 14 < 30: belum cukup bukti
- GAGAL: degradasi IS→OOS 64% > 40%: indikasi overfit
- GAGAL: timing entry tidak lebih baik dari acak (persentil 57 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.84 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS 0.27 < buy&hold 0.43: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.06 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 14 trade OOS (14.3/100 trade)
- PERINGATAN: parameter tidak stabil antar fold (40%)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 17 | 14 | 14 |
| Profit factor | 3.95 | 1.41 | 1.35 |
| Win rate | 38.2% | 28.6% | 28.6% |
| Expectancy (R) | 1.14 | 0.15 | 0.12 |
| Sharpe | 0.98 | 0.27 | 0.24 |
| Max DD | -18.2% | -30.5% | -31.1% |
| CAGR | 16.2% | 3.0% | 2.6% |

- Deflated Sharpe prob (n_trials=30): 0.06
- Timing vs entry acak: persentil 57 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.84 (harus < 0.5)
- Buy & hold jendela OOS: return +26.9%, Sharpe 0.43, maxDD -67.5% | strategi: return +10.2%, Sharpe 0.27, maxDD -30.5%
- Stabilitas parameter antar fold: 40%
- Monte Carlo max DD: median -13.7%, p95 -21.2%
- Parameter terpilih (fold terakhir): {'lookback': 60, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2017-11-09→2023-06-05 | 2023-06-06→2024-01-28 | {'lookback': 120, 'rebalance': 10} | 3.01 | 1.14 | 3 |
| 2 | 2018-07-10→2024-01-28 | 2024-01-29→2024-09-21 | {'lookback': 60, 'rebalance': 21} | 4.93 | 1.08 | 4 |
| 3 | 2019-03-04→2024-09-21 | 2024-09-22→2025-05-16 | {'lookback': 120, 'rebalance': 10} | 3.85 | 0.00 | 3 |
| 4 | 2019-10-27→2025-05-16 | 2025-05-17→2026-01-08 | {'lookback': 60, 'rebalance': 10} | 5.06 | 11.49 | 3 |
| 5 | 2020-06-20→2026-01-08 | 2026-01-09→2026-09-02 | {'lookback': 60, 'rebalance': 10} | 2.90 | 0.00 | 1 |