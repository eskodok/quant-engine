## Validasi rsi2_reversion @ BMRI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: degradasi IS→OOS 58% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.61 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 65 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 7 trade OOS (42.9/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 21 | 7 | 7 |
| Profit factor | 2.75 | 1.16 | 0.61 |
| Win rate | 55.1% | 71.4% | 57.1% |
| Expectancy (R) | 0.13 | 0.03 | -0.09 |
| Sharpe | 0.37 | 0.07 | -0.20 |
| Max DD | -1.4% | -1.3% | -1.5% |
| CAGR | 0.5% | 0.1% | -0.2% |

- Deflated Sharpe prob (n_trials=60): 0.01
- Timing vs entry acak: persentil 65 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.29 (harus < 0.5)
- Buy & hold jendela OOS: return -22.5%, Sharpe -0.11, maxDD -50.2% | strategi: return +0.2%, Sharpe 0.07, maxDD -1.3%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -1.0%, p95 -1.3%
- Parameter terpilih (fold terakhir): {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 2.77 | inf | 1 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 2.49 | inf | 4 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 2.91 | 0.00 | 0 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 4.26 | 0.00 | 1 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 0} | 1.33 | 0.00 | 1 |