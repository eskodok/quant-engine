## Validasi trend_pullback @ ASII

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 9 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.83 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- PERINGATAN: deflated Sharpe prob 0.03 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 9 trade OOS (33.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 15 | 9 | 9 |
| Profit factor | 0.83 | 1.77 | 1.27 |
| Win rate | 26.2% | 44.4% | 33.3% |
| Expectancy (R) | -0.05 | 0.22 | 0.10 |
| Sharpe | -0.15 | 0.44 | 0.17 |
| Max DD | -2.8% | -2.0% | -2.4% |
| CAGR | -0.2% | 0.5% | 0.2% |

- Deflated Sharpe prob (n_trials=135): 0.03
- Timing vs entry acak: persentil 94 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.09 (harus < 0.5)
- Buy & hold jendela OOS: return -15.3%, Sharpe -0.02, maxDD -41.1% | strategi: return +1.4%, Sharpe 0.44, maxDD -2.0%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -1.3%, p95 -1.8%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.78 | 0.00 | 0 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.78 | 0.00 | 0 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.78 | 0.00 | 0 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.66 | 39.48 | 4 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 1.16 | 0.03 | 5 |