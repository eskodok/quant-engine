## Validasi donchian_breakout @ POOLED_idx_1d

**Verdict: SCRAP**

- Gabungan 11 simbol: BBCA, BBRI, BMRI, BBNI, TLKM, ASII, ICBP, INDF, ANTM, UNTR, PGAS
- GAGAL: PF OOS gabungan 0.77 < 1.15
- GAGAL: PF in-sample 0.77 < 1: OOS untung = kebetulan rezim, bukan edge
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9
- PERINGATAN: hanya 5/11 simbol profitable OOS: edge tidak merata

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 12 | 66 | 66 |
| Profit factor | 0.77 | 0.77 | inf |
| Win rate | 36.4% | 43.9% | 0.0% |
| Expectancy (R) | -0.22 | -0.14 | 0.00 |
| Sharpe | -0.23 | -1.89 | 0.00 |
| Max DD | -4.7% | -1.4% | 0.0% |
| CAGR | -0.4% | -3.1% | 0.0% |

- Deflated Sharpe prob (n_trials=45): 0.00
- Stabilitas parameter antar fold: 87%
- Monte Carlo max DD: median -1.3%, p95 -1.8%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|