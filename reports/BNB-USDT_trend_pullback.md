## Validasi trend_pullback @ BNB/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 20 < 30: belum cukup bukti
- GAGAL: PBO 0.76 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: deflated Sharpe prob 0.41 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 20 trade OOS (15.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 23 | 20 | 20 |
| Profit factor | 2.56 | 3.50 | 3.12 |
| Win rate | 42.2% | 50.0% | 45.0% |
| Expectancy (R) | 0.38 | 0.57 | 0.52 |
| Sharpe | 0.77 | 1.50 | 1.39 |
| Max DD | -3.9% | -2.7% | -2.9% |
| CAGR | 1.9% | 4.2% | 3.8% |

- Deflated Sharpe prob (n_trials=135): 0.41
- Timing vs entry acak: persentil 98 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.76 (harus < 0.5)
- Buy & hold jendela OOS: return +136.8%, Sharpe 0.89, maxDD -58.2% | strategi: return +11.2%, Sharpe 1.50, maxDD -2.7%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -1.7%, p95 -2.8%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2019-06-19→2024-01-24 | 2024-01-25→2024-08-01 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 1.73 | inf | 3 |
| 2 | 2019-12-26→2024-08-01 | 2024-08-02→2025-02-07 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 2.49 | 2.83 | 5 |
| 3 | 2020-07-03→2025-02-07 | 2025-02-08→2025-08-16 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 3.27 | 2.37 | 7 |
| 4 | 2021-01-09→2025-08-16 | 2025-08-17→2026-02-22 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 2.75 | 3.57 | 5 |
| 5 | 2021-07-18→2026-02-22 | 2026-02-23→2026-08-31 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 2.58 | 0.00 | 0 |