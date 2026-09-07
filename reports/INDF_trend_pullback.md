## Validasi trend_pullback @ INDF

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 10 < 30: belum cukup bukti
- GAGAL: PF in-sample 0.34 < 1.1: optimasi pun tidak menemukan parameter yang jelas untung -> hasil OOS = kebetulan
- GAGAL: PF OOS dengan biaya x2.0 = 0.90 < 1: edge habis dimakan biaya
- PERINGATAN: Sharpe OOS 0.21 < buy&hold 0.22: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 10 trade OOS (30.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 16 | 10 | 10 |
| Profit factor | 0.34 | 1.38 | 0.90 |
| Win rate | 14.0% | 40.0% | 40.0% |
| Expectancy (R) | -0.43 | 0.10 | -0.04 |
| Sharpe | -0.67 | 0.21 | -0.08 |
| Max DD | -6.7% | -2.8% | -3.5% |
| CAGR | -1.0% | 0.3% | -0.1% |

- Deflated Sharpe prob (n_trials=135): 0.01
- Timing vs entry acak: persentil 93 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.03 (harus < 0.5)
- Buy & hold jendela OOS: return +7.0%, Sharpe 0.22, maxDD -30.8% | strategi: return +0.9%, Sharpe 0.21, maxDD -2.8%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -1.4%, p95 -2.2%
- Parameter terpilih (fold terakhir): {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2018-09-07→2023-10-26 | 2023-10-27→2024-05-31 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.01 | 0.00 | 0 |
| 2 | 2019-03-18→2024-05-31 | 2024-06-03→2024-12-13 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.00 | inf | 3 |
| 3 | 2019-09-24→2024-12-13 | 2024-12-16→2025-07-24 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 3.0} | 0.40 | 0.28 | 7 |
| 4 | 2020-04-08→2025-07-24 | 2025-07-25→2026-02-10 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 1.5} | 0.57 | 0.00 | 0 |
| 5 | 2020-11-04→2026-02-10 | 2026-02-11→2026-09-04 | {'rsi_pb': 40.0, 'adx_min': 15.0, 'rr': 2.0} | 0.69 | 0.00 | 0 |