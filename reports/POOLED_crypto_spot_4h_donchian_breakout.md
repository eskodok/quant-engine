## Validasi donchian_breakout @ POOLED_crypto_spot_4h

**Verdict: SCRAP**

- Gabungan 4 simbol: BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT
- GAGAL: PF OOS gabungan 0.83 < 1.15
- GAGAL: degradasi IS→OOS 44% > 40%
- GAGAL: PF rata-rata dengan biaya x2 = 0.67 < 1
- GAGAL: timing entry tidak lebih baik dari acak (rata-rata persentil 64 < 75)
- GAGAL: 3/4 simbol gagal PBO atau tes acak: basket tidak boleh menutupi kegagalan mayoritas
- PERINGATAN: Sharpe OOS -0.44 < rata-rata buy&hold -0.33
- PERINGATAN: deflated Sharpe prob 0.01 < 0.9
- PERINGATAN: hanya 0/4 simbol profitable OOS: edge tidak merata

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 31 | 74 | 74 |
| Profit factor | 1.47 | 0.83 | 0.67 |
| Win rate | 39.5% | 28.4% | 0.0% |
| Expectancy (R) | 0.30 | -0.05 | 0.00 |
| Sharpe | 0.78 | -0.44 | 0.00 |
| Max DD | -4.5% | -3.7% | 0.0% |
| CAGR | 3.6% | -0.8% | 0.0% |

- Deflated Sharpe prob (n_trials=45): 0.01
- Timing vs entry acak: persentil 64 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.35 (harus < 0.5)
- Buy & hold jendela OOS: return -17.4%, Sharpe -0.33, maxDD -60.5% | strategi: return -1.7%, Sharpe -0.44, maxDD -3.7%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -3.0%, p95 -4.3%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|