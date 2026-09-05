## Validasi bollinger_reversion @ BNB/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 11 < 30: belum cukup bukti
- GAGAL: PF OOS 0.82 < 1.15
- GAGAL: PF OOS dengan biaya x2.0 = 0.76 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 38 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: Sharpe OOS -0.21 < buy&hold 0.89: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 11 trade OOS (27.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 18 | 11 | 11 |
| Profit factor | 1.17 | 0.82 | 0.76 |
| Win rate | 56.6% | 45.5% | 45.5% |
| Expectancy (R) | 0.07 | -0.09 | -0.12 |
| Sharpe | 0.14 | -0.21 | -0.28 |
| Max DD | -3.9% | -4.2% | -4.4% |
| CAGR | 0.3% | -0.4% | -0.5% |

- Deflated Sharpe prob (n_trials=40): 0.01
- Timing vs entry acak: persentil 38 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.21 (harus < 0.5)
- Buy & hold jendela OOS: return +136.8%, Sharpe 0.89, maxDD -58.2% | strategi: return -1.1%, Sharpe -0.21, maxDD -4.2%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -3.2%, p95 -4.8%
- Parameter terpilih (fold terakhir): {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2019-06-19→2024-01-24 | 2024-01-25→2024-08-01 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.82 | 1.41 | 3 |
| 2 | 2019-12-26→2024-08-01 | 2024-08-02→2025-02-07 | {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 0} | 1.43 | 0.95 | 5 |
| 3 | 2020-07-03→2025-02-07 | 2025-02-08→2025-08-16 | {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 0} | 1.14 | inf | 1 |
| 4 | 2021-01-09→2025-08-16 | 2025-08-17→2026-02-22 | {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 0} | 1.36 | 0.00 | 2 |
| 5 | 2021-07-18→2026-02-22 | 2026-02-23→2026-08-31 | {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 0} | 1.09 | 0.00 | 0 |