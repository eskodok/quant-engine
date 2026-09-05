## Validasi rsi2_reversion @ POOLED_crypto_spot_4h

**Verdict: SCRAP**

- Gabungan 1 simbol: BNB/USDT
- GAGAL: PF OOS gabungan 0.70 < 1.15
- GAGAL: PF rata-rata dengan biaya x2 = 0.44 < 1
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9
- PERINGATAN: hanya 0/1 simbol profitable OOS: edge tidak merata

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 121 | 86 | 86 |
| Profit factor | 1.05 | 0.70 | 0.44 |
| Win rate | 67.8% | 61.6% | 0.0% |
| Expectancy (R) | -0.00 | -0.08 | 0.00 |
| Sharpe | 0.08 | -5.98 | 0.00 |
| Max DD | -5.8% | -6.1% | 0.0% |
| CAGR | 0.2% | -73.1% | 0.0% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -6.9%, p95 -9.0%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|