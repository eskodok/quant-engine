## Validasi tsmom @ PGAS

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 12 < 30: belum cukup bukti
- GAGAL: PF OOS 0.76 < 1.15
- GAGAL: PF in-sample 0.59 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.61 < 1: edge habis dimakan biaya
- PERINGATAN: PBO 0.34 agak tinggi
- PERINGATAN: Sharpe OOS -0.16 < buy&hold 0.33: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 2 parameter untuk 12 trade OOS (16.7/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 10 | 12 | 12 |
| Profit factor | 0.59 | 0.76 | 0.61 |
| Win rate | 18.2% | 41.7% | 41.7% |
| Expectancy (R) | -0.25 | -0.09 | -0.17 |
| Sharpe | -0.16 | -0.16 | -0.31 |
| Max DD | -19.5% | -11.7% | -14.0% |
| CAGR | -1.5% | -2.0% | -3.5% |

- Deflated Sharpe prob (n_trials=30): 0.01
- Timing vs entry acak: persentil 98 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.34 (harus < 0.5)
- Buy & hold jendela OOS: return +16.2%, Sharpe 0.33, maxDD -44.3% | strategi: return -5.6%, Sharpe -0.16, maxDD -11.7%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -13.5%, p95 -18.2%
- Parameter terpilih (fold terakhir): {'lookback': 60, 'rebalance': 10}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-25 | 2023-10-26→2024-05-30 | {'lookback': 60, 'rebalance': 10} | 0.32 | 0.90 | 2 |
| 2 | 2019-03-13→2024-05-30 | 2024-05-31→2024-12-12 | {'lookback': 60, 'rebalance': 10} | 1.19 | 0.42 | 3 |
| 3 | 2019-09-20→2024-12-12 | 2024-12-13→2025-07-23 | {'lookback': 120, 'rebalance': 21} | 0.01 | 0.00 | 2 |
| 4 | 2020-04-06→2025-07-23 | 2025-07-24→2026-02-09 | {'lookback': 120, 'rebalance': 10} | 0.09 | 4.31 | 3 |
| 5 | 2020-11-02→2026-02-09 | 2026-02-10→2026-09-03 | {'lookback': 60, 'rebalance': 10} | 1.34 | 0.00 | 2 |