## Validasi trend_pullback @ BTC/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: PF OOS 1.10 < 1.15
- GAGAL: timing entry tidak lebih baik dari acak (persentil 46 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.66 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS 0.11 < buy&hold 0.93: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 31 trade OOS (9.7/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 31 | 31 | 31 |
| Profit factor | 1.71 | 1.10 | 1.00 |
| Win rate | 33.8% | 25.8% | 25.8% |
| Expectancy (R) | 0.26 | 0.05 | 0.01 |
| Sharpe | 0.52 | 0.11 | 0.00 |
| Max DD | -3.5% | -6.3% | -7.2% |
| CAGR | 1.4% | 0.3% | -0.1% |

- Deflated Sharpe prob (n_trials=135): 0.01
- Timing vs entry acak: persentil 46 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.66 (harus < 0.5)
- Buy & hold jendela OOS: return +188.2%, Sharpe 0.93, maxDD -53.0% | strategi: return +1.1%, Sharpe 0.11, maxDD -6.3%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -5.1%, p95 -7.9%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2017-10-19→2023-05-29 | 2023-05-30→2024-01-23 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 1.77 | 4.08 | 7 |
| 2 | 2018-06-22→2024-01-23 | 2024-01-24→2024-09-18 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 2.12 | 0.91 | 9 |
| 3 | 2019-02-16→2024-09-18 | 2024-09-19→2025-05-15 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 1.64 | 1.07 | 7 |
| 4 | 2019-10-13→2025-05-15 | 2025-05-16→2026-01-09 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 1.73 | 0.18 | 8 |
| 5 | 2020-06-08→2026-01-09 | 2026-01-10→2026-09-05 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0} | 1.28 | 0.00 | 0 |