## Validasi trend_pullback @ UNTR

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 8 < 30: belum cukup bukti
- GAGAL: PBO 0.66 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: deflated Sharpe prob 0.03 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 8 trade OOS (37.5/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 17 | 8 | 8 |
| Profit factor | 1.34 | 1.94 | 1.50 |
| Win rate | 34.8% | 50.0% | 50.0% |
| Expectancy (R) | 0.30 | 0.32 | 0.17 |
| Sharpe | 0.27 | 0.50 | 0.31 |
| Max DD | -3.0% | -2.9% | -3.5% |
| CAGR | 0.4% | 0.9% | 0.6% |

- Deflated Sharpe prob (n_trials=135): 0.03
- Timing vs entry acak: persentil 87 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.66 (harus < 0.5)
- Buy & hold jendela OOS: return +3.7%, Sharpe 0.21, maxDD -35.8% | strategi: return +2.5%, Sharpe 0.50, maxDD -2.9%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -1.6%, p95 -2.6%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 1.64 | 0.00 | 0 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 1.31 | 2.07 | 4 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 2.0} | 1.15 | 0.00 | 1 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 1.08 | 1.86 | 2 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 1.49 | inf | 1 |