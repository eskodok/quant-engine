## Validasi rsi2_reversion @ ETH/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 20 < 30: belum cukup bukti
- GAGAL: PF OOS 0.88 < 1.15
- GAGAL: PF OOS dengan biaya x2.0 = 0.76 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 47 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: PBO 0.43 agak tinggi
- PERINGATAN: Sharpe OOS -0.10 < buy&hold 0.43: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 20 trade OOS (15.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 25 | 20 | 20 |
| Profit factor | 1.41 | 0.88 | 0.76 |
| Win rate | 72.1% | 60.0% | 60.0% |
| Expectancy (R) | 0.04 | -0.02 | -0.05 |
| Sharpe | 0.17 | -0.10 | -0.21 |
| Max DD | -2.0% | -2.4% | -2.8% |
| CAGR | 0.2% | -0.2% | -0.3% |

- Deflated Sharpe prob (n_trials=60): 0.01
- Timing vs entry acak: persentil 47 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.43 (harus < 0.5)
- Buy & hold jendela OOS: return +26.9%, Sharpe 0.43, maxDD -67.5% | strategi: return -0.5%, Sharpe -0.10, maxDD -2.4%
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -2.2%, p95 -3.2%
- Parameter terpilih (fold terakhir): {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 1}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2017-11-09→2023-06-05 | 2023-06-06→2024-01-28 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 1} | 1.44 | 0.24 | 6 |
| 2 | 2018-07-10→2024-01-28 | 2024-01-29→2024-09-21 | {'rsi_buy': 10.0, 'exit_ema': 10, 'need_trend': 1} | 1.20 | 0.61 | 9 |
| 3 | 2019-03-04→2024-09-21 | 2024-09-22→2025-05-16 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 1} | 1.13 | inf | 2 |
| 4 | 2019-10-27→2025-05-16 | 2025-05-17→2026-01-08 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 1} | 1.53 | 7.42 | 3 |
| 5 | 2020-06-20→2026-01-08 | 2026-01-09→2026-09-02 | {'rsi_buy': 5.0, 'exit_ema': 10, 'need_trend': 1} | 1.76 | 0.00 | 0 |