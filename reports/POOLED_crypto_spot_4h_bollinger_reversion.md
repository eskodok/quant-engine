## Validasi bollinger_reversion @ POOLED_crypto_spot_4h

**Verdict: FIX**

- Gabungan 1 simbol: BNB/USDT
- GAGAL: trade OOS gabungan 17 < 30
- PERINGATAN: deflated Sharpe prob 0.21 < 0.9

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 33 | 17 | 17 |
| Profit factor | 1.25 | 2.00 | 1.63 |
| Win rate | 61.0% | 70.6% | 0.0% |
| Expectancy (R) | 0.08 | 0.30 | 0.00 |
| Sharpe | 0.24 | 14.32 | 0.00 |
| Max DD | -5.0% | -1.9% | 0.0% |
| CAGR | 0.7% | 10028.2% | 0.0% |

- Deflated Sharpe prob (n_trials=40): 0.21
- Stabilitas parameter antar fold: 60%
- Monte Carlo max DD: median -1.6%, p95 -2.7%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|