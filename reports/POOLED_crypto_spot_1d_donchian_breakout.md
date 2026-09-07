## Validasi donchian_breakout @ POOLED_crypto_spot_1d

**Verdict: SCRAP**

- Gabungan 4 simbol: BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT
- GAGAL: degradasi IS→OOS 55% > 40%
- GAGAL: timing entry tidak lebih baik dari acak (rata-rata persentil 41 < 75)
- GAGAL: PBO rata-rata 0.70 >= 0.5: overfit
- GAGAL: 3/4 simbol gagal PBO atau tes acak: basket tidak boleh menutupi kegagalan mayoritas
- PERINGATAN: Sharpe OOS 0.39 < rata-rata buy&hold 0.51
- PERINGATAN: deflated Sharpe prob 0.06 < 0.9

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 19 | 48 | 48 |
| Profit factor | 2.82 | 1.27 | 1.18 |
| Win rate | 52.7% | 35.4% | 0.0% |
| Expectancy (R) | 0.73 | 0.17 | 0.00 |
| Sharpe | 0.88 | 0.39 | 0.00 |
| Max DD | -3.5% | -2.3% | 0.0% |
| CAGR | 2.9% | 0.6% | 0.0% |

- Deflated Sharpe prob (n_trials=45): 0.06
- Timing vs entry acak: persentil 41 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.70 (harus < 0.5)
- Buy & hold jendela OOS: return +73.9%, Sharpe 0.51, maxDD -63.7% | strategi: return +2.1%, Sharpe 0.39, maxDD -2.3%
- Stabilitas parameter antar fold: 75%
- Monte Carlo max DD: median -2.1%, p95 -3.3%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|