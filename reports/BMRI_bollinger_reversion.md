## Validasi bollinger_reversion @ BMRI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: PF OOS 0.63 < 1.15
- GAGAL: degradasi IS→OOS 44% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.43 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 65 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: PBO 0.37 agak tinggi
- PERINGATAN: Sharpe OOS -0.29 < buy&hold -0.11: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 7 trade OOS (42.9/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 17 | 7 | 7 |
| Profit factor | 1.14 | 0.63 | 0.43 |
| Win rate | 62.9% | 57.1% | 57.1% |
| Expectancy (R) | 0.04 | -0.18 | -0.30 |
| Sharpe | 0.08 | -0.29 | -0.48 |
| Max DD | -3.8% | -2.2% | -2.7% |
| CAGR | 0.1% | -0.5% | -0.7% |

- Deflated Sharpe prob (n_trials=40): 0.00
- Timing vs entry acak: persentil 65 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.37 (harus < 0.5)
- Buy & hold jendela OOS: return -22.5%, Sharpe -0.11, maxDD -50.2% | strategi: return -1.3%, Sharpe -0.29, maxDD -2.2%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -2.4%, p95 -3.4%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.67 | 1.28 | 4 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.92 | 0.49 | 2 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.16 | 0.00 | 0 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.53 | 0.00 | 0 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.42 | 0.00 | 1 |