## Validasi donchian_breakout @ TPIA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 10 < 30: belum cukup bukti
- GAGAL: timing entry tidak lebih baik dari acak (persentil 66 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: deflated Sharpe prob 0.04 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 10 trade OOS (20.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 15 | 10 | 10 |
| Profit factor | 1.79 | 1.44 | 1.24 |
| Win rate | 52.9% | 60.0% | 60.0% |
| Expectancy (R) | 0.31 | 0.18 | 0.10 |
| Sharpe | 0.48 | 0.27 | 0.16 |
| Max DD | -3.0% | -2.5% | -2.6% |
| CAGR | 1.0% | 0.6% | 0.4% |

- Deflated Sharpe prob (n_trials=45): 0.04
- Timing vs entry acak: persentil 66 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.19 (harus < 0.5)
- Buy & hold jendela OOS: return -30.0%, Sharpe 0.22, maxDD -87.7% | strategi: return +1.8%, Sharpe 0.27, maxDD -2.5%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -2.1%, p95 -3.1%
- Parameter terpilih (fold terakhir): {'donchian_n': 20, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'donchian_n': 20, 'rr': 1.5} | 2.44 | 2.30 | 6 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'donchian_n': 20, 'rr': 1.5} | 2.05 | 0.50 | 3 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'donchian_n': 20, 'rr': 3.0} | 1.64 | inf | 1 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'donchian_n': 20, 'rr': 2.0} | 1.35 | 0.00 | 0 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-07 | {'donchian_n': 20, 'rr': 1.5} | 1.46 | 0.00 | 0 |