## Validasi trend_pullback @ AKRA

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 4 < 30: belum cukup bukti
- GAGAL: PF OOS 1.03 < 1.15
- GAGAL: degradasi IS→OOS 51% > 40%: indikasi overfit
- GAGAL: PF OOS dengan biaya x2.0 = 0.79 < 1: edge habis dimakan biaya
- PERINGATAN: PBO 0.43 agak tinggi
- PERINGATAN: Sharpe OOS 0.02 < buy&hold 0.20: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 4 trade OOS (75.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 16 | 4 | 4 |
| Profit factor | 2.11 | 1.03 | 0.79 |
| Win rate | 40.5% | 25.0% | 25.0% |
| Expectancy (R) | 0.35 | 0.02 | -0.10 |
| Sharpe | 0.40 | 0.02 | -0.10 |
| Max DD | -2.5% | -2.7% | -2.8% |
| CAGR | 0.9% | 0.0% | -0.1% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Timing vs entry acak: persentil 76 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.43 (harus < 0.5)
- Buy & hold jendela OOS: return +0.7%, Sharpe 0.20, maxDD -51.4% | strategi: return +0.1%, Sharpe 0.02, maxDD -2.7%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 1.30 | 1.20 | 3 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0} | 2.33 | 0.00 | 0 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0} | 2.33 | 0.00 | 0 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 3.0} | 2.66 | 0.00 | 1 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-07 | {'rsi_pb': 40.0, 'adx_min': 20.0, 'rr': 1.5} | 1.94 | 0.00 | 0 |