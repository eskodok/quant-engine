# Panduan setup (tanpa coding, ±15 menit, semua lewat browser)

Tujuannya: GitHub menjadi "kurir data" yang tiap pagi kerja menarik harga crypto + saham IDX,
menjalankan engine, dan menyimpan hasilnya. Claude (Cowork) lalu membaca hasil itu tiap
07:00 WIB, menambah berita terkini, dan mengirim ringkasan ke kamu.

## Langkah 1 — Akun GitHub
1. Buka https://github.com/signup dan buat akun (gratis). Verifikasi email.

## Langkah 2 — Buat repository
1. Klik tombol **+** kanan atas → **New repository**.
2. Repository name: `quant-engine`. Pilih **Public** (Actions gratis tanpa batas untuk repo publik).
   Kalau mau Private juga bisa (kuota gratis 2.000 menit/bulan, cukup: pemakaian kita ±5 menit/hari).
3. Jangan centang apa pun. Klik **Create repository**.

## Langkah 3 — Upload file engine
1. Ekstrak `quant-engine-v0.5.zip` di komputer/HP. Akan ada folder `quant-engine`.
2. Di halaman repo yang baru dibuat, klik link **uploading an existing file**
   (atau tombol **Add file → Upload files**).
3. Buka folder `quant-engine` hasil ekstrak, **pilih semua isinya** (Ctrl+A / Cmd+A) dan seret
   ke area upload di browser. Pastikan folder `engine`, `scripts`, `tests`, dan `.github` ikut.
   > Mac: folder `.github` tersembunyi. Tekan **Cmd+Shift+.** di Finder agar terlihat, lalu seret.
   > Kalau tetap tidak bisa, lewati folder `.github` dan lakukan Langkah 3b.
4. Tunggu upload selesai, klik **Commit changes** (hijau, di bawah).

### Langkah 3b — hanya jika folder `.github` gagal terupload
1. Di repo, klik tab **Actions** → **set up a workflow yourself**.
2. Ganti nama file di atas menjadi `daily.yml`.
3. Buka file `github-workflow-daily.yml` dari folder hasil ekstrak dengan Notepad/TextEdit,
   copy seluruh isinya, paste ke editor GitHub. Klik **Commit changes**.

## Langkah 4 — Izinkan workflow menulis ke repo
1. Tab **Settings** → menu kiri **Actions → General**.
2. Bagian **Workflow permissions**: pilih **Read and write permissions** → **Save**.

## Langkah 5 — Jalankan pertama kali (uji)
1. Tab **Actions** → klik **Data harian + scan** di kiri → tombol **Run workflow** (kanan) →
   centang **Jalankan juga validasi walk-forward** → **Run workflow**.
2. Tunggu 10–20 menit (ada tanda centang hijau kalau sukses).
3. Cek folder `reports/` di repo: harus ada `daily_scan.md` dan `validation_summary.md`,
   dan `data/fetch_log.md` menunjukkan simbol mana yang OK/GAGAL.
4. Kirim link repo kamu (contoh `https://github.com/namakamu/quant-engine`) ke Claude.
   Claude akan membuat tugas terjadwal 07:00 WIB Senin–Jumat.

Setelah ini semuanya otomatis: GitHub jalan 06:15 WIB Senin–Jumat, Claude jalan 07:00 WIB.

## Mengubah watchlist (kapan saja, dari HP pun bisa)
1. Buka file `watchlist.txt` di repo → ikon **pensil** (Edit).
2. Tambah/hapus baris dengan format `market simbol timeframe`, contoh:
   `crypto_spot AVAX/USDT 4h` atau `idx ANTM 1d`.
3. **Commit changes**. Berlaku pada run berikutnya. Validasi untuk simbol baru baru ada
   setelah run hari Minggu (atau jalankan manual seperti Langkah 5 dengan centang validasi).

## Mengubah modal untuk hitung ukuran posisi
Buka `scripts/run_daily.py` → baris `EQUITY = {...}` → ubah angkanya (IDR untuk idx,
USDT untuk crypto) → Commit.

## Kalau ada yang merah di Actions
Klik run yang gagal → klik job **run** → baca baris merah. Kirim screenshot ke Claude.
Penyebab paling sering: Langkah 4 terlewat (error "permission denied" saat push).
