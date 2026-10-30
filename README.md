# Program Analisis Nilai Matematika Siswa Berbasis Python

## 1. Deskripsi Proyek
Program ini dibuat untuk membantu guru dalam mengolah dan menganalisis nilai matematika siswa menggunakan bahasa pemrograman Python.

Program dapat menghitung rata-rata nilai, menentukan nilai tertinggi dan terendah, serta menentukan status kelulusan siswa berdasarkan Kriteria Ketuntasan Minimal (KKM) sebesar 75.

## 2. Fitur Program
1. Memasukkan jumlah siswa.
2. Memasukkan nama dan nilai matematika siswa.
3. Memvalidasi nilai agar berada pada rentang 0–100.
4. Menghitung rata-rata nilai siswa.
5. Menentukan nilai tertinggi dan terendah.
6. Menentukan status kelulusan berdasarkan KKM 75.
7. Menampilkan laporan analisis nilai.
8. Menyimpan laporan ke dalam file teks.

## 3. Teknologi yang Digunakan
- Bahasa pemrograman: Python
- Editor: Visual Studio Code
- Penyimpanan laporan: File teks (.txt)
- Version control: Git dan GitHub

## 4. Struktur Folder
```text
proyek-akhir-2225250150/
├── README.md
├── .gitignore
├── laporan_nilai.txt
├── proposal.md
├── data/
│   └── contoh_data.txt
├── docs/
│   └── screenshot/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── input_data.py
│   ├── proses.py
│   └── output.py
└── tests/
    └── test_case.md
```

## 5. Cara Menjalankan Program
1. Buka folder proyek melalui Visual Studio Code.
2. Buka terminal pada folder utama proyek.
3. Jalankan perintah berikut:

```bash
python -m src.main
```

4. Masukkan jumlah siswa, nama siswa, dan nilai matematika sesuai petunjuk program.
5. Program akan menampilkan hasil analisis dan menyimpan laporan ke file `laporan_nilai.txt`.

## 6. Pengujian Program
Pengujian dilakukan terhadap lima skenario, yaitu:
- Nilai tepat KKM (75).
- Nilai melebihi batas (105).
- Input nilai berupa huruf.
- Jumlah siswa 0.
- Nilai terendah (0).

Seluruh lima pengujian tersebut berhasil dilakukan.

Dokumentasi lengkap tersedia pada folder `tests/test_case.md`.

## 7. Kesimpulan
Program berhasil dibuat untuk membantu proses analisis nilai matematika siswa. Program dapat menerima input yang valid, menolak input yang tidak sesuai, menghitung statistik nilai, menentukan status kelulusan, dan menyimpan laporan dalam file teks.

## 8. Pengembang
Nama: Nindia Najihatuz Zahro  
NIM: 2225250150  
Kelas: PMAT-E-2025  
Program Studi: Pendidikan Matematika