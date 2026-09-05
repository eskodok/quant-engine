## Validasi trend_pullback @ INDF

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 10 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.33 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.82 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 10 trade OOS (30.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 16 | 10 | 10 |
| Profit factor | 0.33 | 1.27 | 0.82 |
| Win rate | 14.0% | 40.0% | 40.0% |
| Expectancy (R) | -0.43 | 0.07 | -0.07 |
| Sharpe | -0.67 | 0.15 | -0.14 |
| Max DD | -6.7% | -2.8% | -3.5% |
| CAGR | -1.0% | 0.2% | -0.2% |

- Deflated Sharpe prob (n_trials=135): 0.01
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -1.4%, p95 -2.2%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.01 | 0.00 | 0 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.00 | inf | 3 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 0.41 | 0.18 | 7 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.53 | 0.00 | 0 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 0.69 | 0.00 | 0 |