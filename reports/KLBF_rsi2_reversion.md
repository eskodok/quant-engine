## Validasi rsi2_reversion @ KLBF

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: degradasi IS→OOS 47% > 40%: indikasi overfit
- PERINGATAN: PBO 0.49 agak tinggi
- PERINGATAN: deflated Sharpe prob 0.09 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 7 trade OOS (42.9/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 21 | 7 | 7 |
| Profit factor | 8.05 | 4.26 | 2.21 |
| Win rate | 78.4% | 71.4% | 57.1% |
| Expectancy (R) | 0.24 | 0.23 | 0.12 |
| Sharpe | 0.73 | 0.76 | 0.42 |
| Max DD | -1.5% | -0.7% | -0.9% |
| CAGR | 0.9% | 0.6% | 0.3% |

- Deflated Sharpe prob (n_trials=60): 0.09
- Timing vs entry acak: persentil 96 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.49 (harus < 0.5)
- Buy & hold jendela OOS: return -55.8%, Sharpe -0.64, maxDD -62.1% | strategi: return +1.6%, Sharpe 0.76, maxDD -0.7%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -0.3%, p95 -0.5%
- Parameter terpilih (fold terakhir): {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 1}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 1.88 | 0.00 | 0 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 1} | 1.77 | 9.74 | 4 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_buy': 5.0, 'exit_ema': 5, 'need_trend': 0} | 4.10 | inf | 2 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 1} | 13.97 | 0.00 | 1 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 1} | 18.52 | 0.00 | 0 |