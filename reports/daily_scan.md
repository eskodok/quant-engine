# Scan harian — 2026-09-11 01:05 UTC (08:05 WIB)

| Simbol | TF | Aksi | Regime | Conf | Close | SL | TP | Validasi | Catatan |
|---|---|---|---|---|---|---|---|---|---|
| BTC/USDT | 4h | **LONG** | UPTREND | 55% | 76,562.8 | 75,053.3 | 81,091.3 | FIX |  |
| ETH/USDT | 4h | **AVOID_OR_EXIT** | UPTREND | 0% | 2,438.19 |  |  | SCRAP |  |
| SOL/USDT | 4h | **AVOID_OR_EXIT** | UPTREND | 12% | 98.65 |  |  | SCRAP |  |
| BNB/USDT | 4h | **AVOID_OR_EXIT** | UPTREND | 60% | 708.443 |  |  | FIX |  |
| BTC/USDT | 1d | **NO_TRADE** | SIDEWAYS | 60% | 76,562.8 |  |  | FIX | outlier.return |
| ETH/USDT | 1d | **NO_TRADE** | UPTREND | 5% | 2,438.19 |  |  | SCRAP | outlier.return |
| SOL/USDT | 1d | **NO_TRADE** | SIDEWAYS | 17% | 98.65 |  |  | SCRAP | outlier.return |
| BNB/USDT | 1d | **NO_TRADE** | UPTREND | 60% | 708.443 |  |  | FIX | outlier.return |
| BBCA | 1d | **NO_TRADE** | DOWNTREND | 0% | 6,425 |  |  | SCRAP |  |
| BBRI | 1d | **NO_TRADE** | SIDEWAYS | 13% | 3,320 |  |  | SCRAP |  |
| BMRI | 1d | **NO_TRADE** | DOWNTREND | 0% | 4,370 |  |  | SCRAP |  |
| BBNI | 1d | **NO_TRADE** | SIDEWAYS | 5% | 3,800 |  |  | SCRAP |  |
| TLKM | 1d | **AVOID_OR_EXIT** | DOWNTREND | 0% | 2,630 |  |  | SCRAP |  |
| ICBP | 1d | **AVOID_OR_EXIT** | DOWNTREND | 5% | 7,175 |  |  | SCRAP |  |
| PGAS | 1d | **AVOID_OR_EXIT** | DOWNTREND | 0% | 1,515 |  |  | SCRAP |  |
| AADI | 1d | **NO_TRADE** | UPTREND | 5% | 12,275 |  |  | SCRAP |  |
| AKRA | 1d | **NO_TRADE** | UPTREND | 5% | 1,520 |  |  | SCRAP |  |
| AMMN | 1d | **NO_TRADE** | DOWNTREND | 5% | 4,810 |  |  | SCRAP |  |
| ASII | 1d | **AVOID_OR_EXIT** | DOWNTREND | 15% | 4,870 |  |  | SCRAP |  |
| BREN | 1d | **AVOID_OR_EXIT** | DOWNTREND | 0% | 3,300 |  |  | SCRAP |  |
| EMAS | 1d | DATA_BLOCKED | | | | | | | history: hanya 235 bar (< 400) |
| ENRG | 1d | **NO_TRADE** | UPTREND | 0% | 1,460 |  |  | SCRAP | volume.spikes |
| ESSA | 1d | **NO_TRADE** | SIDEWAYS | 0% | 680 |  |  | SCRAP |  |
| JPFA | 1d | **NO_TRADE** | SIDEWAYS | 5% | 2,320 |  |  | SCRAP |  |
| PTRO | 1d | **NO_TRADE** | SIDEWAYS | 60% | 5,450 |  |  | FIX |  |
| MAPI | 1d | **AVOID_OR_EXIT** | SIDEWAYS | 0% | 1,370 |  |  | SCRAP |  |
| INDF | 1d | **NO_TRADE** | UPTREND | 10% | 7,325 |  |  | SCRAP |  |
| BUMI | 1d | **NO_TRADE** | SIDEWAYS | 5% | 212 |  |  | SCRAP | volume.spikes |
| ANTM | 1d | **NO_TRADE** | SIDEWAYS | 0% | 3,270 |  |  | SCRAP |  |
| CDIA | 1d | DATA_BLOCKED | | | | | | | history: hanya 287 bar (< 400) |
| DSSA | 1d | DATA_BLOCKED | | | | | | | stale_bars: 792 bar (40.6%) volume 0 & datar |
| TPIA | 1d | **AVOID_OR_EXIT** | DOWNTREND | 20% | 1,930 |  |  | SCRAP |  |
| SCMA | 1d | **AVOID_OR_EXIT** | DOWNTREND | 25% | 202 |  |  | SCRAP |  |
| KLBF | 1d | **AVOID_OR_EXIT** | DOWNTREND | 16% | 755 |  |  | SCRAP |  |
| UNVR | 1d | **AVOID_OR_EXIT** | DOWNTREND | 5% | 1,655 |  |  | SCRAP |  |
| MNCN | 1d | **AVOID_OR_EXIT** | DOWNTREND | 5% | 204 |  |  | SCRAP |  |
| UNTR | 1d | **NO_TRADE** | SIDEWAYS | 24% | 26,375 |  |  | SCRAP |  |

**Setup LONG hari ini: 1**

```
=== BTC/USDT [crypto_spot 4h] strategi=bollinger_reversion ===
bar tutup terakhir : 2026-09-10 20:00:00+00:00
AKSI               : LONG   (validasi: FIX, confidence 55%)
regime             : UPTREND
entry (open bar berikutnya, zona) : 76,374.1 – 76,751.5  (ref close 76,562.8)
stop loss          : 75,053.3  (-1.97%)
take profit        : 81,091.3  (+5.91%)  RR 1:3.0
qty                : 0.0163265  nilai 1,250  risiko 25
batalkan bila open bar berikutnya di luar zona entry (gap = RR rusak)
alasan:
  - close < Bollinger bawah(20,2.0)
  - regime UPTREND, ADX 24, RSI 28, close vs EMA20/50/200: -2.2%/-2.6%/+2.5%
confidence:
  - verdict validasi FIX -> basis 0.35
  - PF OOS 2.32 -> +0.20
```

## Regime pasar

- BTC/USDT (4h): UPTREND — regime UPTREND, ADX 24, RSI 28, close vs EMA20/50/200: -2.2%/-2.6%/+2.5%
- ETH/USDT (4h): UPTREND — close < EMA50: tren patah. Bila pegang posisi -> exit di open berikutnya; bila tidak -> jangan beli
- SOL/USDT (4h): UPTREND — close < EMA50: tren patah. Bila pegang posisi -> exit di open berikutnya; bila tidak -> jangan beli
- BNB/USDT (4h): UPTREND — close < EMA50: tren patah. Bila pegang posisi -> exit di open berikutnya; bila tidak -> jangan beli
- BTC/USDT (1d): SIDEWAYS — tidak ada setup: syarat entry strategi tidak terpenuhi di bar terakhir
- ETH/USDT (1d): UPTREND — tidak ada setup: syarat entry strategi tidak terpenuhi di bar terakhir
- SOL/USDT (1d): SIDEWAYS — tidak ada setup: syarat entry strategi tidak terpenuhi di bar terakhir
- BNB/USDT (1d): UPTREND — tidak ada setup: syarat entry strategi tidak terpenuhi di bar terakhir
- BBCA (1d): DOWNTREND — tidak ada setup: syarat entry strategi tidak terpenuhi di bar terakhir
- BBRI (1d): SIDEWAYS — tidak ada setup: syarat entry strategi tidak terpenuhi di bar terakhir
- BMRI (1d): DOWNTREND — tidak ada setup: syarat entry strategi tidak terpenuhi di bar terakhir
- BBNI (1d): SIDEWAYS — tidak ada setup: syarat entry strategi tidak terpenuhi di bar terakhir
- TLKM (1d): DOWNTREND — close < EMA50: tren patah. Bila pegang posisi -> exit di open berikutnya; bila tidak -> jangan beli
- ICBP (1d): DOWNTREND — close < EMA50: tren patah. Bila pegang posisi -> exit di open berikutnya; bila tidak -> jangan beli
- PGAS (1d): DOWNTREND — close < EMA50: tren patah. Bila pegang posisi -> exit di open berikutnya; bila tidak -> jangan beli
- AADI (1d): UPTREND — tidak ada setup: syarat entry strategi tidak terpenuhi di bar terakhir
- AKRA (1d): UPTREND — tidak ada setup: syarat entry strategi tidak terpenuhi di bar terakhir
- AMMN (1d): DOWNTREND — tidak ada setup: syarat entry strategi tidak terpenuhi di bar terakhir
- ASII (1d): DOWNTREND — close < EMA50: tren patah. Bila pegang posisi -> exit di open berikutnya; bila tidak -> jangan beli
- BREN (1d): DOWNTREND — close < EMA50: tren patah. Bila pegang posisi -> exit di open berikutnya; bila tidak -> jangan beli
- ENRG (1d): UPTREND — tidak ada setup: syarat entry strategi tidak terpenuhi di bar terakhir
- ESSA (1d): SIDEWAYS — tidak ada setup: syarat entry strategi tidak terpenuhi di bar terakhir
- JPFA (1d): SIDEWAYS — tidak ada setup: syarat entry strategi tidak terpenuhi di bar terakhir
- PTRO (1d): SIDEWAYS — tidak ada setup: syarat entry strategi tidak terpenuhi di bar terakhir
- MAPI (1d): SIDEWAYS — close < EMA50: tren patah. Bila pegang posisi -> exit di open berikutnya; bila tidak -> jangan beli
- INDF (1d): UPTREND — tidak ada setup: syarat entry strategi tidak terpenuhi di bar terakhir
- BUMI (1d): SIDEWAYS — tidak ada setup: syarat entry strategi tidak terpenuhi di bar terakhir
- ANTM (1d): SIDEWAYS — tidak ada setup: syarat entry strategi tidak terpenuhi di bar terakhir
- TPIA (1d): DOWNTREND — close < EMA50: tren patah. Bila pegang posisi -> exit di open berikutnya; bila tidak -> jangan beli
- SCMA (1d): DOWNTREND — close < EMA50: tren patah. Bila pegang posisi -> exit di open berikutnya; bila tidak -> jangan beli
- KLBF (1d): DOWNTREND — close < EMA50: tren patah. Bila pegang posisi -> exit di open berikutnya; bila tidak -> jangan beli
- UNVR (1d): DOWNTREND — close < EMA50: tren patah. Bila pegang posisi -> exit di open berikutnya; bila tidak -> jangan beli
- MNCN (1d): DOWNTREND — close < EMA50: tren patah. Bila pegang posisi -> exit di open berikutnya; bila tidak -> jangan beli
- UNTR (1d): SIDEWAYS — tidak ada setup: syarat entry strategi tidak terpenuhi di bar terakhir
