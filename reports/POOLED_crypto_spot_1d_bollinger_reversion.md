## Validasi bollinger_reversion @ POOLED_crypto_spot_1d

**Verdict: SCRAP**

- Gabungan 4 simbol: BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT
- GAGAL: 3/4 simbol gagal PBO atau tes acak: basket tidak boleh menutupi kegagalan mayoritas
- PERINGATAN: Sharpe OOS 0.50 < rata-rata buy&hold 0.51
- PERINGATAN: deflated Sharpe prob 0.17 < 0.9

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 20 | 57 | 57 |
| Profit factor | 1.46 | 1.42 | 1.44 |
| Win rate | 63.2% | 63.2% | 0.0% |
| Expectancy (R) | 0.13 | 0.15 | 0.00 |
| Sharpe | 0.29 | 0.50 | 0.00 |
| Max DD | -3.4% | -1.6% | 0.0% |
| CAGR | 0.6% | 0.6% | 0.0% |

- Deflated Sharpe prob (n_trials=40): 0.17
- Timing vs entry acak: persentil 75 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.50 (harus < 0.5)
- Buy & hold jendela OOS: return +73.9%, Sharpe 0.51, maxDD -63.7% | strategi: return +2.1%, Sharpe 0.50, maxDD -1.6%
- Stabilitas parameter antar fold: 100%
- Monte Carlo max DD: median -1.1%, p95 -1.9%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|