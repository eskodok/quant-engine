## Validasi bollinger_reversion @ BBRI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 2 < 30: belum cukup bukti
- GAGAL: PF OOS 0.00 < 1.15
- GAGAL: PF in-sample 0.88 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 100% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.00 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 0 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.67 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.80 < buy&hold -0.27: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 2 trade OOS (150.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 16 | 2 | 2 |
| Profit factor | 0.88 | 0.00 | 0.00 |
| Win rate | 47.6% | 0.0% | 0.0% |
| Expectancy (R) | -0.12 | -1.11 | -1.22 |
| Sharpe | -0.09 | -0.80 | -0.84 |
| Max DD | -4.3% | -2.6% | -2.7% |
| CAGR | -0.2% | -0.8% | -0.9% |

- Deflated Sharpe prob (n_trials=40): 0.00
- Timing vs entry acak: persentil 0 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.67 (harus < 0.5)
- Buy & hold jendela OOS: return -32.2%, Sharpe -0.27, maxDD -59.5% | strategi: return -2.1%, Sharpe -0.80, maxDD -2.6%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'bb_n': 30, 'bb_k': 2.5, 'need_trend': 0} | 0.90 | 0.00 | 2 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.67 | 0.00 | 0 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.98 | 0.00 | 0 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.08 | 0.00 | 0 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 0} | 0.76 | 0.00 | 0 |