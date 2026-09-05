## Validasi bollinger_reversion @ POOLED_idx_1d

**Verdict: SCRAP**

- Gabungan 12 simbol: BBCA, BBRI, BMRI, BBNI, TLKM, ASII, ICBP, INDF, KLBF, ANTM, UNTR, PGAS
- GAGAL: PF OOS gabungan 0.70 < 1.15
- GAGAL: degradasi IS→OOS 42% > 40%
- GAGAL: PF rata-rata dengan biaya x2 = 0.71 < 1
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9
- PERINGATAN: hanya 3/12 simbol profitable OOS: edge tidak merata

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 14 | 82 | 82 |
| Profit factor | 1.22 | 0.70 | 0.71 |
| Win rate | 59.4% | 51.2% | 0.0% |
| Expectancy (R) | 0.04 | -0.35 | 0.00 |
| Sharpe | 0.09 | -2.54 | 0.00 |
| Max DD | -3.3% | -1.4% | 0.0% |
| CAGR | 0.1% | -3.0% | 0.0% |

- Deflated Sharpe prob (n_trials=40): 0.00
- Stabilitas parameter antar fold: 95%
- Monte Carlo max DD: median -1.3%, p95 -1.7%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|