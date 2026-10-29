
def input_data():
    """Memasukkan data nama dan nilai siswa."""
    data_siswa = []

    while True:
        try:
            jumlah = int(input("Masukkan jumlah siswa: "))
            if jumlah > 0:
                break
            print("Jumlah siswa harus lebih dari 0.")
        except ValueError:
            print("Input harus berupa bilangan bulat.")

    for i in range(jumlah):
        print(f"\nData siswa ke-{i + 1}")

        nama = input("Masukkan nama siswa: ").strip()
        while nama == "":
            print("Nama tidak boleh kosong.")
            nama = input("Masukkan nama siswa: ").strip()

        while True:
            try:
                nilai = float(input("Masukkan nilai matematika (0-100): "))

                if 0 <= nilai <= 100:
                    break

                print("Nilai harus berada antara 0 sampai 100.")
            except ValueError:
                print("Nilai harus berupa angka.")

        data_siswa.append({
            "nama": nama,
            "nilai": nilai
        })

    return data_siswa


def hitung_statistik(data_siswa):
    """Menghitung statistik nilai siswa."""
    nilai_siswa = [siswa["nilai"] for siswa in data_siswa]

    rata_rata = sum(nilai_siswa) / len(nilai_siswa)
    nilai_tertinggi = max(nilai_siswa)
    nilai_terendah = min(nilai_siswa)

    return rata_rata, nilai_tertinggi, nilai_terendah


def tentukan_status(data_siswa, kkm=75):
    """Menentukan status kelulusan setiap siswa."""
    for siswa in data_siswa:
        if siswa["nilai"] >= kkm:
            siswa["status"] = "Lulus"
        else:
            siswa["status"] = "Belum Lulus"

    return data_siswa


def tampilkan_laporan(data_siswa):
    """Menampilkan laporan analisis nilai."""
    rata_rata, tertinggi, terendah = hitung_statistik(data_siswa)

    jumlah_lulus = sum(
        1 for siswa in data_siswa
        if siswa["status"] == "Lulus"
    )
    jumlah_belum_lulus = len(data_siswa) - jumlah_lulus

    print("\n===== LAPORAN ANALISIS NILAI MATEMATIKA =====")
    print(f"{'Nama':<20} {'Nilai':>8} {'Status':<15}")
    print("-" * 45)

    for siswa in data_siswa:
        print(
            f"{siswa['nama']:<20} "
            f"{siswa['nilai']:>8.2f} "
            f"{siswa['status']:<15}"
        )

    print("-" * 45)
    print(f"Rata-rata nilai  : {rata_rata:.2f}")
    print(f"Nilai tertinggi  : {tertinggi:.2f}")
    print(f"Nilai terendah   : {terendah:.2f}")
    print(f"Jumlah siswa lulus: {jumlah_lulus}")
    print(f"Belum lulus      : {jumlah_belum_lulus}")


def simpan_laporan(data_siswa):
    """Menyimpan laporan ke file teks."""
    rata_rata, tertinggi, terendah = hitung_statistik(data_siswa)

    jumlah_lulus = sum(
        1 for siswa in data_siswa
        if siswa["status"] == "Lulus"
    )
    jumlah_belum_lulus = len(data_siswa) - jumlah_lulus

    with open("laporan_nilai.txt", "w", encoding="utf-8") as file:
        file.write("LAPORAN ANALISIS NILAI MATEMATIKA\n")
        file.write("=" * 40 + "\n")

        for siswa in data_siswa:
            file.write(
                f"Nama: {siswa['nama']}, "
                f"Nilai: {siswa['nilai']:.2f}, "
                f"Status: {siswa['status']}\n"
            )

        file.write(f"\nRata-rata: {rata_rata:.2f}\n")
        file.write(f"Nilai tertinggi: {tertinggi:.2f}\n")
        file.write(f"Nilai terendah: {terendah:.2f}\n")
        file.write(f"Jumlah siswa lulus: {jumlah_lulus}\n")
        file.write(f"Jumlah siswa belum lulus: {jumlah_belum_lulus}\n")

    print("\nLaporan berhasil disimpan ke laporan_nilai.txt")


def main():
    data_siswa = input_data()
    tentukan_status(data_siswa)
    tampilkan_laporan(data_siswa)
    simpan_laporan(data_siswa)


if __name__ == "__main__":
    main()
