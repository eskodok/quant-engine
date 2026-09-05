## Validasi tsmom @ SOL/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: PF OOS 0.35 < 1.15
- GAGAL: degradasi IS→OOS 81% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.33 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 29 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: PBO 0.43 agak tinggi
- PERINGATAN: Sharpe OOS -0.59 < buy&hold -0.23: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 7 trade OOS (28.6/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 15 | 7 | 7 |
| Profit factor | 1.83 | 0.35 | 0.33 |
| Win rate | 23.8% | 28.6% | 28.6% |
| Expectancy (R) | 0.64 | -0.19 | -0.20 |
| Sharpe | 0.64 | -0.59 | -0.63 |
| Max DD | -20.1% | -12.2% | -12.5% |
| CAGR | 8.3% | -4.2% | -4.5% |

- Deflated Sharpe prob (n_trials=30): 0.00
- Timing vs entry acak: persentil 29 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.43 (harus < 0.5)
- Buy & hold jendela OOS: return -56.6%, Sharpe -0.23, maxDD -76.2% | strategi: return -7.2%, Sharpe -0.59, maxDD -12.2%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -8.4%, p95 -10.6%
- Parameter terpilih (fold terakhir): {'lookback': 60, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2021-08-04→2024-11-29 | 2024-11-30→2025-04-06 | {'lookback': 60, 'rebalance': 10} | 1.96 | 0.00 | 4 |
| 2 | 2021-12-10→2025-04-06 | 2025-04-07→2025-08-12 | {'lookback': 250, 'rebalance': 10} | 1.98 | 0.00 | 1 |
| 3 | 2022-04-17→2025-08-12 | 2025-08-13→2025-12-18 | {'lookback': 250, 'rebalance': 10} | 2.49 | inf | 1 |
| 4 | 2022-08-23→2025-12-18 | 2025-12-19→2026-04-25 | {'lookback': 250, 'rebalance': 10} | 1.69 | 0.00 | 0 |
| 5 | 2022-12-29→2026-04-25 | 2026-04-26→2026-08-31 | {'lookback': 60, 'rebalance': 10} | 1.04 | inf | 1 |