## Validasi trend_pullback @ ANTM

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 11 < 30: belum cukup bukti
- GAGAL: PF OOS 0.85 < 1.15
- GAGAL: PF in-sample 0.87 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.73 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 68 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: Sharpe OOS -0.15 < buy&hold 0.68: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 11 trade OOS (27.3/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 18 | 11 | 11 |
| Profit factor | 0.87 | 0.85 | 0.73 |
| Win rate | 26.0% | 27.3% | 27.3% |
| Expectancy (R) | -0.06 | -0.06 | -0.12 |
| Sharpe | -0.15 | -0.15 | -0.31 |
| Max DD | -4.3% | -2.6% | -2.7% |
| CAGR | -0.2% | -0.3% | -0.5% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Timing vs entry acak: persentil 68 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.20 (harus < 0.5)
- Buy & hold jendela OOS: return +80.9%, Sharpe 0.68, maxDD -46.8% | strategi: return -0.7%, Sharpe -0.15, maxDD -2.6%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -3.0%, p95 -4.3%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 1.37 | 0.00 | 0 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 0.98 | 0.00 | 0 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 0.98 | 0.90 | 5 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.53 | 0.00 | 2 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.49 | 1.44 | 4 |