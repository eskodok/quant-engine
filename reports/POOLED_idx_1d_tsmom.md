## Validasi tsmom @ POOLED_idx_1d

**Verdict: SCRAP**

- Gabungan 12 simbol: BBCA, BBRI, BMRI, BBNI, TLKM, ASII, ICBP, INDF, KLBF, ANTM, UNTR, PGAS
- GAGAL: PF OOS gabungan 0.70 < 1.15
- GAGAL: PF in-sample 0.75 < 1: OOS untung = kebetulan rezim, bukan edge
- GAGAL: PF rata-rata dengan biaya x2 = 0.47 < 1
- GAGAL: timing entry tidak lebih baik dari acak (rata-rata persentil 54 < 75)
- PERINGATAN: Sharpe OOS -1.65 < rata-rata buy&hold -0.04
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9
- PERINGATAN: hanya 3/12 simbol profitable OOS: edge tidak merata

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 13 | 83 | 83 |
| Profit factor | 0.75 | 0.70 | 0.47 |
| Win rate | 20.2% | 24.1% | 0.0% |
| Expectancy (R) | -0.12 | -0.13 | 0.00 |
| Sharpe | -0.13 | -1.65 | 0.00 |
| Max DD | -21.3% | -6.0% | 0.0% |
| CAGR | -1.4% | -11.8% | 0.0% |

- Deflated Sharpe prob (n_trials=30): 0.01
- Timing vs entry acak: persentil 54 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.38 (harus < 0.5)
- Buy & hold jendela OOS: return -11.2%, Sharpe -0.04, maxDD -48.1% | strategi: return -4.6%, Sharpe -1.65, maxDD -6.0%
- Stabilitas parameter antar fold: 70%
- Monte Carlo max DD: median -6.3%, p95 -8.5%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|