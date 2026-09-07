## Validasi bollinger_reversion @ ESSA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 9 < 30: belum cukup bukti
- GAGAL: PF OOS 0.88 < 1.15
- GAGAL: PF OOS dengan biaya x2.0 = 0.75 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 45 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.70 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.12 < buy&hold 0.28: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 9 trade OOS (33.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 13 | 9 | 9 |
| Profit factor | 1.11 | 0.88 | 0.75 |
| Win rate | 56.5% | 55.6% | 55.6% |
| Expectancy (R) | 0.06 | -0.05 | -0.12 |
| Sharpe | 0.09 | -0.12 | -0.26 |
| Max DD | -3.2% | -2.5% | -2.9% |
| CAGR | 0.1% | -0.2% | -0.4% |

- Deflated Sharpe prob (n_trials=40): 0.01
- Timing vs entry acak: persentil 45 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.70 (harus < 0.5)
- Buy & hold jendela OOS: return +3.2%, Sharpe 0.28, maxDD -47.7% | strategi: return -0.5%, Sharpe -0.12, maxDD -2.5%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -2.5%, p95 -3.7%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-30 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.07 | 0.00 | 0 |
| 2 | 2019-03-15→2024-05-30 | 2024-05-31→2024-12-11 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.07 | 1.43 | 3 |
| 3 | 2019-09-23→2024-12-11 | 2024-12-12→2025-07-21 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.13 | 0.29 | 3 |
| 4 | 2020-04-06→2025-07-21 | 2025-07-22→2026-02-04 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.05 | inf | 1 |
| 5 | 2020-10-27→2026-02-04 | 2026-02-05→2026-08-31 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.25 | 1.11 | 2 |