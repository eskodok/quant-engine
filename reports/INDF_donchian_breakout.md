## Validasi donchian_breakout @ INDF

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 8 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.71 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.92 < 1: edge habis dimakan biaya
- PERINGATAN: PBO 0.30 agak tinggi
- PERINGATAN: Sharpe OOS 0.13 < buy&hold 0.21: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.02 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 8 trade OOS (25.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 7 | 8 | 8 |
| Profit factor | 0.71 | 1.17 | 0.92 |
| Win rate | 35.2% | 50.0% | 50.0% |
| Expectancy (R) | -0.22 | 0.14 | -0.03 |
| Sharpe | -0.18 | 0.13 | -0.06 |
| Max DD | -2.9% | -3.2% | -3.5% |
| CAGR | -0.2% | 0.2% | -0.2% |

- Deflated Sharpe prob (n_trials=45): 0.02
- Timing vs entry acak: persentil 85 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.30 (harus < 0.5)
- Buy & hold jendela OOS: return +6.3%, Sharpe 0.21, maxDD -30.8% | strategi: return +0.7%, Sharpe 0.13, maxDD -3.2%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -2.2%, p95 -4.1%
- Parameter terpilih (fold terakhir): {'donchian_n': 20, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'donchian_n': 20, 'rr': 1.5} | 0.26 | 0.00 | 0 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'donchian_n': 20, 'rr': 1.5} | 0.38 | 3.32 | 4 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'donchian_n': 20, 'rr': 1.5} | 1.10 | 1.27 | 2 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'donchian_n': 20, 'rr': 1.5} | 1.00 | 0.00 | 1 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'donchian_n': 20, 'rr': 1.5} | 0.83 | 0.00 | 1 |