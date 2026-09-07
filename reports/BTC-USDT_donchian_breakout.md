## Validasi donchian_breakout @ BTC/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 21 < 30: belum cukup bukti
- GAGAL: PF OOS 0.94 < 1.15
- GAGAL: degradasi IS→OOS 60% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.88 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 31 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.71 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -0.08 < buy&hold 0.93: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 21 trade OOS (9.5/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 24 | 21 | 21 |
| Profit factor | 2.38 | 0.94 | 0.88 |
| Win rate | 50.1% | 33.3% | 33.3% |
| Expectancy (R) | 0.71 | -0.04 | -0.08 |
| Sharpe | 0.94 | -0.08 | -0.16 |
| Max DD | -3.8% | -6.2% | -6.5% |
| CAGR | 3.1% | -0.3% | -0.6% |

- Deflated Sharpe prob (n_trials=45): 0.01
- Timing vs entry acak: persentil 31 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.71 (harus < 0.5)
- Buy & hold jendela OOS: return +188.2%, Sharpe 0.93, maxDD -53.0% | strategi: return -1.0%, Sharpe -0.08, maxDD -6.2%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -6.6%, p95 -9.8%
- Parameter terpilih (fold terakhir): {'donchian_n': 55, 'rr': 3.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2017-10-19→2023-05-29 | 2023-05-30→2024-01-23 | {'donchian_n': 20, 'rr': 3.0} | 2.99 | 1.59 | 4 |
| 2 | 2018-06-22→2024-01-23 | 2024-01-24→2024-09-18 | {'donchian_n': 20, 'rr': 3.0} | 2.73 | 0.78 | 6 |
| 3 | 2019-02-16→2024-09-18 | 2024-09-19→2025-05-15 | {'donchian_n': 20, 'rr': 3.0} | 2.30 | 2.23 | 6 |
| 4 | 2019-10-13→2025-05-15 | 2025-05-16→2026-01-09 | {'donchian_n': 20, 'rr': 3.0} | 2.42 | 0.00 | 5 |
| 5 | 2020-06-08→2026-01-09 | 2026-01-10→2026-09-05 | {'donchian_n': 55, 'rr': 3.0} | 1.44 | 0.00 | 0 |