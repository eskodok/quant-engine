## Validasi bollinger_reversion @ MAPI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 13 < 30: belum cukup bukti
- GAGAL: PF OOS 0.88 < 1.15
- GAGAL: PF in-sample 1.09 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.70 < 1: edge habis dimakan biaya
- PERINGATAN: PBO 0.41 agak tinggi
- PERINGATAN: Sharpe OOS -0.13 < buy&hold 0.06: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 13 trade OOS (23.1/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 17 | 13 | 13 |
| Profit factor | 1.09 | 0.88 | 0.70 |
| Win rate | 66.4% | 53.8% | 53.8% |
| Expectancy (R) | 0.01 | -0.03 | -0.15 |
| Sharpe | 0.02 | -0.13 | -0.34 |
| Max DD | -4.3% | -4.9% | -5.4% |
| CAGR | -0.0% | -0.3% | -0.8% |

- Deflated Sharpe prob (n_trials=40): 0.01
- Timing vs entry acak: persentil 75 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.41 (harus < 0.5)
- Buy & hold jendela OOS: return -20.8%, Sharpe 0.06, maxDD -46.0% | strategi: return -0.8%, Sharpe -0.13, maxDD -4.9%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -3.7%, p95 -5.2%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.82 | 0.21 | 6 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.75 | 0.67 | 2 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.99 | 0.00 | 0 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.96 | 0.00 | 0 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.92 | 3.57 | 5 |