## Validasi trend_pullback @ POOLED_idx_1d

**Verdict: SCRAP**

- Gabungan 22 simbol: BBCA, BBRI, BMRI, BBNI, TLKM, ICBP, PGAS, AKRA, ASII, ENRG, ESSA, JPFA, PTRO, MAPI, INDF, BUMI, ANTM, TPIA, SCMA, KLBF, UNVR, UNTR
- GAGAL: PF OOS gabungan 0.93 < 1.15
- GAGAL: PF in-sample 0.89 < 1.1: OOS untung = kebetulan rezim, bukan edge
- GAGAL: PF rata-rata dengan biaya x2 = 0.86 < 1
- GAGAL: timing entry tidak lebih baik dari acak (rata-rata persentil 62 < 75)
- GAGAL: PBO rata-rata 0.53 >= 0.5: overfit
- GAGAL: 18/22 simbol gagal PBO atau tes acak: basket tidak boleh menutupi kegagalan mayoritas
- PERINGATAN: Sharpe OOS -0.21 < rata-rata buy&hold 0.21
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9
- PERINGATAN: hanya 10/22 simbol profitable OOS: edge tidak merata

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 17 | 184 | 184 |
| Profit factor | 0.89 | 0.93 | 0.86 |
| Win rate | 24.5% | 31.0% | 0.0% |
| Expectancy (R) | -0.09 | -0.01 | 0.00 |
| Sharpe | -0.21 | -0.21 | 0.00 |
| Max DD | -4.5% | -0.7% | 0.0% |
| CAGR | -0.2% | -0.1% | 0.0% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Timing vs entry acak: persentil 62 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.53 (harus < 0.5)
- Buy & hold jendela OOS: return +77.5%, Sharpe 0.21, maxDD -53.9% | strategi: return -0.2%, Sharpe -0.21, maxDD -0.7%
- Stabilitas parameter antar fold: 80%
- Monte Carlo max DD: median -0.7%, p95 -1.0%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|