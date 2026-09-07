## Validasi bollinger_reversion @ UNVR

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 6 < 30: belum cukup bukti
- GAGAL: PF OOS 0.77 < 1.15
- GAGAL: degradasi IS→OOS 59% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.61 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 70 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 6 trade OOS (50.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 5 | 6 | 6 |
| Profit factor | 1.87 | 0.77 | 0.61 |
| Win rate | 66.7% | 33.3% | 33.3% |
| Expectancy (R) | 0.41 | -0.13 | -0.23 |
| Sharpe | 0.27 | -0.20 | -0.36 |
| Max DD | -1.6% | -3.3% | -3.7% |
| CAGR | 0.2% | -0.3% | -0.5% |

- Deflated Sharpe prob (n_trials=40): 0.01
- Timing vs entry acak: persentil 70 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.21 (harus < 0.5)
- Buy & hold jendela OOS: return -57.7%, Sharpe -0.45, maxDD -74.5% | strategi: return -0.8%, Sharpe -0.20, maxDD -3.3%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -2.3%, p95 -3.4%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.60 | 0.00 | 0 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 2.63 | 0.00 | 0 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 2.63 | 0.00 | 0 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.49 | 0.81 | 5 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.98 | 0.00 | 1 |