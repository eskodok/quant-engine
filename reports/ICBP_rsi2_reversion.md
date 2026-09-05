## Validasi rsi2_reversion @ ICBP

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: PF OOS 0.93 < 1.15
- GAGAL: degradasi IS→OOS 64% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.40 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 7 trade OOS (42.9/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 16 | 7 | 7 |
| Profit factor | 2.59 | 0.93 | 0.40 |
| Win rate | 71.5% | 71.4% | 57.1% |
| Expectancy (R) | 0.20 | -0.01 | -0.12 |
| Sharpe | 0.41 | -0.04 | -0.36 |
| Max DD | -1.5% | -1.5% | -1.7% |
| CAGR | 0.5% | -0.0% | -0.3% |

- Deflated Sharpe prob (n_trials=60): 0.01
- Timing vs entry acak: persentil 78 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.04 (harus < 0.5)
- Buy & hold jendela OOS: return -29.4%, Sharpe -0.29, maxDD -53.1% | strategi: return -0.1%, Sharpe -0.04, maxDD -1.5%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -1.1%, p95 -1.2%
- Parameter terpilih (fold terakhir): {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 5.80 | 0.14 | 2 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 2.50 | 17.44 | 2 |
| 3 | 2019-09-20→2024-12-11 | 2024-12-12→2025-07-22 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 1.75 | inf | 3 |
| 4 | 2020-04-06→2025-07-22 | 2025-07-23→2026-02-06 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 1.20 | 0.00 | 0 |
| 5 | 2020-11-02→2026-02-06 | 2026-02-09→2026-09-03 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 1.68 | 0.00 | 0 |