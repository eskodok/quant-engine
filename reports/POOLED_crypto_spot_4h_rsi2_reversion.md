## Validasi rsi2_reversion @ POOLED_crypto_spot_4h

**Verdict: SCRAP**

- Gabungan 4 simbol: BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT
- GAGAL: PF OOS gabungan 0.72 < 1.15
- GAGAL: PF in-sample 0.83 < 1.1: OOS untung = kebetulan rezim, bukan edge
- GAGAL: PF rata-rata dengan biaya x2 = 0.43 < 1
- GAGAL: 2/4 simbol gagal PBO atau tes acak: basket tidak boleh menutupi kegagalan mayoritas
- PERINGATAN: Sharpe OOS -0.88 < rata-rata buy&hold -0.38
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9
- PERINGATAN: hanya 1/4 simbol profitable OOS: edge tidak merata

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 75 | 169 | 169 |
| Profit factor | 0.83 | 0.72 | 0.43 |
| Win rate | 62.5% | 59.8% | 0.0% |
| Expectancy (R) | -0.04 | -0.06 | 0.00 |
| Sharpe | -0.46 | -0.88 | 0.00 |
| Max DD | -4.7% | -2.6% | 0.0% |
| CAGR | -1.5% | -0.9% | 0.0% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 82 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.13 (harus < 0.5)
- Buy & hold jendela OOS: return -19.6%, Sharpe -0.38, maxDD -60.5% | strategi: return -2.0%, Sharpe -0.88, maxDD -2.6%
- Stabilitas parameter antar fold: 85%
- Monte Carlo max DD: median -2.5%, p95 -3.2%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|