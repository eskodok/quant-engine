## Validasi tsmom @ SOL/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 8 < 30: belum cukup bukti
- GAGAL: PF OOS 0.06 < 1.15
- GAGAL: degradasi IS→OOS 97% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.06 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 4 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: PBO 0.43 agak tinggi
- PERINGATAN: Sharpe OOS -1.21 < buy&hold -0.21: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 8 trade OOS (25.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 15 | 8 | 8 |
| Profit factor | 1.82 | 0.06 | 0.06 |
| Win rate | 23.8% | 12.5% | 12.5% |
| Expectancy (R) | 0.63 | -0.38 | -0.39 |
| Sharpe | 0.63 | -1.21 | -1.26 |
| Max DD | -20.1% | -14.8% | -15.2% |
| CAGR | 8.2% | -8.0% | -8.3% |

- Deflated Sharpe prob (n_trials=30): 0.00
- Timing vs entry acak: persentil 4 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.43 (harus < 0.5)
- Buy & hold jendela OOS: return -55.5%, Sharpe -0.21, maxDD -76.2% | strategi: return -13.5%, Sharpe -1.21, maxDD -14.8%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -14.1%, p95 -15.0%
- Parameter terpilih (fold terakhir): {'lookback': 60, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2021-08-04→2024-12-01 | 2024-12-02→2025-04-08 | {'lookback': 60, 'rebalance': 10} | 1.91 | 0.00 | 3 |
| 2 | 2021-12-10→2025-04-08 | 2025-04-09→2025-08-14 | {'lookback': 250, 'rebalance': 10} | 1.98 | 0.00 | 1 |
| 3 | 2022-04-17→2025-08-14 | 2025-08-15→2025-12-20 | {'lookback': 250, 'rebalance': 10} | 2.49 | 0.37 | 3 |
| 4 | 2022-08-23→2025-12-20 | 2025-12-21→2026-04-27 | {'lookback': 250, 'rebalance': 10} | 1.69 | 0.00 | 0 |
| 5 | 2022-12-29→2026-04-27 | 2026-04-28→2026-09-02 | {'lookback': 60, 'rebalance': 10} | 1.04 | 0.00 | 1 |