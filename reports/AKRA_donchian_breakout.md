## Validasi donchian_breakout @ AKRA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 5 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.88 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- PERINGATAN: PBO 0.46 agak tinggi
- PERINGATAN: Sharpe OOS 0.14 < buy&hold 0.20: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.02 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 5 trade OOS (40.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 15 | 5 | 5 |
| Profit factor | 0.88 | 1.38 | 1.05 |
| Win rate | 35.7% | 40.0% | 40.0% |
| Expectancy (R) | -0.08 | 0.14 | 0.02 |
| Sharpe | -0.11 | 0.14 | 0.03 |
| Max DD | -6.1% | -2.2% | -2.4% |
| CAGR | -0.3% | 0.2% | 0.0% |

- Deflated Sharpe prob (n_trials=45): 0.02
- Timing vs entry acak: persentil 96 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.46 (harus < 0.5)
- Buy & hold jendela OOS: return +0.7%, Sharpe 0.20, maxDD -51.4% | strategi: return +0.7%, Sharpe 0.14, maxDD -2.2%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -1.7%, p95 -1.9%
- Parameter terpilih (fold terakhir): {'donchian_n': 20, 'rr': 3.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'donchian_n': 40, 'rr': 1.5} | 0.61 | inf | 2 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'donchian_n': 40, 'rr': 1.5} | 0.94 | 0.00 | 0 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'donchian_n': 40, 'rr': 1.5} | 0.84 | 0.00 | 0 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'donchian_n': 20, 'rr': 3.0} | 1.17 | 0.00 | 1 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-07 | {'donchian_n': 20, 'rr': 3.0} | 0.82 | 0.00 | 2 |