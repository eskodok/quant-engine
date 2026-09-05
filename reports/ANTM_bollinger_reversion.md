## Validasi bollinger_reversion @ ANTM

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 6 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.95 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- PERINGATAN: PBO 0.34 agak tinggi
- PERINGATAN: deflated Sharpe prob 0.14 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 6 trade OOS (50.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 12 | 6 | 6 |
| Profit factor | 0.95 | 3.38 | 2.90 |
| Win rate | 45.4% | 83.3% | 83.3% |
| Expectancy (R) | -0.01 | 0.41 | 0.32 |
| Sharpe | -0.03 | 0.71 | 0.58 |
| Max DD | -5.0% | -1.1% | -1.1% |
| CAGR | -0.0% | 0.9% | 0.7% |

- Deflated Sharpe prob (n_trials=40): 0.14
- Timing vs entry acak: persentil 79 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.34 (harus < 0.5)
- Buy & hold jendela OOS: return +75.1%, Sharpe 0.66, maxDD -46.8% | strategi: return +2.5%, Sharpe 0.71, maxDD -1.1%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -1.0%, p95 -1.0%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.00 | 0.00 | 0 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.00 | inf | 1 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.11 | inf | 2 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.84 | inf | 2 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.82 | 0.00 | 1 |