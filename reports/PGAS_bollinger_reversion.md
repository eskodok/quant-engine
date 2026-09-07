## Validasi bollinger_reversion @ PGAS

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 10 < 30: belum cukup bukti
- GAGAL: PF OOS dengan biaya x2.0 = 0.99 < 1: edge habis dimakan biaya
- PERINGATAN: PBO 0.39 agak tinggi
- PERINGATAN: Sharpe OOS 0.21 < buy&hold 0.36: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.03 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 10 trade OOS (30.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 12 | 10 | 10 |
| Profit factor | 1.22 | 1.31 | 0.99 |
| Win rate | 69.4% | 70.0% | 50.0% |
| Expectancy (R) | 0.05 | 0.11 | -0.01 |
| Sharpe | 0.09 | 0.21 | -0.01 |
| Max DD | -3.0% | -3.1% | -3.5% |
| CAGR | 0.2% | 0.4% | -0.0% |

- Deflated Sharpe prob (n_trials=40): 0.03
- Timing vs entry acak: persentil 85 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.39 (harus < 0.5)
- Buy & hold jendela OOS: return +19.7%, Sharpe 0.36, maxDD -44.3% | strategi: return +1.1%, Sharpe 0.21, maxDD -3.1%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -2.5%, p95 -3.5%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.60 | inf | 1 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.85 | inf | 2 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.25 | inf | 2 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.70 | inf | 1 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.72 | 0.20 | 4 |