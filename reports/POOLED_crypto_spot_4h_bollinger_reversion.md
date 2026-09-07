## Validasi bollinger_reversion @ POOLED_crypto_spot_4h

**Verdict: SCRAP**

- Gabungan 4 simbol: BTC/USDT, ETH/USDT, SOL/USDT, BNB/USDT
- GAGAL: PF in-sample 1.00 < 1.1: OOS untung = kebetulan rezim, bukan edge
- GAGAL: PBO rata-rata 0.53 >= 0.5: overfit
- GAGAL: 2/4 simbol gagal PBO atau tes acak: basket tidak boleh menutupi kegagalan mayoritas
- PERINGATAN: deflated Sharpe prob 0.15 < 0.9

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 21 | 36 | 36 |
| Profit factor | 1.00 | 1.58 | 1.57 |
| Win rate | 57.3% | 66.7% | 0.0% |
| Expectancy (R) | -0.04 | 0.20 | 0.00 |
| Sharpe | -0.13 | 0.63 | 0.00 |
| Max DD | -4.6% | -0.9% | 0.0% |
| CAGR | -0.5% | 0.6% | 0.0% |

- Deflated Sharpe prob (n_trials=40): 0.15
- Timing vs entry acak: persentil 88 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.53 (harus < 0.5)
- Buy & hold jendela OOS: return -19.6%, Sharpe -0.38, maxDD -60.5% | strategi: return +1.2%, Sharpe 0.63, maxDD -0.9%
- Stabilitas parameter antar fold: 70%
- Monte Carlo max DD: median -0.6%, p95 -1.1%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|