## Validasi trend_pullback @ POOLED_idx_1d

**Verdict: SCRAP**

- Gabungan 4 simbol: BBCA, BMRI, TLKM, ASII
- GAGAL: trade OOS gabungan 16 < 30
- GAGAL: PF OOS gabungan 0.47 < 1.15
- GAGAL: PF rata-rata dengan biaya x2 = 0.31 < 1
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9
- PERINGATAN: hanya 1/4 simbol profitable OOS: edge tidak merata

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 13 | 16 | 16 |
| Profit factor | 0.74 | 0.47 | 0.31 |
| Win rate | 26.3% | 25.0% | 0.0% |
| Expectancy (R) | -0.10 | -0.20 | 0.00 |
| Sharpe | -0.24 | -4.71 | 0.00 |
| Max DD | -3.2% | -0.9% | 0.0% |
| CAGR | -0.3% | -12.5% | 0.0% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Stabilitas parameter antar fold: 75%
- Monte Carlo max DD: median -1.2%, p95 -1.5%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|