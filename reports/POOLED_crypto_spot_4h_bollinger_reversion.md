## Validasi bollinger_reversion @ POOLED_crypto_spot_4h

**Verdict: FIX**

- Gabungan 4 simbol: BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT
- PERINGATAN: deflated Sharpe prob 0.14 < 0.9

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 23 | 44 | 44 |
| Profit factor | 1.00 | 1.54 | 1.48 |
| Win rate | 57.4% | 65.9% | 0.0% |
| Expectancy (R) | -0.04 | 0.16 | 0.00 |
| Sharpe | -0.13 | 8.86 | 0.00 |
| Max DD | -4.7% | -0.8% | 0.0% |
| CAGR | -0.5% | 98.6% | 0.0% |

- Deflated Sharpe prob (n_trials=40): 0.14
- Timing vs entry acak: persentil 84 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.49 (harus < 0.5)
- Buy & hold jendela OOS: return -17.4%, Sharpe -0.33, maxDD -60.5% | strategi: return +1.4%, Sharpe 8.86, maxDD -0.8%
- Stabilitas parameter antar fold: 75%
- Monte Carlo max DD: median -0.7%, p95 -1.1%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|