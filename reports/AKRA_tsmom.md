## Validasi tsmom @ AKRA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 14 < 30: belum cukup bukti
- GAGAL: PF OOS 0.00 < 1.15
- GAGAL: degradasi IS→OOS 100% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.00 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 1 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: PBO 0.39 agak tinggi
- PERINGATAN: Sharpe OOS -0.92 < buy&hold 0.20: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 14 trade OOS (14.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 14 | 14 | 14 |
| Profit factor | 1.26 | 0.00 | 0.00 |
| Win rate | 29.9% | 7.1% | 0.0% |
| Expectancy (R) | 0.22 | -0.35 | -0.42 |
| Sharpe | 0.16 | -0.92 | -1.11 |
| Max DD | -15.3% | -29.5% | -32.5% |
| CAGR | 1.2% | -8.2% | -9.9% |

- Deflated Sharpe prob (n_trials=30): 0.00
- Timing vs entry acak: persentil 1 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.39 (harus < 0.5)
- Buy & hold jendela OOS: return +0.7%, Sharpe 0.20, maxDD -51.4% | strategi: return -21.1%, Sharpe -0.92, maxDD -29.5%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -22.6%, p95 -22.7%
- Parameter terpilih (fold terakhir): {'lookback': 60, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'lookback': 60, 'rebalance': 10} | 1.45 | 0.05 | 2 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'lookback': 120, 'rebalance': 10} | 1.20 | 0.00 | 2 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'lookback': 60, 'rebalance': 10} | 1.14 | 0.00 | 1 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'lookback': 60, 'rebalance': 10} | 1.34 | 0.00 | 6 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-07 | {'lookback': 60, 'rebalance': 10} | 1.13 | 0.00 | 3 |