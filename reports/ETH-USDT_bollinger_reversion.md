## Validasi bollinger_reversion @ ETH/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 19 < 30: belum cukup bukti
- GAGAL: PF OOS 0.96 < 1.15
- GAGAL: degradasi IS→OOS 50% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.89 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 56 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.77 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.03 < buy&hold 0.43: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 19 trade OOS (15.8/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 24 | 19 | 19 |
| Profit factor | 1.91 | 0.96 | 0.89 |
| Win rate | 70.0% | 57.9% | 57.9% |
| Expectancy (R) | 0.23 | -0.02 | -0.04 |
| Sharpe | 0.53 | -0.03 | -0.11 |
| Max DD | -3.0% | -3.0% | -3.1% |
| CAGR | 1.0% | -0.1% | -0.3% |

- Deflated Sharpe prob (n_trials=40): 0.01
- Timing vs entry acak: persentil 56 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.77 (harus < 0.5)
- Buy & hold jendela OOS: return +26.9%, Sharpe 0.43, maxDD -67.5% | strategi: return -0.3%, Sharpe -0.03, maxDD -3.0%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -3.4%, p95 -5.1%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2017-11-09→2023-06-05 | 2023-06-06→2024-01-28 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 2.02 | 0.67 | 3 |
| 2 | 2018-07-10→2024-01-28 | 2024-01-29→2024-09-21 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 2.36 | 0.87 | 7 |
| 3 | 2019-03-04→2024-09-21 | 2024-09-22→2025-05-16 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.99 | 0.74 | 4 |
| 4 | 2019-10-27→2025-05-16 | 2025-05-17→2026-01-08 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.70 | 1.38 | 5 |
| 5 | 2020-06-20→2026-01-08 | 2026-01-09→2026-09-02 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.49 | 0.00 | 0 |