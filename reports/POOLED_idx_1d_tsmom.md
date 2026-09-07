## Validasi tsmom @ POOLED_idx_1d

**Verdict: SCRAP**

- Gabungan 23 simbol: BBCA, BBRI, BMRI, BBNI, TLKM, ICBP, PGAS, AKRA, ASII, ENRG, ESSA, JPFA, PTRO, MAPI, INDF, BUMI, ANTM, TPIA, SCMA, KLBF, UNVR, MNCN, UNTR
- GAGAL: PF OOS gabungan 1.11 < 1.15
- GAGAL: PF in-sample 1.02 < 1.1: OOS untung = kebetulan rezim, bukan edge
- GAGAL: timing entry tidak lebih baik dari acak (rata-rata persentil 58 < 75)
- GAGAL: PBO rata-rata 0.53 >= 0.5: overfit
- GAGAL: 19/23 simbol gagal PBO atau tes acak: basket tidak boleh menutupi kegagalan mayoritas
- PERINGATAN: Sharpe OOS 0.15 < rata-rata buy&hold 0.18
- PERINGATAN: deflated Sharpe prob 0.06 < 0.9
- PERINGATAN: hanya 10/23 simbol profitable OOS: edge tidak merata

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 13 | 170 | 170 |
| Profit factor | 1.02 | 1.11 | 1.07 |
| Win rate | 22.1% | 25.9% | 0.0% |
| Expectancy (R) | 0.01 | 0.07 | 0.00 |
| Sharpe | -0.07 | 0.15 | 0.00 |
| Max DD | -21.1% | -5.8% | 0.0% |
| CAGR | -0.2% | 0.4% | 0.0% |

- Deflated Sharpe prob (n_trials=30): 0.06
- Timing vs entry acak: persentil 58 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.53 (harus < 0.5)
- Buy & hold jendela OOS: return +71.7%, Sharpe 0.18, maxDD -54.2% | strategi: return +1.1%, Sharpe 0.15, maxDD -5.8%
- Stabilitas parameter antar fold: 64%
- Monte Carlo max DD: median -2.8%, p95 -4.3%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|