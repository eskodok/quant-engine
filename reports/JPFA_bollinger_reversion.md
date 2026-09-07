## Validasi bollinger_reversion @ JPFA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 9 < 30: belum cukup bukti
- GAGAL: PF OOS 0.98 < 1.15
- GAGAL: PF OOS dengan biaya x2.0 = 0.76 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 58 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.70 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.01 < buy&hold 0.75: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 9 trade OOS (33.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 8 | 9 | 9 |
| Profit factor | 1.36 | 0.98 | 0.76 |
| Win rate | 60.9% | 66.7% | 66.7% |
| Expectancy (R) | 0.10 | -0.01 | -0.09 |
| Sharpe | 0.13 | -0.01 | -0.18 |
| Max DD | -2.3% | -3.4% | -3.7% |
| CAGR | 0.2% | -0.0% | -0.3% |

- Deflated Sharpe prob (n_trials=40): 0.01
- Timing vs entry acak: persentil 58 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.70 (harus < 0.5)
- Buy & hold jendela OOS: return +88.6%, Sharpe 0.75, maxDD -39.2% | strategi: return -0.1%, Sharpe -0.01, maxDD -3.4%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -2.1%, p95 -3.1%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.29 | 0.00 | 0 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.29 | inf | 2 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.19 | 0.79 | 3 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.33 | 0.00 | 0 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.67 | 0.59 | 4 |