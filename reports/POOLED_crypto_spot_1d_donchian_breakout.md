## Validasi donchian_breakout @ POOLED_crypto_spot_1d

**Verdict: SCRAP**

- Gabungan 4 simbol: BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT
- GAGAL: degradasi IS→OOS 57% > 40%
- GAGAL: timing entry tidak lebih baik dari acak (rata-rata persentil 42 < 75)
- GAGAL: PBO rata-rata 0.70 >= 0.5: overfit
- PERINGATAN: deflated Sharpe prob 0.05 < 0.9

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 19 | 48 | 48 |
| Profit factor | 2.87 | 1.24 | 1.18 |
| Win rate | 53.6% | 35.4% | 0.0% |
| Expectancy (R) | 0.75 | 0.16 | 0.00 |
| Sharpe | 0.89 | 1.82 | 0.00 |
| Max DD | -3.5% | -2.1% | 0.0% |
| CAGR | 2.9% | 14.9% | 0.0% |

- Deflated Sharpe prob (n_trials=45): 0.05
- Timing vs entry acak: persentil 42 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.70 (harus < 0.5)
- Buy & hold jendela OOS: return +71.8%, Sharpe 0.50, maxDD -63.7% | strategi: return +1.9%, Sharpe 1.82, maxDD -2.1%
- Stabilitas parameter antar fold: 75%
- Monte Carlo max DD: median -2.1%, p95 -3.3%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|