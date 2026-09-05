## Validasi tsmom @ POOLED_crypto_spot_4h

**Verdict: SCRAP**

- Gabungan 4 simbol: BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT
- GAGAL: PF OOS gabungan 0.92 < 1.15
- GAGAL: degradasi IS→OOS 57% > 40%
- GAGAL: timing entry tidak lebih baik dari acak (rata-rata persentil 59 < 75)
- PERINGATAN: Sharpe OOS -0.79 < rata-rata buy&hold -0.33
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 28 | 91 | 91 |
| Profit factor | 2.12 | 0.92 | 1.04 |
| Win rate | 32.2% | 19.8% | 0.0% |
| Expectancy (R) | 0.48 | -0.03 | 0.00 |
| Sharpe | 1.01 | -0.79 | 0.00 |
| Max DD | -13.5% | -13.1% | 0.0% |
| CAGR | 13.7% | -35.0% | 0.0% |

- Deflated Sharpe prob (n_trials=30): 0.01
- Timing vs entry acak: persentil 59 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.42 (harus < 0.5)
- Buy & hold jendela OOS: return -17.4%, Sharpe -0.33, maxDD -60.5% | strategi: return -2.1%, Sharpe -0.79, maxDD -13.1%
- Stabilitas parameter antar fold: 55%
- Monte Carlo max DD: median -8.3%, p95 -11.9%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|