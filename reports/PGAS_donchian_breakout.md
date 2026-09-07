## Validasi donchian_breakout @ PGAS

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 15 < 30: belum cukup bukti
- GAGAL: PF OOS 0.36 < 1.15
- GAGAL: PF in-sample 0.32 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.28 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 21 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: PBO 0.46 agak tinggi
- PERINGATAN: Sharpe OOS -0.92 < buy&hold 0.36: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 15 trade OOS (13.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 11 | 15 | 15 |
| Profit factor | 0.32 | 0.36 | 0.28 |
| Win rate | 23.2% | 26.7% | 26.7% |
| Expectancy (R) | -0.55 | -0.49 | -0.60 |
| Sharpe | -0.69 | -0.92 | -1.14 |
| Max DD | -7.9% | -10.0% | -10.9% |
| CAGR | -1.3% | -2.6% | -3.2% |

- Deflated Sharpe prob (n_trials=45): 0.00
- Timing vs entry acak: persentil 21 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.46 (harus < 0.5)
- Buy & hold jendela OOS: return +19.7%, Sharpe 0.36, maxDD -44.3% | strategi: return -7.1%, Sharpe -0.92, maxDD -10.0%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -8.0%, p95 -9.7%
- Parameter terpilih (fold terakhir): {'donchian_n': 40, 'rr': 2.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'donchian_n': 20, 'rr': 1.5} | 0.36 | inf | 1 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'donchian_n': 20, 'rr': 1.5} | 0.45 | 0.00 | 4 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'donchian_n': 20, 'rr': 1.5} | 0.19 | 0.00 | 3 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'donchian_n': 20, 'rr': 1.5} | 0.14 | 1.18 | 6 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'donchian_n': 40, 'rr': 2.0} | 0.47 | 0.00 | 1 |