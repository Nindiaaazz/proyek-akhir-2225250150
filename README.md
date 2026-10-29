# Program Analisis Nilai Matematika Siswa Berbasis Python

## Deskripsi
Program ini dibuat untuk membantu guru menganalisis nilai matematika siswa secara sederhana menggunakan Python.

## Tujuan
- Menghitung rata-rata nilai siswa.
- Menentukan nilai tertinggi dan terendah.
- Menentukan status kelulusan berdasarkan KKM 75.
- Menampilkan dan menyimpan laporan hasil analisis.

## Fitur
1. Memasukkan nama dan nilai siswa.
2. Memvalidasi nilai dalam rentang 0–100.
3. Menghitung statistik nilai.
4. Menentukan status kelulusan siswa.
5. Menyimpan laporan ke file teks.

## Teknologi
- Python
- Visual Studio Code
- Git dan GitHub

## Cara Menjalankan
Petunjuk menjalankan program akan dilengkapi setelah kode Python selesai dibuat.

## Hasil Pengujian
Hasil pengujian akan dicatat setelah program selesai dijalankan dan diuji.

## Identitas Proyek
- Nama proyek: Program Analisis Nilai Matematika Siswa Berbasis Python
- Repository: `proyek-akhir-2225250150`

## Cara Menjalankan Program

1. Pastikan Python sudah terpasang di komputer.
2. Buka folder proyek di Visual Studio Code.
3. Buka terminal melalui menu Terminal > New Terminal.
4. Jalankan perintah berikut:

   ```powershell
   python src/main.py
   ```

5. Masukkan jumlah siswa, nama siswa, dan nilai matematika sesuai petunjuk program.
6. Periksa hasil analisis yang muncul di terminal.

Jika perintah `python` tidak dikenali, coba gunakan `py src/main.py`.

## Pengujian Program

Program direncanakan dan diuji menggunakan delapan skenario:
1. TC01: Menguji perhitungan nilai normal.
2. TC02: Menguji nilai minimum, yaitu 0.
3. TC03: Menguji nilai maksimum, yaitu 100.
4. TC04: Menguji penolakan nilai di atas 100.
5. TC05: Menguji input nilai berupa teks.
6. TC06: Menguji nilai yang sama dengan KKM 75.
7. TC07: Menguji kondisi semua siswa lulus.
8. TC08: Menguji jumlah siswa yang tidak valid.

Rincian hasil aktual setiap pengujian dicatat dalam file `tests/test_case.md`.

## File Laporan

Setelah program selesai dijalankan, laporan analisis disimpan dalam file `laporan_nilai.txt` di direktori kerja tempat program dijalankan.