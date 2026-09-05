## Validasi trend_pullback @ POOLED_crypto_spot_1d

**Verdict: SCRAP**

- Gabungan 4 simbol: BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT
- GAGAL: timing entry tidak lebih baik dari acak (rata-rata persentil 63 < 75)
- GAGAL: PBO rata-rata 0.74 >= 0.5: overfit
- PERINGATAN: deflated Sharpe prob 0.05 < 0.9

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 25 | 73 | 73 |
| Profit factor | 2.13 | 1.44 | 1.57 |
| Win rate | 34.6% | 32.9% | 0.0% |
| Expectancy (R) | 0.32 | 0.16 | 0.00 |
| Sharpe | 0.68 | 2.42 | 0.00 |
| Max DD | -3.7% | -2.5% | 0.0% |
| CAGR | 1.7% | 14.3% | 0.0% |

- Deflated Sharpe prob (n_trials=135): 0.05
- Timing vs entry acak: persentil 63 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.74 (harus < 0.5)
- Buy & hold jendela OOS: return +71.8%, Sharpe 0.50, maxDD -63.7% | strategi: return +2.8%, Sharpe 2.42, maxDD -2.5%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -1.6%, p95 -2.5%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|