## Validasi bollinger_reversion @ POOLED_crypto_spot_1d

**Verdict: SCRAP**

- Gabungan 4 simbol: BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT
- GAGAL: timing entry tidak lebih baik dari acak (rata-rata persentil 71 < 75)
- GAGAL: PBO rata-rata 0.51 >= 0.5: overfit
- PERINGATAN: deflated Sharpe prob 0.14 < 0.9

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 20 | 58 | 58 |
| Profit factor | 1.43 | 1.37 | 1.41 |
| Win rate | 62.9% | 63.8% | 0.0% |
| Expectancy (R) | 0.12 | 0.13 | 0.00 |
| Sharpe | 0.27 | 2.77 | 0.00 |
| Max DD | -3.4% | -1.5% | 0.0% |
| CAGR | 0.6% | 12.3% | 0.0% |

- Deflated Sharpe prob (n_trials=40): 0.14
- Timing vs entry acak: persentil 71 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.51 (harus < 0.5)
- Buy & hold jendela OOS: return +71.8%, Sharpe 0.50, maxDD -63.7% | strategi: return +1.9%, Sharpe 2.77, maxDD -1.5%
- Stabilitas parameter antar fold: 95%
- Monte Carlo max DD: median -1.2%, p95 -1.9%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|