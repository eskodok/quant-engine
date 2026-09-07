## Validasi trend_pullback @ SOL/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 6 < 30: belum cukup bukti
- GAGAL: PBO 0.64 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 6 trade OOS (50.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 20 | 6 | 6 |
| Profit factor | 2.24 | 1.65 | 1.57 |
| Win rate | 27.0% | 50.0% | 50.0% |
| Expectancy (R) | 0.29 | 0.25 | 0.23 |
| Sharpe | 0.81 | 0.34 | 0.31 |
| Max DD | -1.8% | -1.4% | -1.4% |
| CAGR | 1.8% | 0.8% | 0.8% |

- Deflated Sharpe prob (n_trials=135): 0.01
- Timing vs entry acak: persentil 77 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.64 (harus < 0.5)
- Buy & hold jendela OOS: return -55.5%, Sharpe -0.21, maxDD -76.2% | strategi: return +1.5%, Sharpe 0.34, maxDD -1.4%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -1.9%, p95 -2.3%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2021-08-04→2024-12-01 | 2024-12-02→2025-04-08 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 2.86 | 0.12 | 3 |
| 2 | 2021-12-10→2025-04-08 | 2025-04-09→2025-08-14 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 2.05 | inf | 1 |
| 3 | 2022-04-17→2025-08-14 | 2025-08-15→2025-12-20 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 1.97 | 2.82 | 2 |
| 4 | 2022-08-23→2025-12-20 | 2025-12-21→2026-04-27 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 1.93 | 0.00 | 0 |
| 5 | 2022-12-29→2026-04-27 | 2026-04-28→2026-09-02 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 2.39 | 0.00 | 0 |