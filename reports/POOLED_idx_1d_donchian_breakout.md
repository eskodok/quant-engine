## Validasi donchian_breakout @ POOLED_idx_1d

**Verdict: SCRAP**

- Gabungan 21 simbol: BBCA, BBRI, BMRI, BBNI, TLKM, ICBP, PGAS, AKRA, ASII, ENRG, ESSA, JPFA, PTRO, MAPI, INDF, BUMI, ANTM, TPIA, SCMA, UNVR, UNTR
- GAGAL: PF in-sample 1.02 < 1.1: OOS untung = kebetulan rezim, bukan edge
- GAGAL: timing entry tidak lebih baik dari acak (rata-rata persentil 72 < 75)
- GAGAL: 15/21 simbol gagal PBO atau tes acak: basket tidak boleh menutupi kegagalan mayoritas
- PERINGATAN: deflated Sharpe prob 0.12 < 0.9

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 11 | 143 | 143 |
| Profit factor | 1.02 | 1.21 | inf |
| Win rate | 38.3% | 49.0% | 0.0% |
| Expectancy (R) | -0.11 | 0.12 | 0.00 |
| Sharpe | -0.10 | 0.52 | 0.00 |
| Max DD | -4.4% | -0.9% | 0.0% |
| CAGR | -0.1% | 0.3% | 0.0% |

- Deflated Sharpe prob (n_trials=45): 0.12
- Timing vs entry acak: persentil 72 (harus >= 75)
- Probability of Backtest Overfitting (CSCV): 0.49 (harus < 0.5)
- Buy & hold jendela OOS: return +83.9%, Sharpe 0.26, maxDD -53.5% | strategi: return +0.8%, Sharpe 0.52, maxDD -0.9%
- Stabilitas parameter antar fold: 85%
- Monte Carlo max DD: median -0.5%, p95 -0.9%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|