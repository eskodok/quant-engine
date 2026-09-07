## Validasi tsmom @ BUMI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 9 < 30: belum cukup bukti
- GAGAL: timing entry tidak lebih baik dari acak (persentil 43 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: PBO 0.37 agak tinggi
- PERINGATAN: Sharpe OOS 0.13 < buy&hold 0.65: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.03 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 9 trade OOS (22.2/100 trade)
- PERINGATAN: parameter tidak stabil antar fold (40%)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 13 | 9 | 9 |
| Profit factor | 1.72 | 1.27 | 1.14 |
| Win rate | 20.9% | 22.2% | 22.2% |
| Expectancy (R) | 0.34 | 0.23 | 0.19 |
| Sharpe | 0.34 | 0.13 | 0.07 |
| Max DD | -19.0% | -14.5% | -14.9% |
| CAGR | 3.4% | 0.8% | 0.2% |

- Deflated Sharpe prob (n_trials=30): 0.03
- Timing vs entry acak: persentil 43 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.37 (harus < 0.5)
- Buy & hold jendela OOS: return +82.6%, Sharpe 0.65, maxDD -72.0% | strategi: return +2.1%, Sharpe 0.13, maxDD -14.5%
- Stabilitas parameter antar fold: 40%
- Monte Carlo max DD: median -11.1%, p95 -14.6%
- Parameter terpilih (fold terakhir): {'lookback': 120, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'lookback': 60, 'rebalance': 10} | 1.47 | 0.00 | 0 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'lookback': 250, 'rebalance': 10} | 1.20 | 0.00 | 1 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'lookback': 60, 'rebalance': 10} | 2.43 | 0.00 | 2 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'lookback': 120, 'rebalance': 10} | 1.05 | 20.99 | 3 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'lookback': 120, 'rebalance': 10} | 2.47 | 0.00 | 3 |