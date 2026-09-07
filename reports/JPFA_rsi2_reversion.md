## Validasi rsi2_reversion @ JPFA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 20 < 30: belum cukup bukti
- GAGAL: timing entry tidak lebih baik dari acak (persentil 74 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: PBO 0.30 agak tinggi
- PERINGATAN: Sharpe OOS 0.42 < buy&hold 0.75: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.05 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 20 trade OOS (15.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 18 | 20 | 20 |
| Profit factor | 1.85 | 1.54 | 1.09 |
| Win rate | 83.5% | 80.0% | 60.0% |
| Expectancy (R) | 0.11 | 0.09 | 0.02 |
| Sharpe | 0.36 | 0.42 | 0.08 |
| Max DD | -1.6% | -1.3% | -1.4% |
| CAGR | 0.4% | 0.7% | 0.1% |

- Deflated Sharpe prob (n_trials=60): 0.05
- Timing vs entry acak: persentil 74 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.30 (harus < 0.5)
- Buy & hold jendela OOS: return +88.6%, Sharpe 0.75, maxDD -39.2% | strategi: return +1.8%, Sharpe 0.42, maxDD -1.3%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -1.8%, p95 -2.8%
- Parameter terpilih (fold terakhir): {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 1}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 1} | 1.57 | inf | 1 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_buy': 15.0, 'exit_ema': 10, 'need_trend': 1} | 1.61 | 2.14 | 8 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 1} | 2.19 | 0.54 | 5 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 1} | 1.57 | inf | 2 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 1} | 2.29 | 1.10 | 4 |