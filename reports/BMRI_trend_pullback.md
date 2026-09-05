## Validasi trend_pullback @ BMRI

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 9 < 30: belum cukup bukti
- GAGAL: PF OOS 0.24 < 1.15
- GAGAL: PF in-sample 0.69 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- GAGAL: degradasi IS→OOS 65% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.18 < 1: edge habis dimakan biaya
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 9 trade OOS (33.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 18 | 9 | 9 |
| Profit factor | 0.69 | 0.24 | 0.18 |
| Win rate | 33.6% | 11.1% | 11.1% |
| Expectancy (R) | -0.12 | -0.48 | -0.61 |
| Sharpe | -0.24 | -1.03 | -1.27 |
| Max DD | -4.2% | -4.6% | -5.0% |
| CAGR | -0.4% | -1.5% | -1.8% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -4.3%, p95 -5.4%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.59 | 0.30 | 8 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 0.74 | 0.00 | 0 |
| 3 | 2019-09-19→2024-12-11 | 2024-12-12→2025-07-22 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 0.84 | 0.00 | 0 |
| 4 | 2020-04-03→2025-07-22 | 2025-07-23→2026-02-06 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 0.60 | 0.00 | 0 |
| 5 | 2020-10-27→2026-02-06 | 2026-02-09→2026-09-02 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.68 | 0.00 | 1 |