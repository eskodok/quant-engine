## Validasi tsmom @ MAPI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 8 < 30: belum cukup bukti
- GAGAL: PF OOS 0.13 < 1.15
- GAGAL: degradasi IS→OOS 92% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.09 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 38 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: PBO 0.40 agak tinggi
- PERINGATAN: Sharpe OOS -0.78 < buy&hold 0.06: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 8 trade OOS (25.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 12 | 8 | 8 |
| Profit factor | 1.58 | 0.13 | 0.09 |
| Win rate | 25.2% | 25.0% | 12.5% |
| Expectancy (R) | 0.33 | -0.44 | -0.50 |
| Sharpe | 0.28 | -0.78 | -0.90 |
| Max DD | -18.0% | -12.8% | -14.6% |
| CAGR | 2.5% | -4.8% | -5.5% |

- Deflated Sharpe prob (n_trials=30): 0.00
- Timing vs entry acak: persentil 38 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.40 (harus < 0.5)
- Buy & hold jendela OOS: return -20.8%, Sharpe 0.06, maxDD -46.0% | strategi: return -12.8%, Sharpe -0.78, maxDD -12.8%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -13.4%, p95 -15.4%
- Parameter terpilih (fold terakhir): {'lookback': 120, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'lookback': 120, 'rebalance': 10} | 1.42 | 0.25 | 5 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'lookback': 120, 'rebalance': 21} | 1.29 | 0.00 | 0 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'lookback': 120, 'rebalance': 10} | 1.69 | 0.00 | 0 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'lookback': 120, 'rebalance': 10} | 2.08 | 0.00 | 1 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'lookback': 120, 'rebalance': 10} | 1.44 | 0.00 | 2 |