# PROPOSAL PROYEK AKHIR
## Program Analisis Nilai Matematika Siswa Berbasis Python

### 1. Judul Proyek
Program Analisis Nilai Matematika Siswa Berbasis Python.

### 2. Latar Belakang
Pengolahan nilai matematika siswa biasanya dilakukan secara manual sehingga membutuhkan waktu dan berisiko terjadi kesalahan perhitungan. Oleh karena itu, diperlukan program sederhana yang dapat membantu guru mengolah dan menganalisis nilai siswa secara lebih cepat dan tepat.

### 3. Pengguna dan Tujuan
**Pengguna:** Guru matematika.

**Tujuan:**
1. Mempermudah pengolahan nilai matematika siswa.
2. Menghitung rata-rata, nilai tertinggi, dan nilai terendah.
3. Menentukan status kelulusan siswa berdasarkan KKM.
4. Menghasilkan laporan hasil analisis nilai.

### 4. Ruang Lingkup
Program dibuat menggunakan Python dan dijalankan melalui terminal di VS Code.

Fitur program meliputi:
1. Memasukkan nama dan nilai siswa.
2. Memvalidasi nilai agar berada pada rentang 0–100.
3. Menghitung rata-rata, nilai tertinggi, dan nilai terendah.
4. Menentukan status siswa berdasarkan KKM 75.
5. Menampilkan dan menyimpan laporan hasil analisis ke file teks.

Program ini tidak menggunakan database dan antarmuka grafis.

### 5. Kebutuhan Program

**Kebutuhan fungsional:**
- F01: Program menerima jumlah siswa, nama, dan nilai.
- F02: Program memeriksa apakah nilai berada pada rentang 0–100.
- F03: Program menghitung rata-rata nilai siswa.
- F04: Program menentukan nilai tertinggi dan terendah.
- F05: Program menentukan status siswa berdasarkan KKM 75.
- F06: Program menampilkan hasil analisis.
- F07: Program menyimpan laporan ke file teks.

**Kebutuhan nonfungsional:**
- Program dibuat menggunakan bahasa Python.
- Program dapat dijalankan melalui terminal VS Code.
- Program memiliki kode yang mudah dipahami.
- Program memberikan pesan apabila input tidak valid.

### 6. Input, Proses, dan Output (IPO)

**Input:**
- Jumlah siswa.
- Nama setiap siswa.
- Nilai matematika setiap siswa.
- KKM sebesar 75.

**Proses:**
1. Menerima data siswa.
2. Memvalidasi nama dan nilai yang dimasukkan.
3. Menghitung rata-rata, nilai tertinggi, dan nilai terendah.
4. Menentukan status setiap siswa berdasarkan KKM.
5. Menyusun dan menyimpan laporan.

**Output:**
- Daftar nama dan nilai siswa.
- Status setiap siswa, yaitu Lulus atau Belum Lulus.
- Nilai rata-rata, tertinggi, dan terendah.
- Jumlah siswa yang lulus dan belum lulus.
- File laporan hasil analisis.

### 7. Algoritma dan Pseudocode

**Algoritma:**
1. Mulai program.
2. Masukkan jumlah siswa.
3. Masukkan nama dan nilai setiap siswa.
4. Periksa validitas input.
5. Jika input tidak valid, minta pengguna memasukkan ulang data.
6. Hitung rata-rata, nilai tertinggi, dan nilai terendah.
7. Tentukan status kelulusan setiap siswa berdasarkan KKM 75.
8. Tampilkan hasil analisis.
9. Simpan laporan ke file teks.
10. Selesai.

**Pseudocode:**
```text
MULAI
    INPUT jumlah_siswa

    UNTUK setiap siswa
        INPUT nama
        INPUT nilai

        SELAMA nilai tidak valid
            TAMPILKAN pesan kesalahan
            INPUT ulang nilai
        AKHIR SELAMA
    AKHIR UNTUK

    HITUNG rata-rata
    CARI nilai tertinggi
    CARI nilai terendah

    UNTUK setiap siswa
        JIKA nilai >= 75
            status = "Lulus"
        JIKA TIDAK
            status = "Belum Lulus"
        AKHIR JIKA
    AKHIR UNTUK

    TAMPILKAN hasil analisis
    SIMPAN laporan ke file teks
SELESAI
```

### 8. Struktur Program

Program direncanakan memiliki beberapa fungsi berikut:
- `input_data()`: menerima data siswa.
- `validasi_nilai()`: memeriksa validitas nilai.
- `hitung_statistik()`: menghitung rata-rata, nilai tertinggi, dan nilai terendah.
- `tentukan_status()`: menentukan status kelulusan siswa.
- `tampilkan_laporan()`: menampilkan hasil analisis.
- `simpan_laporan()`: menyimpan laporan ke file teks.
- `main()`: menjalankan keseluruhan program.

Rencana struktur folder:

```text
proyek-akhir-2225250150/
├── README.md
├── proposal.md
├── .gitignore
├── src/
│   ├── main.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   └── test_case.md
└── output/
    └── .gitkeep
```

### 9. Struktur Data
Struktur data yang digunakan:
- **List:** menyimpan kumpulan nama dan nilai siswa.
- **Dictionary:** menyimpan data setiap siswa, seperti nama, nilai, dan status.
- **String:** menyimpan nama siswa dan keterangan kelulusan.
- **File teks:** menyimpan laporan hasil analisis.

### 10. Rencana Pengujian

| No. | Kasus Pengujian | Input | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Nilai normal | 80, 70, 90 | Rata-rata 80, tertinggi 90, terendah 70 |
| TC02 | Nilai minimum | 0 | Nilai diterima dan status Belum Lulus |
| TC03 | Nilai maksimum | 100 | Nilai diterima dan status Lulus |
| TC04 | Nilai di atas batas | 105 | Program menolak nilai dan meminta input ulang |
| TC05 | Input bukan angka | abc | Program menampilkan pesan kesalahan dan meminta input ulang |
| TC06 | Nilai sama dengan KKM | 75 | Status Lulus |
| TC07 | Semua siswa lulus | 80, 85, 90 | Semua siswa dinyatakan Lulus |
| TC08 | Jumlah siswa tidak valid | 0 atau bilangan negatif | Program menolak jumlah siswa |

Pengujian akan dilakukan setelah program selesai dibuat. Hasil pengujian sebenarnya akan dicatat pada dokumentasi proyek.

### 11. Pembagian Tugas
Proyek ini dikerjakan secara individu. Seluruh proses, mulai dari perancangan, penulisan kode Python, pengujian, perbaikan kesalahan, hingga dokumentasi, dilakukan oleh penulis. AI dapat digunakan sebagai alat bantu, tetapi program tetap dijalankan dan diuji secara mandiri.

### 12. Jadwal Pengerjaan

| Pertemuan | Kegiatan |
|---|---|
| Pertemuan 14 | Menentukan ide proyek dan menyusun proposal |
| Pertemuan 15 | Membuat program Python, menjalankan program, melakukan minimal lima pengujian, memperbaiki kesalahan, dan melengkapi README.md |
| Pertemuan 16 | Menyiapkan demonstrasi dan evaluasi proyek, jika diperlukan |

### 13. Repository GitHub
Nama repository: `proyek-akhir-2225250150`

URL repository: Diisi setelah repository dibuat di GitHub.