## Validasi donchian_breakout @ PGAS

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 15 < 30: belum cukup bukti
- GAGAL: PF OOS 0.41 < 1.15
- GAGAL: PF in-sample 0.34 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.33 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 24 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: PBO 0.49 agak tinggi
- PERINGATAN: Sharpe OOS -0.82 < buy&hold 0.33: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 15 trade OOS (13.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 11 | 15 | 15 |
| Profit factor | 0.34 | 0.41 | 0.33 |
| Win rate | 23.2% | 26.7% | 26.7% |
| Expectancy (R) | -0.53 | -0.43 | -0.54 |
| Sharpe | -0.67 | -0.82 | -1.05 |
| Max DD | -7.9% | -9.2% | -10.1% |
| CAGR | -1.2% | -2.3% | -2.9% |

- Deflated Sharpe prob (n_trials=45): 0.00
- Timing vs entry acak: persentil 24 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.49 (harus < 0.5)
- Buy & hold jendela OOS: return +16.2%, Sharpe 0.33, maxDD -44.3% | strategi: return -6.2%, Sharpe -0.82, maxDD -9.2%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -7.4%, p95 -9.4%
- Parameter terpilih (fold terakhir): {'donchian_n': 40, 'rr': 2.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-25 | 2023-10-26→2024-05-30 | {'donchian_n': 20, 'rr': 1.5} | 0.36 | inf | 1 |
| 2 | 2019-03-13→2024-05-30 | 2024-05-31→2024-12-12 | {'donchian_n': 20, 'rr': 1.5} | 0.53 | 0.00 | 4 |
| 3 | 2019-09-20→2024-12-12 | 2024-12-13→2025-07-23 | {'donchian_n': 20, 'rr': 1.5} | 0.20 | 0.00 | 3 |
| 4 | 2020-04-06→2025-07-23 | 2025-07-24→2026-02-09 | {'donchian_n': 20, 'rr': 1.5} | 0.14 | 1.18 | 6 |
| 5 | 2020-11-02→2026-02-09 | 2026-02-10→2026-09-03 | {'donchian_n': 40, 'rr': 2.0} | 0.47 | 0.00 | 1 |