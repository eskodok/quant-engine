## Validasi bollinger_reversion @ BMRI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: PF OOS 0.63 < 1.15
- GAGAL: degradasi IS→OOS 45% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.43 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 62 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: PBO 0.39 agak tinggi
- PERINGATAN: Sharpe OOS -0.29 < buy&hold -0.15: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 7 trade OOS (42.9/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 17 | 7 | 7 |
| Profit factor | 1.14 | 0.63 | 0.43 |
| Win rate | 62.9% | 57.1% | 57.1% |
| Expectancy (R) | 0.04 | -0.18 | -0.30 |
| Sharpe | 0.09 | -0.29 | -0.48 |
| Max DD | -3.8% | -2.2% | -2.7% |
| CAGR | 0.1% | -0.5% | -0.7% |

- Deflated Sharpe prob (n_trials=40): 0.00
- Timing vs entry acak: persentil 62 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.39 (harus < 0.5)
- Buy & hold jendela OOS: return -25.5%, Sharpe -0.15, maxDD -50.2% | strategi: return -1.3%, Sharpe -0.29, maxDD -2.2%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -2.4%, p95 -3.4%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.69 | 1.28 | 4 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.92 | 0.49 | 2 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.16 | 0.00 | 0 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.53 | 0.00 | 0 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.42 | 0.00 | 1 |