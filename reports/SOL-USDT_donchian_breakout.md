## Validasi donchian_breakout @ SOL/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 3 < 30: belum cukup bukti
- GAGAL: PF OOS 0.00 < 1.15
- GAGAL: degradasi IS→OOS 100% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.00 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 0 < 75): hasil = arus pasar, bukan sinyal
- GAGAL: PBO 0.74 >= 0.5: parameter terbaik in-sample cenderung jelek out-of-sample (overfit)
- PERINGATAN: Sharpe OOS -1.00 < buy&hold -0.21: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 3 trade OOS (66.7/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 13 | 3 | 3 |
| Profit factor | 3.11 | 0.00 | 0.00 |
| Win rate | 55.7% | 0.0% | 0.0% |
| Expectancy (R) | 0.59 | -0.76 | -0.78 |
| Sharpe | 0.88 | -1.00 | -1.02 |
| Max DD | -3.1% | -2.3% | -2.3% |
| CAGR | 2.4% | -1.3% | -1.3% |

- Deflated Sharpe prob (n_trials=45): 0.00
- Timing vs entry acak: persentil 0 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.74 (harus < 0.5)
- Buy & hold jendela OOS: return -55.5%, Sharpe -0.21, maxDD -76.2% | strategi: return -2.3%, Sharpe -1.00, maxDD -2.3%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'donchian_n': 20, 'rr': 2.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2021-08-04→2024-12-01 | 2024-12-02→2025-04-08 | {'donchian_n': 20, 'rr': 1.5} | 5.82 | 0.00 | 1 |
| 2 | 2021-12-10→2025-04-08 | 2025-04-09→2025-08-14 | {'donchian_n': 20, 'rr': 1.5} | 2.87 | 0.00 | 1 |
| 3 | 2022-04-17→2025-08-14 | 2025-08-15→2025-12-20 | {'donchian_n': 20, 'rr': 1.5} | 2.57 | 0.00 | 1 |
| 4 | 2022-08-23→2025-12-20 | 2025-12-21→2026-04-27 | {'donchian_n': 20, 'rr': 2.0} | 2.14 | 0.00 | 0 |
| 5 | 2022-12-29→2026-04-27 | 2026-04-28→2026-09-02 | {'donchian_n': 20, 'rr': 2.0} | 2.14 | 0.00 | 0 |