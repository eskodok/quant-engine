## Validasi trend_pullback @ POOLED_idx_1d

**Verdict: SCRAP**

- Gabungan 12 simbol: BBCA, BBRI, BMRI, BBNI, TLKM, ASII, ICBP, INDF, KLBF, ANTM, UNTR, PGAS
- GAGAL: PF OOS gabungan 0.77 < 1.15
- GAGAL: PF in-sample 0.78 < 1.1: OOS untung = kebetulan rezim, bukan edge
- GAGAL: PF rata-rata dengan biaya x2 = 0.69 < 1
- GAGAL: timing entry tidak lebih baik dari acak (rata-rata persentil 63 < 75)
- GAGAL: 9/12 simbol gagal PBO atau tes acak: basket tidak boleh menutupi kegagalan mayoritas
- PERINGATAN: Sharpe OOS -0.58 < rata-rata buy&hold -0.04
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 18 | 99 | 99 |
| Profit factor | 0.78 | 0.77 | 0.69 |
| Win rate | 25.0% | 30.3% | 0.0% |
| Expectancy (R) | -0.11 | -0.08 | 0.00 |
| Sharpe | -0.28 | -0.58 | 0.00 |
| Max DD | -4.8% | -1.4% | 0.0% |
| CAGR | -0.4% | -0.3% | 0.0% |

- Deflated Sharpe prob (n_trials=135): 0.00
- Timing vs entry acak: persentil 63 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.38 (harus < 0.5)
- Buy & hold jendela OOS: return -11.2%, Sharpe -0.04, maxDD -48.1% | strategi: return -0.8%, Sharpe -0.58, maxDD -1.4%
- Stabilitas parameter antar fold: 77%
- Monte Carlo max DD: median -1.1%, p95 -1.5%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|