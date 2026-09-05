## Validasi trend_pullback @ POOLED_crypto_spot_4h

**Verdict: SCRAP**

- Gabungan 4 simbol: BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT
- GAGAL: PF OOS gabungan 0.56 < 1.15
- GAGAL: degradasi IS→OOS 54% > 40%
- GAGAL: PF rata-rata dengan biaya x2 = 0.44 < 1
- GAGAL: timing entry tidak lebih baik dari acak (rata-rata persentil 47 < 75)
- GAGAL: PBO rata-rata 0.60 >= 0.5: overfit
- GAGAL: 4/4 simbol gagal PBO atau tes acak: basket tidak boleh menutupi kegagalan mayoritas
- PERINGATAN: Sharpe OOS -1.12 < rata-rata buy&hold -0.33
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9
- PERINGATAN: hanya 0/4 simbol profitable OOS: edge tidak merata

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 38 | 90 | 90 |
| Profit factor | 1.22 | 0.56 | 0.44 |
| Win rate | 32.3% | 18.9% | 0.0% |
| Expectancy (R) | 0.09 | -0.18 | 0.00 |
| Sharpe | 0.09 | -1.12 | 0.00 |
| Max DD | -5.1% | -3.4% | 0.0% |
| CAGR | -0.0% | -1.4% | 0.0% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Timing vs entry acak: persentil 47 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.60 (harus < 0.5)
- Buy & hold jendela OOS: return -17.4%, Sharpe -0.33, maxDD -60.5% | strategi: return -3.0%, Sharpe -1.12, maxDD -3.4%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -3.5%, p95 -4.2%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|