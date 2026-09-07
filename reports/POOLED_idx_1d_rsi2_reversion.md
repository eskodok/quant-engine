## Validasi rsi2_reversion @ POOLED_idx_1d

**Verdict: SCRAP**

- Gabungan 23 simbol: BBCA, BBRI, BMRI, BBNI, TLKM, ICBP, PGAS, AKRA, ASII, ENRG, ESSA, JPFA, PTRO, MAPI, INDF, BUMI, ANTM, TPIA, SCMA, KLBF, UNVR, MNCN, UNTR
- GAGAL: PF OOS gabungan 0.58 < 1.15
- GAGAL: degradasi IS→OOS 69% > 40%
- GAGAL: PF rata-rata dengan biaya x2 = 0.49 < 1
- GAGAL: timing entry tidak lebih baik dari acak (rata-rata persentil 49 < 75)
- GAGAL: 20/23 simbol gagal PBO atau tes acak: basket tidak boleh menutupi kegagalan mayoritas
- PERINGATAN: Sharpe OOS -1.60 < rata-rata buy&hold 0.18
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9
- PERINGATAN: hanya 4/23 simbol profitable OOS: edge tidak merata

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 28 | 326 | 326 |
| Profit factor | 1.85 | 0.58 | 0.49 |
| Win rate | 64.0% | 54.9% | 0.0% |
| Expectancy (R) | 0.06 | -0.13 | 0.00 |
| Sharpe | 0.17 | -1.60 | 0.00 |
| Max DD | -2.6% | -1.8% | 0.0% |
| CAGR | 0.2% | -0.6% | 0.0% |

- Deflated Sharpe prob (n_trials=60): 0.00
- Timing vs entry acak: persentil 49 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.47 (harus < 0.5)
- Buy & hold jendela OOS: return +71.7%, Sharpe 0.18, maxDD -54.2% | strategi: return -1.8%, Sharpe -1.60, maxDD -1.8%
- Stabilitas parameter antar fold: 64%
- Monte Carlo max DD: median -1.8%, p95 -2.0%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|