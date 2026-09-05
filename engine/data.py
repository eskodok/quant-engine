"""Loader data OHLCV. Satu format keluaran, apa pun sumbernya.

Kontrak keluaran:
- index: DatetimeIndex UTC, naik monoton, unik, nama 'ts'
- kolom: open, high, low, close, volume (float64)
- setiap bar = bar yang SUDAH TUTUP. Bar yang masih berjalan dibuang di sini,
  bukan di strategi (sumber lookahead paling umum: memakai close bar yang belum selesai).
"""
from __future__ import annotations

import time
from pathlib import Path

import pandas as pd

from .config import TIMEFRAME_SECONDS

COLUMNS = ["open", "high", "low", "close", "volume"]
CACHE_DIR = Path(__file__).resolve().parent.parent / "data_cache"


def _finalize(df: pd.DataFrame, timeframe: str, drop_open_bar: bool = True) -> pd.DataFrame:
    df = df[COLUMNS].astype("float64").copy()
    df.index = pd.to_datetime(df.index, utc=True)
    df.index.name = "ts"
    df = df[~df.index.duplicated(keep="last")].sort_index()
    if drop_open_bar and len(df):
        # bar terakhir dianggap masih berjalan jika ts_open + tf > sekarang
        tf = TIMEFRAME_SECONDS[timeframe]
        now = pd.Timestamp.now(tz="UTC")
        last_close = df.index[-1] + pd.Timedelta(seconds=tf)
        if last_close > now:
            df = df.iloc[:-1]
    return df


# Urutan fallback exchange. Binance/OKX/Bybit memblokir IP Amerika (termasuk server
# GitHub Actions), jadi kita coba berurutan sampai ada yang memberi data.
EXCHANGE_FALLBACK = ("binance", "kucoin", "gateio", "mexc", "bitget", "kraken", "coinbase", "bitstamp")


def load_crypto(symbol: str, timeframe: str = "4h", limit_bars: int = 3000,
                exchange_id: str | None = None) -> pd.DataFrame:
    """Ambil OHLCV via ccxt dengan fallback exchange. symbol contoh: 'BTC/USDT'.
    Bila exchange tidak punya pair USDT, dicoba pair USD (harga hampir identik)."""
    import ccxt  # import lokal agar modul lain tetap bisa dipakai tanpa ccxt

    errors = []
    for ex_id in ([exchange_id] if exchange_id else EXCHANGE_FALLBACK):
        try:
            ex = getattr(ccxt, ex_id)({"enableRateLimit": True, "timeout": 20000})
            markets = ex.load_markets()
            sym = symbol
            if sym not in markets:
                alt = symbol.replace("/USDT", "/USD")
                if alt in markets:
                    sym = alt
                else:
                    errors.append(f"{ex_id}: pair {symbol} tidak ada")
                    continue
            if timeframe not in (ex.timeframes or {}):
                errors.append(f"{ex_id}: timeframe {timeframe} tidak didukung")
                continue
            df = _fetch_ccxt(ex, sym, timeframe, limit_bars)
            if len(df) < 300:
                errors.append(f"{ex_id}: hanya {len(df)} bar")
                continue
            df.attrs["source"] = f"{ex_id}:{sym}"
            return df
        except Exception as e:  # noqa: BLE001 - lanjut ke exchange berikutnya
            errors.append(f"{ex_id}: {type(e).__name__}: {str(e)[:80]}")
    raise RuntimeError(f"semua exchange gagal untuk {symbol}: " + " | ".join(errors))


def _fetch_ccxt(ex, symbol: str, timeframe: str, limit_bars: int) -> pd.DataFrame:
    """Tarik OHLCV mundur dari sekarang, halaman demi halaman, sampai `limit_bars` atau
    histori exchange habis. Berhenti HANYA bila halaman kosong / tidak maju — halaman
    yang tidak penuh bukan tanda habis (KuCoin dkk. punya lubang kecil di datanya)."""
    ms = TIMEFRAME_SECONDS[timeframe] * 1000
    now_ms = int(time.time() * 1000)
    since = now_ms - limit_bars * ms
    per_call = 720 if ex.id == "kraken" else 1000
    rows: list = []
    last_ts = None
    for _ in range(400):  # pengaman: maks 400 halaman
        batch = ex.fetch_ohlcv(symbol, timeframe=timeframe, since=since, limit=per_call)
        if not batch:
            # tidak ada data di rentang ini (exchange belum ada saat itu) -> lompat ke depan
            since += per_call * ms
            if since >= now_ms:
                break
            continue
        rows.extend(batch)
        newest = batch[-1][0]
        if last_ts is not None and newest <= last_ts:
            break  # tidak maju
        last_ts = newest
        if newest + ms >= now_ms - ms:
            break  # sudah sampai bar terakhir yang tutup
        since = newest + ms
    df = pd.DataFrame(rows, columns=["ts", *COLUMNS])
    df["ts"] = pd.to_datetime(df["ts"], unit="ms", utc=True)
    df = df.set_index("ts")
    df = _finalize(df, timeframe)
    # data harus segar; kalau tidak, exchange ini dianggap gagal (pemanggil pindah ke exchange lain)
    if len(df) and (pd.Timestamp.now(tz="UTC") - df.index[-1]).total_seconds() > 3 * TIMEFRAME_SECONDS[timeframe]:
        raise RuntimeError(f"data tidak segar: bar terakhir {df.index[-1]}")
    return df


def load_idx(ticker: str, timeframe: str = "1d", years: int = 6) -> pd.DataFrame:
    """Ambil saham IDX via yfinance. ticker 'BBCA' -> 'BBCA.JK'.

    Catatan penting:
    - auto_adjust=False: kita simpan harga aktual (tidak diadjust) supaya level
      SL/TP realistis; dividen kecil di IDX diabaikan, tapi STOCK SPLIT akan
      terdeteksi sebagai outlier oleh scrub -> harus di-handle manual.
    - hanya mendukung 1d (data intraday Yahoo untuk IDX tidak reliabel).
    """
    import yfinance as yf

    if timeframe != "1d":
        raise ValueError("IDX via yfinance hanya mendukung timeframe 1d")
    sym = ticker if ticker.endswith(".JK") else f"{ticker.upper()}.JK"
    raw = yf.download(sym, period=f"{years}y", interval="1d", auto_adjust=False,
                      progress=False, threads=False)
    if raw is None or raw.empty:
        raise RuntimeError(f"yfinance tidak mengembalikan data untuk {sym}")
    if isinstance(raw.columns, pd.MultiIndex):
        raw.columns = raw.columns.get_level_values(0)
    raw = raw.rename(columns={"Open": "open", "High": "high", "Low": "low",
                              "Close": "close", "Volume": "volume"})
    # Yahoo memberi tanggal lokal tanpa tz; tandai sebagai 16:00 Asia/Jakarta = TUTUP sesi,
    # supaya timestamp bar = saat semua informasinya benar-benar tersedia.
    idx = pd.to_datetime(raw.index).tz_localize("Asia/Jakarta") + pd.Timedelta(hours=16)
    raw.index = idx.tz_convert("UTC")
    # yfinance kadang menyertakan bar hari ini yang belum tutup; buang jika sesi belum selesai.
    df = _finalize(raw, timeframe, drop_open_bar=False)
    # bar hari ini hanya sah bila sesi sudah tutup (16:00 WIB)
    now_utc = pd.Timestamp.now(tz="UTC")
    if len(df) and df.index[-1] > now_utc:
        df = df.iloc[:-1]
    return df


def load_csv(path: str, timeframe: str, continuous: bool = True) -> pd.DataFrame:
    """CSV dengan kolom ts/timestamp/date + OHLCV. ts diasumsikan UTC bila tanpa tz.

    continuous=False (IDX): bar harian sudah ditandai pada jam tutup sesi oleh load_idx,
    jadi aturan "bar belum tutup" (ts + TF > sekarang) TIDAK boleh dipakai — itu akan
    membuang bar kemarin setiap pagi.
    """
    raw = pd.read_csv(path)
    cols = {c.lower(): c for c in raw.columns}
    tcol = next((cols[c] for c in ("ts", "timestamp", "date", "datetime", "time") if c in cols), None)
    if tcol is None:
        raise ValueError("CSV harus punya kolom waktu (ts/timestamp/date)")
    raw = raw.rename(columns={cols[c]: c for c in COLUMNS if c in cols})
    raw.index = pd.to_datetime(raw[tcol], utc=True)
    return _finalize(raw, timeframe, drop_open_bar=continuous)


def load(symbol: str, market: str, timeframe: str, cache: bool = True, **kw) -> pd.DataFrame:
    """Dispatcher + cache parquet sederhana (cache dipakai maksimal 1 timeframe lamanya)."""
    CACHE_DIR.mkdir(exist_ok=True)
    key = f"{market}_{symbol.replace('/', '-').replace(':', '_')}_{timeframe}.parquet"
    path = CACHE_DIR / key
    if cache and path.exists():
        age = time.time() - path.stat().st_mtime
        if age < TIMEFRAME_SECONDS[timeframe]:
            return pd.read_parquet(path)
    if market in ("crypto_spot", "crypto_perp"):
        df = load_crypto(symbol, timeframe, **kw)
    elif market == "idx":
        df = load_idx(symbol, timeframe, **kw)
    else:
        raise ValueError(f"market tidak dikenal: {market}")
    if cache:
        try:
            df.to_parquet(path)
        except Exception:
            pass
    return df
