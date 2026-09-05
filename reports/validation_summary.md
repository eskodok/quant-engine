# Validasi mingguan — 2026-09-05 

| Simbol | Strategi | Verdict | Sebelumnya | PF OOS | Trade OOS | DSR | Alasan utama |
|---|---|---|---|---|---|---|---|
| BTC/USDT | trend_pullback | **SCRAP** | SCRAP | 0.83 | 16 | 0.09 | GAGAL: trade OOS 16 < 30: belum cukup bukti |
| ETH/USDT | trend_pullback | **SCRAP** | SCRAP | 1.13 | 21 | 0.23 | GAGAL: trade OOS 21 < 30: belum cukup bukti |
| SOL/USDT | trend_pullback | **SCRAP** | SCRAP | 0.37 | 14 | 0.02 | GAGAL: trade OOS 14 < 30: belum cukup bukti |
| BNB/USDT | trend_pullback | **SCRAP** | SCRAP | 1.16 | 19 | 0.26 | GAGAL: trade OOS 19 < 30: belum cukup bukti |
| BBCA | trend_pullback | **SCRAP** | - | 0.00 | 1 | 0.00 | GAGAL: trade OOS 1 < 30: belum cukup bukti |
| BBRI | trend_pullback | **SCRAP** | - | 0.00 | 0 | 0.03 | GAGAL: trade OOS 0 < 30: belum cukup bukti |
| BMRI | trend_pullback | **SCRAP** | - | 0.00 | 3 | 0.00 | GAGAL: trade OOS 3 < 30: belum cukup bukti |
| TLKM | trend_pullback | **SCRAP** | - | 0.00 | 3 | 0.00 | GAGAL: trade OOS 3 < 30: belum cukup bukti |
| ASII | trend_pullback | **SCRAP** | - | 1.74 | 9 | 0.14 | GAGAL: trade OOS 9 < 30: belum cukup bukti |

## Validasi basket (trade OOS semua simbol digabung)

| Basket | Strategi | Verdict | PF OOS | Trade OOS | DSR | Catatan |
|---|---|---|---|---|---|---|
| crypto_spot 4h (4 simbol) | trend_pullback | **SCRAP** | 0.87 | 70 | 0.00 | GAGAL: PF OOS gabungan 0.87 < 1.15; GAGAL: PF rata-rata dengan biaya x2 = 0.66 < 1; PERINGATAN: deflated Sharpe prob 0.0 |
| idx 1d (5 simbol) | trend_pullback | **SCRAP** | 0.47 | 16 | 0.00 | GAGAL: trade OOS gabungan 16 < 30; GAGAL: PF OOS gabungan 0.47 < 1.15; GAGAL: PF rata-rata dengan biaya x2 = 0.31 < 1; P |
