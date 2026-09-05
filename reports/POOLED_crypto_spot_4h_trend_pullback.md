## Validasi trend_pullback @ POOLED_crypto_spot_4h

**Verdict: SCRAP**

- Gabungan 1 simbol: BNB/USDT
- GAGAL: PF OOS gabungan 0.50 < 1.15
- GAGAL: degradasi IS→OOS 51% > 40%
- GAGAL: PF rata-rata dengan biaya x2 = 0.40 < 1
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9
- PERINGATAN: hanya 0/1 simbol profitable OOS: edge tidak merata

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 54 | 36 | 36 |
| Profit factor | 1.01 | 0.50 | 0.40 |
| Win rate | 24.9% | 16.7% | 0.0% |
| Expectancy (R) | 0.03 | -0.12 | 0.00 |
| Sharpe | 0.04 | -11.39 | 0.00 |
| Max DD | -6.5% | -6.1% | 0.0% |
| CAGR | 0.1% | -97.5% | 0.0% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -7.4%, p95 -9.5%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|