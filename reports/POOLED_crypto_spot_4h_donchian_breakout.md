## Validasi donchian_breakout @ POOLED_crypto_spot_4h

**Verdict: SCRAP**

- Gabungan 4 simbol: BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT
- GAGAL: PF OOS gabungan 0.74 < 1.15
- GAGAL: degradasi IS→OOS 49% > 40%
- GAGAL: PF rata-rata dengan biaya x2 = 0.57 < 1
- GAGAL: timing entry tidak lebih baik dari acak (rata-rata persentil 55 < 75)
- GAGAL: 4/4 simbol gagal PBO atau tes acak: basket tidak boleh menutupi kegagalan mayoritas
- PERINGATAN: Sharpe OOS -0.68 < rata-rata buy&hold -0.38
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9
- PERINGATAN: hanya 0/4 simbol profitable OOS: edge tidak merata

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 31 | 77 | 77 |
| Profit factor | 1.47 | 0.74 | 0.57 |
| Win rate | 39.3% | 26.0% | 0.0% |
| Expectancy (R) | 0.29 | -0.14 | 0.00 |
| Sharpe | 0.77 | -0.68 | 0.00 |
| Max DD | -4.5% | -4.3% | 0.0% |
| CAGR | 3.6% | -1.2% | 0.0% |

- Deflated Sharpe prob (n_trials=45): 0.00
- Timing vs entry acak: persentil 55 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.33 (harus < 0.5)
- Buy & hold jendela OOS: return -19.6%, Sharpe -0.38, maxDD -60.5% | strategi: return -2.6%, Sharpe -0.68, maxDD -4.3%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -3.6%, p95 -4.8%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|