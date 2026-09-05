## Validasi donchian_breakout @ POOLED_crypto_spot_4h

**Verdict: SCRAP**

- Gabungan 1 simbol: BNB/USDT
- GAGAL: PF OOS gabungan 0.93 < 1.15
- GAGAL: degradasi IS→OOS 40% > 40%
- GAGAL: PF rata-rata dengan biaya x2 = 0.80 < 1
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9
- PERINGATAN: hanya 0/1 simbol profitable OOS: edge tidak merata

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 50 | 43 | 43 |
| Profit factor | 1.55 | 0.93 | 0.80 |
| Win rate | 40.2% | 30.2% | 0.0% |
| Expectancy (R) | 0.44 | 0.01 | 0.00 |
| Sharpe | 0.84 | -1.18 | 0.00 |
| Max DD | -5.9% | -6.0% | 0.0% |
| CAGR | 4.1% | -53.3% | 0.0% |

- Deflated Sharpe prob (n_trials=45): 0.01
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -7.4%, p95 -10.9%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|