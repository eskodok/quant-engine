## Validasi bollinger_reversion @ BNB/USDT

**Verdict: SCRAP**

- Uji lookahead: LULUS (sinyal masa lalu tidak berubah saat data masa depan diacak)
- Data terlalu pendek untuk 5 fold (test_len=20 bar)

| Metrik | In-sample (rata2 fold) | Out-of-sample (gabungan) | OOS biaya x2 |
|---|---|---|---|
| Trades | 0 | 0 | 0 |
| Profit factor | 0.00 | 0.00 | 0.00 |
| Win rate | 0.0% | 0.0% | 0.0% |
| Expectancy (R) | 0.00 | 0.00 | 0.00 |
| Sharpe | 0.00 | 0.00 | 0.00 |
| Max DD | 0.0% | 0.0% | 0.0% |
| CAGR | 0.0% | 0.0% | 0.0% |

- Deflated Sharpe prob (n_trials=0): 0.00
- Stabilitas parameter antar fold: 0%
- Monte Carlo max DD: median 0.0%, p95 0.0%
- Parameter terpilih (fold terakhir): {}

### Fold
| # | Train | Test | Params | IS PF | OOS PF | OOS trades |
|---|---|---|---|---|---|---|