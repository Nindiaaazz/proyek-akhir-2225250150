# Dokumentasi Pengujian Program

## Tujuan
Pengujian dilakukan untuk memastikan Program Analisis Nilai Matematika berjalan sesuai dengan kebutuhan.

## Daftar Pengujian

| Kode | Kasus Pengujian | Input | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Nilai normal | 80, 70, 90 | Rata-rata 80, tertinggi 90, terendah 70 |
| TC02 | Nilai minimum | 0 | Nilai diterima dan status Belum Lulus |
| TC03 | Nilai maksimum | 100 | Nilai diterima dan status Lulus |
| TC04 | Nilai di atas batas | 105, lalu 80 | Nilai 105 ditolak dan program meminta input ulang |
| TC05 | Input bukan angka | abc, lalu 80 | Input abc ditolak dan program meminta input ulang |
| TC06 | Nilai sama dengan KKM | 75 | Status Lulus |
| TC07 | Semua siswa lulus | 80, 85, 90 | Semua siswa berstatus Lulus |
| TC08 | Jumlah siswa tidak valid | 0 | Program meminta jumlah siswa yang valid |

## Hasil Pengujian Aktual
Hasil aktual diisi berdasarkan pengujian langsung di VS Code.

| Kode | Hasil Aktual | Status |
|---|---|---|
| TC01 | Isi sesuai hasil yang muncul di terminal | Isi setelah diuji |
| TC02 | Nilai 0 diterima. Rata-rata, nilai tertinggi, dan terendah 0.00. Status Belum Lulus. | Berhasil |
| TC03 | Nilai 100 diterima. Rata-rata, nilai tertinggi, dan terendah 100.00. Status Lulus. | Berhasil |
| TC04 | Nilai 105 ditolak. Nilai 80 diterima dan status Lulus. | Berhasil |
| TC05 | Input abc ditolak. Nilai 80 diterima dan status Lulus. | Berhasil |
| TC06 | Nilai 75 diterima dan siswa berstatus Lulus karena memenuhi KKM. | Berhasil |
| TC07 | Ketiga siswa memperoleh nilai di atas KKM dan semuanya berstatus Lulus. | Berhasil |
| TC08 | Jumlah siswa 0 ditolak. Program meminta jumlah yang valid dan berhasil dilanjutkan setelah dimasukkan 1. | Berhasil |