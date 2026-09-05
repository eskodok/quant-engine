# Quant Swing Engine v0.5 — anti garbage-in, garbage-out

> **Tidak bisa coding? Baca `SETUP.md`** — semua lewat browser, tidak perlu install apa pun.

Signal engine swing (4H–1D) untuk crypto spot/perp dan saham IDX. Bukan bot;
outputnya setup (entry, SL, TP, qty, confidence, alasan) yang kamu eksekusi manual.

## Kenapa engine lama "sampah" dan apa yang beda di sini

| Masalah lama | Perlindungan di engine ini |
|---|---|
| Data rusak masuk diam-diam | `scrub` = gerbang wajib: 10 cek (schema, gap, OHLC, NaN, stale, split/outlier, kesegaran, bar belum tutup). Satu BLOCK → berhenti. Tidak ada mode "abaikan". |
| Lookahead bias (pakai close bar yang belum selesai, indikator "mengintip") | Bar terakhir yang belum tutup dibuang di loader. `assert_no_lookahead()`: data masa depan diacak, sinyal masa lalu harus identik — dijalankan di test DAN sebelum setiap validasi. |
| Backtest bagus, live jelek | Fill di **open bar berikutnya** + slippage, fee dua sisi eksplisit per market, SL menang bila SL & TP kena di bar sama, gap melewati SL diisi di open. |
| Overfit | Walk-forward 5 fold (optimasi hanya dari data sebelum blok test), grid sengaja kecil (≤3 parameter), degradasi IS→OOS >40% = FIX, deflated Sharpe (koreksi jumlah percobaan), stabilitas parameter antar fold. |
| Edge semu dari biaya | Stress test biaya ×2: PF harus tetap > 1. |
| Confidence karangan | Confidence diturunkan dari verdict validasi + PF OOS + DSR + regime + likuiditas, dan tiap komponennya dicetak. Strategi yang belum SHIP/FIX → tidak boleh keluar sinyal LONG. |
| Terlalu rumit | 5 perintah CLI, ~900 baris Python, pandas/numpy/scipy saja. Setiap modul satu tanggung jawab. |

## Instalasi (di komputermu)

```bash
pip install pandas numpy scipy pyarrow ccxt yfinance pytest
python -m pytest tests -q          # harus 12 passed
```

## Alur kerja

```bash
# 1. cek data dulu
python cli.py scrub BTC/USDT --market crypto_spot --tf 4h
python cli.py scrub BBCA --market idx --tf 1d

# 2. backtest cepat (SELURUH data = in-sample; hanya untuk lihat strategi "hidup")
python cli.py backtest BTC/USDT --market crypto_spot --tf 4h --strategy trend_pullback --trades 10

# 3. validasi walk-forward -> verdict SHIP / FIX / SCRAP, tersimpan di reports/
python cli.py validate BTC/USDT --market crypto_spot --tf 4h --strategy trend_pullback
python cli.py validate BBCA BBRI --market idx --tf 1d --strategy donchian_breakout

# 4. sinyal hari ini (hanya keluar LONG kalau validasi SHIP/FIX)
python cli.py signal BTC/USDT --market crypto_spot --tf 4h --equity 5000
python cli.py scan BBCA BBRI TLKM ASII BMRI --market idx --tf 1d --equity 50000000
```

Opsi: `--csv data.csv` (kolom ts,open,high,low,close,volume) untuk data sendiri;
`--synthetic` untuk data uji; `--cost-mult 2` untuk backtest dengan biaya dobel.

## Cara membaca verdict

- **SHIP**: OOS ≥30 trade, PF OOS ≥1.15, degradasi <40%, tahan biaya ×2, DSR ≥0.90, parameter stabil. Layak dipakai untuk sinyal.
- **FIX**: profitable OOS tapi ada peringatan (sampel kecil, DSR rendah, parameter goyah). Boleh dipakai dengan size setengah.
- **SCRAP**: OOS tidak profitable / gagal lookahead / edge habis oleh biaya. Jangan dipakai — dan ini hasil yang *normal* untuk kebanyakan ide.

Catatan jujur: pada data sintetis acak engine ini memberi SCRAP (memang seharusnya —
tidak ada edge di random walk), sementara backtest full-sample menunjukkan PF 2.1 /
Sharpe 2.2. Itulah persisnya jebakan "backtest bagus, live jelek".

## Mode otomatis (GitHub Actions + Claude)

```
watchlist.txt  --> scripts/fetch_data.py  --> data/*.csv          (GitHub, 06:15 WIB Sen-Jum)
               --> scripts/run_validate.py --> reports/*_*.json   (GitHub, Minggu malam)
               --> scripts/run_daily.py    --> reports/daily_scan.md/.json
Claude (07:00 WIB) clone repo -> baca reports -> cari berita -> ringkasan ke kamu
```

Validasi mingguan menguji **semua strategi** untuk tiap simbol; `run_daily` memilih otomatis
strategi dengan verdict terbaik (SHIP > FIX) bila kolom strategi di watchlist kosong.
Aturan tambahan: strategi harus profitable **in-sample** juga — OOS untung tapi IS rugi
berarti kebetulan rezim, bukan edge (kasus nyata: Bollinger crypto 4H, IS 0.62 / OOS 1.31).

Validasi dilakukan per simbol **dan** per basket (semua simbol satu market digabung):
strategi swing per simbol hanya memberi 5–30 trade OOS, terlalu sedikit untuk disimpulkan;
basket 5 saham memberi 5x bukti. Sinyal memakai verdict basket bila per simbol gagal hanya
karena sampel kecil.

## Struktur

```
engine/config.py    profil market (fee, slippage, lot, ARA/ARB), risk, threshold validasi
engine/data.py      loader ccxt / yfinance / csv -> satu format, bar belum tutup dibuang
engine/scrub.py     gerbang kualitas data (BLOCK/WARN/OK)
engine/features.py  indikator past-only + assert_no_lookahead()
engine/strategy.py  TrendPullback, DonchianBreakout, RSI2Reversion, BollingerReversion (fungsi murni)
engine/backtest.py  simulasi bar-per-bar, fill open t+1, SL/TP intrabar konservatif
engine/metrics.py   PF, Sharpe, DD, deflated Sharpe, Monte Carlo DD
engine/validate.py  walk-forward + stress biaya + verdict
engine/signal.py    setup hari ini + confidence yang bisa diaudit
cli.py              scrub | backtest | validate | signal | scan
scripts/            fetch_data, run_validate, run_daily (dipakai GitHub Actions)
watchlist.txt       daftar simbol; edit langsung di GitHub
tests/              12 uji anti-GIGO
```

## Menambah strategi

Subclass `Strategy` di `engine/strategy.py`: isi `params`, `grid` (kecil!), dan
`signals(f)` yang mengembalikan kolom `entry, exit, stop, target, reason` dari fitur
sampai bar t saja. Daftarkan di `STRATEGIES`. Test lookahead otomatis mencakupnya.

## Hasil di data riil (Sep 2026)

Keempat strategi SCRAP pada BTC/ETH/SOL/BNB 4H (500 hari) dan 5 blue chip IDX (6 tahun):
PF OOS basket 0.47–0.87. Engine bekerja; strateginya belum. v0.4 memperbesar bukti
(crypto 4H 12.000 bar + 1D 4.000 bar, IDX 8 tahun, 12 emiten) sebelum riset lanjut.

## Batasan v0.4 (sengaja)

Long only; satu posisi per simbol; funding perp tidak dimodelkan (ada WARN);
IDX hanya 1D via Yahoo (delay ~15 menit, split harus di-handle manual bila scrub BLOCK);
tidak ada portfolio-level risk antar simbol; belum ada layer fundamental/berita.

## Referensi yang dipakai

- shakeebshaan/claude-code-quant-skills — pola `/data-scrub` dan `/backtest-review`
- wshobson/agents quantitative-trading/backtesting-frameworks — train/val/test, walk-forward
- marketcalls/vectorbt-backtesting-skills — tabel biaya per market
- Susan Potter, "A Taxonomy of Backtest Lies" — daftar bias
- Bailey & López de Prado (2014) — Deflated Sharpe Ratio
