## Validasi rsi2_reversion @ POOLED_crypto_spot_1d

**Verdict: SCRAP**

- Gabungan 4 simbol: BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT
- GAGAL: PF OOS gabungan 0.86 < 1.15
- GAGAL: PF rata-rata dengan biaya x2 = 0.73 < 1
- GAGAL: timing entry tidak lebih baik dari acak (rata-rata persentil 46 < 75)
- GAGAL: PBO rata-rata 0.74 >= 0.5: overfit
- GAGAL: 4/4 simbol gagal PBO atau tes acak: basket tidak boleh menutupi kegagalan mayoritas
- PERINGATAN: Sharpe OOS -0.24 < rata-rata buy&hold 0.51
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9
- PERINGATAN: hanya 0/4 simbol profitable OOS: edge tidak merata

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 41 | 121 | 121 |
| Profit factor | 1.35 | 0.86 | 0.73 |
| Win rate | 71.8% | 63.6% | 0.0% |
| Expectancy (R) | 0.04 | -0.03 | 0.00 |
| Sharpe | 0.23 | -0.24 | 0.00 |
| Max DD | -2.6% | -2.2% | 0.0% |
| CAGR | 0.4% | -0.3% | 0.0% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 46 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.74 (harus < 0.5)
- Buy & hold jendela OOS: return +73.9%, Sharpe 0.51, maxDD -63.7% | strategi: return -0.9%, Sharpe -0.24, maxDD -2.2%
- Stabilitas parameter antar fold: 65%
- Monte Carlo max DD: median -1.8%, p95 -2.6%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|