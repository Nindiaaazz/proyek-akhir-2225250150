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
3. Menghitung rata-rata, nilai tertinggi, dan nilai terendah.
4. Menentukan status kelulusan siswa.
5. Menyimpan laporan ke file teks.

## Teknologi
- Python
- Visual Studio Code
- Git dan GitHub

## Struktur Proyek
```text
proyek-akhir-2225250150/
├── README.md
├── proposal.md
├── .gitignore
├── laporan_nilai.txt
├── src/
│   └── main.py
└── tests/
    └── test_case.md
```

## Cara Menjalankan Program
1. Pastikan Python sudah terpasang.
2. Buka folder proyek di VS Code.
3. Pilih menu **Terminal > New Terminal**.
4. Jalankan perintah berikut:

   ```bash
   python src/main.py
   ```

   Jika perintah `python` tidak dikenali, coba:

   ```bash
   py src/main.py
   ```

5. Masukkan jumlah siswa, nama siswa, dan nilai matematika.
6. Lihat hasil analisis yang ditampilkan di terminal.

## Pengujian Program
Program diuji dengan delapan skenario:
1. TC01: nilai normal (80, 70, 90).
2. TC02: nilai minimum (0).
3. TC03: nilai maksimum (100).
4. TC04: nilai di atas batas (105).
5. TC05: input teks (`abc`).
6. TC06: nilai sama dengan KKM (75).
7. TC07: semua siswa lulus.
8. TC08: jumlah siswa tidak valid (0).

Hasil aktual setiap pengujian dicatat dalam file `tests/test_case.md`.

## File Laporan
Setelah program dijalankan, hasil analisis disimpan dalam file `laporan_nilai.txt` di direktori kerja tempat program dijalankan.

## Repository GitHub
https://github.com/Nindiaaazz/proyek-akhir-2225250150