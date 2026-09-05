## Validasi rsi2_reversion @ POOLED_idx_1d

**Verdict: SCRAP**

- Gabungan 12 simbol: BBCA, BBRI, BMRI, BBNI, TLKM, ASII, ICBP, INDF, KLBF, ANTM, UNTR, PGAS
- GAGAL: PF OOS gabungan 0.69 < 1.15
- GAGAL: degradasi IS→OOS 70% > 40%
- GAGAL: PF rata-rata dengan biaya x2 = 0.56 < 1
- GAGAL: timing entry tidak lebih baik dari acak (rata-rata persentil 68 < 75)
- PERINGATAN: Sharpe OOS -2.22 < rata-rata buy&hold -0.04
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9
- PERINGATAN: hanya 3/12 simbol profitable OOS: edge tidak merata

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 24 | 139 | 139 |
| Profit factor | 2.32 | 0.69 | 0.56 |
| Win rate | 63.0% | 56.8% | 0.0% |
| Expectancy (R) | 0.08 | -0.09 | 0.00 |
| Sharpe | 0.21 | -2.22 | 0.00 |
| Max DD | -2.6% | -1.0% | 0.0% |
| CAGR | 0.3% | -1.6% | 0.0% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 68 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.39 (harus < 0.5)
- Buy & hold jendela OOS: return -11.2%, Sharpe -0.04, maxDD -48.1% | strategi: return -0.9%, Sharpe -2.22, maxDD -1.0%
- Stabilitas parameter antar fold: 72%
- Monte Carlo max DD: median -1.1%, p95 -1.4%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|