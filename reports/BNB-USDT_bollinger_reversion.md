## Validasi bollinger_reversion @ BNB/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- GAGAL: trade OOS 10 < 30: belum cukup bukti
- GAGAL: PF OOS 0.95 < 1.15
- GAGAL: PF OOS dengan biaya x2.0 = 0.89 < 1: edge habis dimakan biaya
- GAGAL: timing entry tidak lebih baik dari acak (persentil 52 < 75): hasil = arus pasar, bukan sinyal
- PERINGATAN: Sharpe OOS -0.05 < buy&hold 0.85: belum lebih baik dari sekadar memegang aset
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9: Sharpe bisa hasil kebetulan
- PERINGATAN: 3 parameter untuk 10 trade OOS (30.0/100 trade)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 17 | 10 | 10 |
| Profit factor | 1.27 | 0.95 | 0.89 |
| Win rate | 57.5% | 40.0% | 40.0% |
| Expectancy (R) | 0.11 | -0.02 | -0.06 |
| Sharpe | 0.22 | -0.05 | -0.12 |
| Max DD | -3.9% | -3.7% | -3.9% |
| CAGR | 0.4% | -0.1% | -0.2% |

- Deflated Sharpe prob (n_trials=40): 0.01
- Timing vs entry acak: persentil 52 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.21 (harus < 0.5)
- Buy & hold jendela OOS: return +126.0%, Sharpe 0.85, maxDD -58.2% | strategi: return -0.3%, Sharpe -0.05, maxDD -3.7%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -3.1%, p95 -4.5%
- Parameter terpilih (fold terakhir): {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 0}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|
| 1 | 2019-06-19→2024-01-25 | 2024-01-26→2024-08-02 | {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 0} | 1.25 | 1.67 | 2 |
| 2 | 2019-12-26→2024-08-02 | 2024-08-03→2025-02-08 | {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 0} | 1.43 | 1.18 | 5 |
| 3 | 2020-07-03→2025-02-08 | 2025-02-09→2025-08-17 | {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 0} | 1.21 | inf | 1 |
| 4 | 2021-01-09→2025-08-17 | 2025-08-18→2026-02-23 | {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 0} | 1.36 | 0.00 | 2 |
| 5 | 2021-07-18→2026-02-23 | 2026-02-24→2026-09-01 | {'bb_n': 30, 'bb_k': 2.0, 'need_trend': 0} | 1.09 | 0.00 | 0 |