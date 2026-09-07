## Validasi bollinger_reversion @ PTRO

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 10 < 30: belum cukup bukti
- GAGAL: PF OOS 1.03 < 1.15
- GAGAL: PF OOS dengan biaya x2.0 = 0.92 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 47 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.83 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS 0.03 < buy&hold 1.52: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.02 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 10 trade OOS (30.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 14 | 10 | 10 |
| Profit factor | 1.27 | 1.03 | 0.92 |
| Win rate | 60.8% | 60.0% | 60.0% |
| Expectancy (R) | 0.01 | 0.01 | -0.04 |
| Sharpe | 0.15 | 0.03 | -0.05 |
| Max DD | -3.0% | -3.7% | -3.5% |
| CAGR | 0.3% | 0.0% | -0.2% |

- Deflated Sharpe prob (n_trials=40): 0.02
- Timing vs entry acak: persentil 47 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.83 (harus < 0.5)
- Buy & hold jendela OOS: return +1260.8%, Sharpe 1.52, maxDD -73.2% | strategi: return +0.1%, Sharpe 0.03, maxDD -3.7%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -2.8%, p95 -4.6%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.27 | 1.19 | 2 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.95 | 1.70 | 2 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.29 | inf | 3 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.68 | 0.34 | 3 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.15 | 0.00 | 0 |