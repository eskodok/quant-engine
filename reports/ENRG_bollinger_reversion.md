## Validasi bollinger_reversion @ ENRG

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 9 < 30: belum cukup bukti
- PERINGATAN: Sharpe OOS 0.84 < buy&hold 1.18: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.20 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 9 trade OOS (33.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 11 | 9 | 9 |
| Profit factor | 2.92 | 13.42 | 9.14 |
| Win rate | 81.3% | 88.9% | 88.9% |
| Expectancy (R) | 0.32 | 0.66 | 0.57 |
| Sharpe | 0.48 | 0.84 | 0.75 |
| Max DD | -1.8% | -2.3% | -2.4% |
| CAGR | 0.8% | 2.4% | 2.2% |

- Deflated Sharpe prob (n_trials=40): 0.20
- Timing vs entry acak: persentil 100 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.26 (harus < 0.5)
- Buy & hold jendela OOS: return +449.2%, Sharpe 1.18, maxDD -57.1% | strategi: return +6.9%, Sharpe 0.84, maxDD -2.3%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -0.5%, p95 -0.5%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 3.50 | 0.00 | 0 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 2.60 | inf | 1 |
| 3 | 2019-09-24→2024-12-16 | 2024-12-17→2025-07-25 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 2.96 | inf | 2 |
| 4 | 2020-04-08→2025-07-25 | 2025-07-28→2026-02-11 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 2.96 | 3.49 | 3 |
| 5 | 2020-11-04→2026-02-11 | 2026-02-12→2026-09-04 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 2.54 | inf | 3 |