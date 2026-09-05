## Validasi trend_pullback @ ICBP

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 6 < 30: belum cukup bukti
- GAGAL: PF OOS 0.00 < 1.15
- GAGAL: PF in-sample 0.00 < 1: optimasi pun tidak menemukan parameter untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.00 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 0 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: PBO 0.46 agak tinggi
- PERINGATAN: Sharpe OOS -1.15 < buy&hold -0.29: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 6 trade OOS (50.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 20 | 6 | 6 |
| Profit factor | 0.00 | 0.00 | 0.00 |
| Win rate | 0.0% | 0.0% | 0.0% |
| Expectancy (R) | -0.66 | -0.78 | -0.91 |
| Sharpe | -1.39 | -1.15 | -1.25 |
| Max DD | -10.9% | -3.8% | -4.7% |
| CAGR | -2.2% | -1.4% | -1.7% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Timing vs entry acak: persentil 0 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.46 (harus < 0.5)
- Buy & hold jendela OOS: return -29.4%, Sharpe -0.29, maxDD -53.1% | strategi: return -3.8%, Sharpe -1.15, maxDD -3.8%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -3.9%, p95 -3.9%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-04→2023-10-24 | 2023-10-25→2024-05-29 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.00 | 0.00 | 4 |
| 2 | 2019-03-13→2024-05-29 | 2024-05-30→2024-12-11 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.00 | 0.00 | 2 |
| 3 | 2019-09-20→2024-12-11 | 2024-12-12→2025-07-22 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.00 | 0.00 | 0 |
| 4 | 2020-04-06→2025-07-22 | 2025-07-23→2026-02-06 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.00 | 0.00 | 0 |
| 5 | 2020-11-02→2026-02-06 | 2026-02-09→2026-09-03 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.00 | 0.00 | 0 |