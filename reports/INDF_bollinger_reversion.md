## Validasi bollinger_reversion @ INDF

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: PF OOS 0.31 < 1.15
- GAGAL: PF in-sample 0.94 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 66% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.21 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 37 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: PBO 0.49 agak tinggi
- PERINGATAN: Sharpe OOS -0.81 < buy&hold 0.21: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 7 trade OOS (42.9/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 14 | 7 | 7 |
| Profit factor | 0.94 | 0.31 | 0.21 |
| Win rate | 57.1% | 28.6% | 28.6% |
| Expectancy (R) | -0.24 | -2.57 | -1.37 |
| Sharpe | -0.07 | -0.81 | -1.06 |
| Max DD | -2.7% | -3.6% | -4.1% |
| CAGR | -0.1% | -1.0% | -1.3% |

- Deflated Sharpe prob (n_trials=40): 0.00
- Timing vs entry acak: persentil 37 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.49 (harus < 0.5)
- Buy & hold jendela OOS: return +6.3%, Sharpe 0.21, maxDD -30.8% | strategi: return -2.6%, Sharpe -0.81, maxDD -3.6%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -2.9%, p95 -3.8%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.12 | 0.00 | 1 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.60 | inf | 1 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.30 | 0.24 | 2 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.02 | 0.00 | 3 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.64 | 0.00 | 0 |