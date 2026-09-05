## Validasi donchian_breakout @ ETH/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 13 < 30: belum cukup bukti
- GAGAL: PF OOS 1.10 < 1.15
- GAGAL: degradasi IS→OOS 52% > 40%: indikasi overfit
- GAGAL: timing entry tidak lebih baik dari acak (persentil 45 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.89 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS 0.09 < buy&hold 0.43: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.02 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 13 trade OOS (15.4/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 22 | 13 | 13 |
| Profit factor | 2.28 | 1.10 | 1.04 |
| Win rate | 48.1% | 30.8% | 30.8% |
| Expectancy (R) | 0.61 | 0.07 | 0.04 |
| Sharpe | 0.63 | 0.09 | 0.05 |
| Max DD | -4.2% | -4.2% | -4.3% |
| CAGR | 2.4% | 0.2% | 0.1% |

- Deflated Sharpe prob (n_trials=45): 0.02
- Timing vs entry acak: persentil 45 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.89 (harus < 0.5)
- Buy & hold jendela OOS: return +26.9%, Sharpe 0.43, maxDD -67.5% | strategi: return +0.8%, Sharpe 0.09, maxDD -4.2%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -4.5%, p95 -6.9%
- Parameter terpilih (fold terakhir): {'donchian_n': 20, 'rr': 3.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2017-11-09→2023-06-05 | 2023-06-06→2024-01-28 | {'donchian_n': 20, 'rr': 3.0} | 3.04 | 0.93 | 4 |
| 2 | 2018-07-10→2024-01-28 | 2024-01-29→2024-09-21 | {'donchian_n': 20, 'rr': 3.0} | 2.36 | 0.80 | 5 |
| 3 | 2019-03-04→2024-09-21 | 2024-09-22→2025-05-16 | {'donchian_n': 20, 'rr': 3.0} | 2.08 | 0.00 | 1 |
| 4 | 2019-10-27→2025-05-16 | 2025-05-17→2026-01-08 | {'donchian_n': 20, 'rr': 3.0} | 2.12 | 3.22 | 3 |
| 5 | 2020-06-20→2026-01-08 | 2026-01-09→2026-09-02 | {'donchian_n': 20, 'rr': 3.0} | 1.79 | 0.00 | 0 |