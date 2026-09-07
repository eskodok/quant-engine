## Validasi rsi2_reversion @ BBCA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 8 < 30: belum cukup bukti
- GAGAL: PF OOS 0.76 < 1.15
- GAGAL: degradasi IS→OOS 68% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.08 < 1: edge habis dimakan biaya
- PERINGATAN: PBO 0.30 agak tinggi
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 8 trade OOS (37.5/100 trade)
- PERINGATAN: parameter tidak stabil antar fold (40%)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 23 | 8 | 8 |
| Profit factor | 2.39 | 0.76 | 0.08 |
| Win rate | 67.3% | 62.5% | 37.5% |
| Expectancy (R) | 0.17 | -0.04 | -0.22 |
| Sharpe | 0.45 | -0.10 | -0.55 |
| Max DD | -1.7% | -1.7% | -2.0% |
| CAGR | 0.6% | -0.1% | -0.6% |

- Deflated Sharpe prob (n_trials=60): 0.01
- Timing vs entry acak: persentil 79 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.30 (harus < 0.5)
- Buy & hold jendela OOS: return -23.9%, Sharpe -0.21, maxDD -55.7% | strategi: return -0.3%, Sharpe -0.10, maxDD -1.7%
- Stabilitas parameter antar fold: 40%
- Monte Carlo max DD: median -1.1%, p95 -1.2%
- Parameter terpilih (fold terakhir): {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 1} | 2.60 | 0.00 | 2 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 1} | 1.81 | inf | 4 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 1.77 | 3.03 | 2 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 2.27 | 0.00 | 0 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-07 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 3.47 | 0.00 | 0 |