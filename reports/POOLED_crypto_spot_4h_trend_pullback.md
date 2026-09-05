## Validasi trend_pullback @ POOLED_crypto_spot_4h

**Verdict: SCRAP**

- Gabungan 4 simbol: BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT
- GAGAL: PF OOS gabungan 0.87 < 1.15
- GAGAL: PF rata-rata dengan biaya x2 = 0.66 < 1
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 16 | 70 | 70 |
| Profit factor | 1.00 | 0.87 | 0.66 |
| Win rate | 30.4% | 28.6% | 0.0% |
| Expectancy (R) | 0.00 | -0.05 | 0.00 |
| Sharpe | -0.28 | -2.68 | 0.00 |
| Max DD | -3.2% | -1.7% | 0.0% |
| CAGR | -0.3% | -16.7% | 0.0% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Stabilitas parameter antar fold: 70%
- Monte Carlo max DD: median -1.5%, p95 -2.1%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|