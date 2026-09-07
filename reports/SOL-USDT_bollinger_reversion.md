## Validasi bollinger_reversion @ SOL/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 7 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.81 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PBO 0.87 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: deflated Sharpe prob 0.07 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 7 trade OOS (42.9/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 12 | 7 | 7 |
| Profit factor | 0.81 | 1.98 | 1.90 |
| Win rate | 56.8% | 71.4% | 71.4% |
| Expectancy (R) | -0.09 | 0.29 | 0.27 |
| Sharpe | -0.16 | 0.61 | 0.57 |
| Max DD | -3.5% | -1.7% | -1.8% |
| CAGR | -0.3% | 1.1% | 1.1% |

- Deflated Sharpe prob (n_trials=40): 0.07
- Timing vs entry acak: persentil 95 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.87 (harus < 0.5)
- Buy & hold jendela OOS: return -55.5%, Sharpe -0.21, maxDD -76.2% | strategi: return +2.0%, Sharpe 0.61, maxDD -1.7%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -1.0%, p95 -2.0%
- Parameter terpilih (fold terakhir): {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2021-08-04→2024-12-01 | 2024-12-02→2025-04-08 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.52 | 1.57 | 3 |
| 2 | 2021-12-10→2025-04-08 | 2025-04-09→2025-08-14 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.73 | inf | 1 |
| 3 | 2022-04-17→2025-08-14 | 2025-08-15→2025-12-20 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 0.68 | 1.96 | 3 |
| 4 | 2022-08-23→2025-12-20 | 2025-12-21→2026-04-27 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.01 | 0.00 | 0 |
| 5 | 2022-12-29→2026-04-27 | 2026-04-28→2026-09-02 | {'bb_n': 20, 'bb_k': 2.0, 'need_trend': 0} | 1.11 | 0.00 | 0 |