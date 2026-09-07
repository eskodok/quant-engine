## Validasi trend_pullback @ PTRO

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 15 < 30: belum cukup bukti
- GAGAL: timing entry tidak lebih baik dari acak (persentil 65 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: Sharpe OOS 0.86 < buy&hold 1.52: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.09 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 15 trade OOS (20.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 24 | 15 | 15 |
| Profit factor | 1.87 | 2.23 | 1.95 |
| Win rate | 39.1% | 33.3% | 26.7% |
| Expectancy (R) | 0.29 | 0.38 | 0.32 |
| Sharpe | 0.55 | 0.86 | 0.75 |
| Max DD | -5.3% | -2.8% | -3.0% |
| CAGR | 1.3% | 2.0% | 1.7% |

- Deflated Sharpe prob (n_trials=135): 0.09
- Timing vs entry acak: persentil 65 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.24 (harus < 0.5)
- Buy & hold jendela OOS: return +1260.8%, Sharpe 1.52, maxDD -73.2% | strategi: return +5.7%, Sharpe 0.86, maxDD -2.8%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -2.3%, p95 -3.8%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 1.43 | 1.03 | 5 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 1.34 | inf | 3 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 1.95 | 0.00 | 5 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0} | 2.35 | 5.24 | 2 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 2.26 | 0.00 | 0 |