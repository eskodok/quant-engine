## Validasi bollinger_reversion @ UNTR

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 9 < 30: belum cukup bukti
- GAGAL: PF OOS 0.80 < 1.15
- GAGAL: PF OOS dengan biaya x2.0 = 0.54 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 74 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: PBO 0.30 agak tinggi
- PERINGATAN: Sharpe OOS -0.14 < buy&hold 0.21: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 9 trade OOS (33.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 16 | 9 | 9 |
| Profit factor | 1.32 | 0.80 | 0.54 |
| Win rate | 54.9% | 55.6% | 55.6% |
| Expectancy (R) | 0.12 | -0.09 | -0.24 |
| Sharpe | 0.22 | -0.14 | -0.36 |
| Max DD | -2.7% | -3.1% | -3.5% |
| CAGR | 0.4% | -0.3% | -0.7% |

- Deflated Sharpe prob (n_trials=40): 0.01
- Timing vs entry acak: persentil 74 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.30 (harus < 0.5)
- Buy & hold jendela OOS: return +3.7%, Sharpe 0.21, maxDD -35.8% | strategi: return -0.8%, Sharpe -0.14, maxDD -3.1%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -2.7%, p95 -3.9%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.29 | 0.00 | 0 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.29 | inf | 2 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.49 | 0.49 | 3 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.31 | 0.69 | 3 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.21 | 0.00 | 1 |