## Validasi donchian_breakout @ ANTM

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 9 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.68 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- PERINGATAN: PBO 0.49 agak tinggi
- PERINGATAN: Sharpe OOS 0.30 < buy&hold 0.66: belum lebih baik dari sekadar memegang aset
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
- Timing vs entry acak: persentil 88 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.49 (harus < 0.5)
- Buy & hold jendela OOS: return +75.1%, Sharpe 0.66, maxDD -46.8% | strategi: return +1.6%, Sharpe 0.30, maxDD -3.2%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -2.1%, p95 -3.3%
- Parameter terpilih (fold terakhir): {'donchian_n': 20, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'donchian_n': 20, 'rr': 1.5} | 0.56 | 0.00 | 0 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'donchian_n': 20, 'rr': 1.5} | 0.57 | 0.00 | 0 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'donchian_n': 20, 'rr': 1.5} | 0.57 | 2.86 | 4 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'donchian_n': 20, 'rr': 1.5} | 0.61 | 1.28 | 4 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'donchian_n': 20, 'rr': 1.5} | 1.09 | 0.00 | 1 |