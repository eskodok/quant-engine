## Validasi donchian_breakout @ MAPI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 4 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.50 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- PERINGATAN: PBO 0.44 agak tinggi
- PERINGATAN: deflated Sharpe prob 0.04 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 4 trade OOS (50.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 13 | 4 | 4 |
| Profit factor | 0.50 | 2.03 | 1.63 |
| Win rate | 22.8% | 50.0% | 50.0% |
| Expectancy (R) | -0.31 | 0.32 | 0.22 |
| Sharpe | -0.42 | 0.35 | 0.25 |
| Max DD | -5.1% | -1.1% | -1.1% |
| CAGR | -0.8% | 0.5% | 0.3% |

- Deflated Sharpe prob (n_trials=45): 0.04
- Timing vs entry acak: persentil 98 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.44 (harus < 0.5)
- Buy & hold jendela OOS: return -20.8%, Sharpe 0.06, maxDD -46.0% | strategi: return +1.3%, Sharpe 0.35, maxDD -1.1%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'donchian_n': 20, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-27 | 2023-10-30→2024-06-03 | {'donchian_n': 20, 'rr': 1.5} | 0.42 | inf | 1 |
| 2 | 2019-03-18→2024-06-03 | 2024-06-04→2024-12-16 | {'donchian_n': 20, 'rr': 1.5} | 0.51 | 0.00 | 0 |
| 3 | 2019-09-25→2024-12-16 | 2024-12-17→2025-07-25 | {'donchian_n': 20, 'rr': 1.5} | 0.51 | 0.00 | 0 |
| 4 | 2020-04-09→2025-07-25 | 2025-07-28→2026-02-11 | {'donchian_n': 20, 'rr': 1.5} | 0.51 | 0.00 | 0 |
| 5 | 2020-11-05→2026-02-11 | 2026-02-12→2026-09-07 | {'donchian_n': 20, 'rr': 1.5} | 0.57 | 1.08 | 3 |