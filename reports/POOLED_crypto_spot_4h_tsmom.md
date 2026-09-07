## Validasi tsmom @ POOLED_crypto_spot_4h

**Verdict: SCRAP**

- Gabungan 4 simbol: BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT
- GAGAL: degradasi IS→OOS 41% > 40%
- GAGAL: 2/4 simbol gagal PBO atau tes acak: basket tidak boleh menutupi kegagalan mayoritas
- PERINGATAN: deflated Sharpe prob 0.06 < 0.9

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 32 | 94 | 94 |
| Profit factor | 2.12 | 1.26 | 1.19 |
| Win rate | 34.4% | 28.7% | 0.0% |
| Expectancy (R) | 0.47 | 0.13 | 0.00 |
| Sharpe | 0.99 | 0.29 | 0.00 |
| Max DD | -13.7% | -13.6% | 0.0% |
| CAGR | 13.9% | 1.9% | 0.0% |

- Deflated Sharpe prob (n_trials=30): 0.06
- Timing vs entry acak: persentil 84 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.41 (harus < 0.5)
- Buy & hold jendela OOS: return -19.6%, Sharpe -0.38, maxDD -60.5% | strategi: return +4.0%, Sharpe 0.29, maxDD -13.6%
- Stabilitas parameter antar fold: 70%
- Monte Carlo max DD: median -6.2%, p95 -9.7%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|