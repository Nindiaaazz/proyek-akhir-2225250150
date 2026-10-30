
from .input_data import input_data
from .proses import hitung_statistik
from .output import tampilkan_laporan, simpan_laporan


def main():
    print("======================================")
    print(" PROGRAM ANALISIS NILAI MATEMATIKA")
    print("======================================")

    # Memasukkan data siswa
    siswa = input_data()

    # Menghitung statistik dan status kelulusan
    statistik = hitung_statistik(siswa)

    # Menampilkan laporan
    tampilkan_laporan(siswa, statistik)

    # Menyimpan laporan
    simpan_laporan(siswa, statistik)


if __name__ == "__main__":
    main()
