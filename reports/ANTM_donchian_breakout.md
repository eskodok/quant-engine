## Validasi donchian_breakout @ ANTM

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 9 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.68 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- PERINGATAN: PBO 0.49 agak tinggi
- PERINGATAN: Sharpe OOS 0.30 < buy&hold 0.68: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.04 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 9 trade OOS (22.2/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 10 | 9 | 9 |
| Profit factor | 0.68 | 1.38 | 1.20 |
| Win rate | 38.9% | 55.6% | 55.6% |
| Expectancy (R) | -0.17 | 0.17 | 0.10 |
| Sharpe | -0.27 | 0.30 | 0.17 |
| Max DD | -4.0% | -3.2% | -3.3% |
| CAGR | -0.4% | 0.6% | 0.3% |

- Deflated Sharpe prob (n_trials=45): 0.04
- Timing vs entry acak: persentil 94 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.49 (harus < 0.5)
- Buy & hold jendela OOS: return +80.9%, Sharpe 0.68, maxDD -46.8% | strategi: return +1.6%, Sharpe 0.30, maxDD -3.2%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -2.1%, p95 -3.3%
- Parameter terpilih (fold terakhir): {'donchian_n': 20, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'donchian_n': 20, 'rr': 1.5} | 0.56 | 0.00 | 0 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'donchian_n': 20, 'rr': 1.5} | 0.57 | 0.00 | 0 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'donchian_n': 20, 'rr': 1.5} | 0.57 | 2.86 | 4 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'donchian_n': 20, 'rr': 1.5} | 0.61 | 1.28 | 4 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'donchian_n': 20, 'rr': 1.5} | 1.09 | 0.00 | 1 |