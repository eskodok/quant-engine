## Validasi rsi2_reversion @ INDF

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 14 < 30: belum cukup bukti
- GAGAL: PF OOS 0.53 < 1.15
- GAGAL: degradasi IS→OOS 70% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.30 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 73 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: PBO 0.44 agak tinggi
- PERINGATAN: Sharpe OOS -0.59 < buy&hold 0.22: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 14 trade OOS (21.4/100 trade)
- PERINGATAN: parameter tidak stabil antar fold (40%)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 28 | 14 | 14 |
| Profit factor | 1.77 | 0.53 | 0.30 |
| Win rate | 66.2% | 42.9% | 42.9% |
| Expectancy (R) | 0.11 | -0.16 | -0.27 |
| Sharpe | 0.32 | -0.59 | -1.00 |
| Max DD | -2.2% | -3.1% | -4.4% |
| CAGR | 0.4% | -0.8% | -1.4% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 73 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.44 (harus < 0.5)
- Buy & hold jendela OOS: return +7.0%, Sharpe 0.22, maxDD -30.8% | strategi: return -2.2%, Sharpe -0.59, maxDD -3.1%
- Stabilitas parameter antar fold: 40%
- Monte Carlo max DD: median -3.2%, p95 -4.1%
- Parameter terpilih (fold terakhir): {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 0} | 2.26 | 0.00 | 1 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_buy': 10.0, 'exit_ema': 5, 'need_trend': 0} | 2.20 | inf | 2 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 0} | 2.13 | 0.52 | 6 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 0} | 1.61 | 0.25 | 4 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'rsi_buy': 15.0, 'exit_ema': 5, 'need_trend': 0} | 0.64 | inf | 1 |