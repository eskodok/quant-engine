## Validasi rsi2_reversion @ POOLED_crypto_spot_1d

**Verdict: SCRAP**

- Gabungan 4 simbol: BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT
- GAGAL: PF OOS gabungan 0.90 < 1.15
- GAGAL: PF rata-rata dengan biaya x2 = 0.74 < 1
- GAGAL: timing entry tidak lebih baik dari acak (rata-rata persentil 54 < 75)
- GAGAL: PBO rata-rata 0.71 >= 0.5: overfit
- PERINGATAN: Sharpe OOS -0.79 < rata-rata buy&hold 0.50
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9
- PERINGATAN: hanya 1/4 simbol profitable OOS: edge tidak merata

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 41 | 123 | 123 |
| Profit factor | 1.34 | 0.90 | 0.74 |
| Win rate | 71.8% | 64.2% | 0.0% |
| Expectancy (R) | 0.04 | -0.02 | 0.00 |
| Sharpe | 0.23 | -0.79 | 0.00 |
| Max DD | -2.6% | -2.0% | 0.0% |
| CAGR | 0.4% | -2.0% | 0.0% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 54 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.71 (harus < 0.5)
- Buy & hold jendela OOS: return +71.8%, Sharpe 0.50, maxDD -63.7% | strategi: return -0.7%, Sharpe -0.79, maxDD -2.0%
- Stabilitas parameter antar fold: 65%
- Monte Carlo max DD: median -1.8%, p95 -2.5%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|