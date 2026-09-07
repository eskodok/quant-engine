## Validasi bollinger_reversion @ BUMI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 8 < 30: belum cukup bukti
- GAGAL: PF OOS 0.67 < 1.15
- GAGAL: PF OOS dengan biaya x2.0 = 0.59 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 36 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.66 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.28 < buy&hold 0.65: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 8 trade OOS (37.5/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 10 | 8 | 8 |
| Profit factor | 1.10 | 0.67 | 0.59 |
| Win rate | 65.0% | 50.0% | 50.0% |
| Expectancy (R) | 0.04 | -0.18 | -0.23 |
| Sharpe | 0.06 | -0.28 | -0.37 |
| Max DD | -1.9% | -3.0% | -3.1% |
| CAGR | 0.1% | -0.5% | -0.7% |

- Deflated Sharpe prob (n_trials=40): 0.00
- Timing vs entry acak: persentil 36 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.66 (harus < 0.5)
- Buy & hold jendela OOS: return +82.6%, Sharpe 0.65, maxDD -72.0% | strategi: return -1.4%, Sharpe -0.28, maxDD -3.0%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -2.9%, p95 -4.2%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.91 | 0.00 | 0 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.91 | inf | 1 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.25 | 1.06 | 3 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.36 | 0.53 | 2 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.08 | 0.00 | 2 |