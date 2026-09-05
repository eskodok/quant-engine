## Validasi tsmom @ POOLED_crypto_spot_1d

**Verdict: SCRAP**

- Gabungan 4 simbol: BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT
- GAGAL: timing entry tidak lebih baik dari acak (rata-rata persentil 69 < 75)
- GAGAL: PBO rata-rata 0.74 >= 0.5: overfit
- PERINGATAN: deflated Sharpe prob 0.28 < 0.9

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 17 | 45 | 45 |
| Profit factor | 2.86 | 2.47 | 2.34 |
| Win rate | 33.7% | 37.8% | 0.0% |
| Expectancy (R) | 0.89 | 0.45 | 0.00 |
| Sharpe | 0.83 | 4.82 | 0.00 |
| Max DD | -21.1% | -6.5% | 0.0% |
| CAGR | 12.7% | 533.9% | 0.0% |

- Deflated Sharpe prob (n_trials=30): 0.28
- Timing vs entry acak: persentil 69 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.74 (harus < 0.5)
- Buy & hold jendela OOS: return +71.8%, Sharpe 0.50, maxDD -63.7% | strategi: return +29.2%, Sharpe 4.82, maxDD -6.5%
- Stabilitas parameter antar fold: 50%
- Monte Carlo max DD: median -4.5%, p95 -7.3%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|