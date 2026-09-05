## Validasi donchian_breakout @ POOLED_idx_1d

**Verdict: SCRAP**

- Gabungan 11 simbol: BBCA, BBRI, BMRI, BBNI, TLKM, ASII, ICBP, INDF, ANTM, UNTR, PGAS
- GAGAL: PF OOS gabungan 0.77 < 1.15
- GAGAL: PF in-sample 0.77 < 1.1: OOS untung = kebetulan rezim, bukan edge
- GAGAL: timing entry tidak lebih baik dari acak (rata-rata persentil 64 < 75)
- GAGAL: 7/11 simbol gagal PBO atau tes acak: basket tidak boleh menutupi kegagalan mayoritas
- PERINGATAN: Sharpe OOS -0.44 < rata-rata buy&hold 0.02
- PERINGATAN: deflated Sharpe prob 0.00 < 0.9
- PERINGATAN: hanya 5/11 simbol profitable OOS: edge tidak merata

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 12 | 66 | 66 |
| Profit factor | 0.77 | 0.77 | inf |
| Win rate | 36.4% | 43.9% | 0.0% |
| Expectancy (R) | -0.22 | -0.14 | 0.00 |
| Sharpe | -0.23 | -0.44 | 0.00 |
| Max DD | -4.7% | -1.5% | 0.0% |
| CAGR | -0.4% | -0.3% | 0.0% |

- Deflated Sharpe prob (n_trials=45): 0.00
- Timing vs entry acak: persentil 64 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.45 (harus < 0.5)
- Buy & hold jendela OOS: return -7.0%, Sharpe 0.02, maxDD -46.8% | strategi: return -0.9%, Sharpe -0.44, maxDD -1.5%
- Stabilitas parameter antar fold: 87%
- Monte Carlo max DD: median -1.3%, p95 -1.8%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|