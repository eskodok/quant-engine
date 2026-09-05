## Validasi donchian_breakout @ ICBP

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 4 < 30: belum cukup bukti
- GAGAL: PF OOS 0.68 < 1.15
- GAGAL: PF in-sample 0.44 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.55 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 56 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 4 trade OOS (50.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 11 | 4 | 4 |
| Profit factor | 0.44 | 0.68 | 0.55 |
| Win rate | 28.4% | 25.0% | 25.0% |
| Expectancy (R) | -0.43 | -0.11 | -0.26 |
| Sharpe | -0.55 | -0.19 | -0.31 |
| Max DD | -5.5% | -2.2% | -2.3% |
| CAGR | -0.9% | -0.3% | -0.4% |

- Deflated Sharpe prob (n_trials=45): 0.01
- Timing vs entry acak: persentil 56 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.10 (harus < 0.5)
- Buy & hold jendela OOS: return -29.4%, Sharpe -0.29, maxDD -53.1% | strategi: return -0.8%, Sharpe -0.19, maxDD -2.2%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'donchian_n': 20, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'donchian_n': 20, 'rr': 1.5} | 0.48 | 0.00 | 1 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'donchian_n': 20, 'rr': 1.5} | 0.28 | 1.51 | 2 |
| 3 | 2019-09-20→2024-12-11 | 2024-12-12→2025-07-22 | {'donchian_n': 20, 'rr': 1.5} | 0.51 | 0.00 | 1 |
| 4 | 2020-04-06→2025-07-22 | 2025-07-23→2026-02-06 | {'donchian_n': 20, 'rr': 1.5} | 0.46 | 0.00 | 0 |
| 5 | 2020-11-02→2026-02-06 | 2026-02-09→2026-09-03 | {'donchian_n': 20, 'rr': 1.5} | 0.46 | 0.00 | 0 |