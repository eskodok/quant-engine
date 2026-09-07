## Validasi bollinger_reversion @ POOLED_idx_1d

**Verdict: SCRAP**

- Gabungan 23 simbol: BBCA, BBRI, BMRI, BBNI, TLKM, ICBP, PGAS, AKRA, ASII, ENRG, ESSA, JPFA, PTRO, MAPI, INDF, BUMI, ANTM, TPIA, SCMA, KLBF, UNVR, MNCN, UNTR
- GAGAL: PF OOS gabungan 0.89 < 1.15
- GAGAL: timing entry tidak lebih baik dari acak (rata-rata persentil 60 < 75)
- GAGAL: PBO rata-rata 0.50 >= 0.5: overfit
- GAGAL: 18/23 simbol gagal PBO atau tes acak: basket tidak boleh menutupi kegagalan mayoritas
- PERINGATAN: Sharpe OOS -0.29 < rata-rata buy&hold 0.18
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9
- PERINGATAN: hanya 7/23 simbol profitable OOS: edge tidak merata

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 13 | 166 | 166 |
| Profit factor | 1.27 | 0.89 | 1.06 |
| Win rate | 59.5% | 55.4% | 0.0% |
| Expectancy (R) | 0.07 | -0.15 | 0.00 |
| Sharpe | 0.09 | -0.29 | 0.00 |
| Max DD | -3.1% | -1.1% | 0.0% |
| CAGR | 0.1% | -0.1% | 0.0% |

- Deflated Sharpe prob (n_trials=40): 0.00
- Timing vs entry acak: persentil 60 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.50 (harus < 0.5)
- Buy & hold jendela OOS: return +71.7%, Sharpe 0.18, maxDD -54.2% | strategi: return -0.4%, Sharpe -0.29, maxDD -1.1%
- Stabilitas parameter antar fold: 95%
- Monte Carlo max DD: median -0.7%, p95 -1.0%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|