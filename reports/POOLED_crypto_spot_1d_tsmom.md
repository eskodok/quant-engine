## Validasi tsmom @ POOLED_crypto_spot_1d

**Verdict: SCRAP**

- Gabungan 4 simbol: BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT
- GAGAL: timing entry tidak lebih baik dari acak (rata-rata persentil 61 < 75)
- GAGAL: PBO rata-rata 0.72 >= 0.5: overfit
- GAGAL: 4/4 simbol gagal PBO atau tes acak: basket tidak boleh menutupi kegagalan mayoritas
- PERINGATAN: deflated Sharpe prob 0.18 < 0.9

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 17 | 50 | 50 |
| Profit factor | 2.87 | 1.91 | 1.62 |
| Win rate | 33.6% | 32.0% | 0.0% |
| Expectancy (R) | 0.90 | 0.40 | 0.00 |
| Sharpe | 0.82 | 0.67 | 0.00 |
| Max DD | -20.8% | -14.6% | 0.0% |
| CAGR | 12.8% | 6.9% | 0.0% |

- Deflated Sharpe prob (n_trials=30): 0.18
- Timing vs entry acak: persentil 61 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.72 (harus < 0.5)
- Buy & hold jendela OOS: return +73.9%, Sharpe 0.51, maxDD -63.7% | strategi: return +24.5%, Sharpe 0.67, maxDD -14.6%
- Stabilitas parameter antar fold: 55%
- Monte Carlo max DD: median -7.0%, p95 -11.1%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|