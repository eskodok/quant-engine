## Validasi trend_pullback @ BTC/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: PF OOS 1.10 < 1.15
- GAGAL: timing entry tidak lebih baik dari acak (persentil 51 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.69 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS 0.11 < buy&hold 0.92: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 31 trade OOS (9.7/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 31 | 31 | 31 |
| Profit factor | 1.71 | 1.10 | 1.00 |
| Win rate | 33.6% | 25.8% | 25.8% |
| Expectancy (R) | 0.26 | 0.05 | 0.01 |
| Sharpe | 0.51 | 0.11 | 0.00 |
| Max DD | -3.5% | -6.3% | -7.2% |
| CAGR | 1.4% | 0.3% | -0.1% |

- Deflated Sharpe prob (n_trials=135): 0.01
- Timing vs entry acak: persentil 51 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.69 (harus < 0.5)
- Buy & hold jendela OOS: return +180.1%, Sharpe 0.92, maxDD -53.0% | strategi: return +1.1%, Sharpe 0.11, maxDD -6.3%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -5.1%, p95 -7.9%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2017-10-19→2023-05-28 | 2023-05-29→2024-01-21 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 1.81 | 4.08 | 7 |
| 2 | 2018-06-21→2024-01-21 | 2024-01-22→2024-09-15 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 2.12 | 0.91 | 9 |
| 3 | 2019-02-14→2024-09-15 | 2024-09-16→2025-05-11 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 1.64 | 1.07 | 7 |
| 4 | 2019-10-10→2025-05-11 | 2025-05-12→2026-01-04 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 1.70 | 0.18 | 8 |
| 5 | 2020-06-04→2026-01-04 | 2026-01-05→2026-08-30 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0} | 1.28 | 0.00 | 0 |