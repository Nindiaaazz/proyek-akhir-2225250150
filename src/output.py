
def tampilkan_laporan(siswa, statistik):
    print("\n===== LAPORAN ANALISIS NILAI MATEMATIKA =====")

    for data in siswa:
        print(f"Nama: {data['nama']}")
        print(f"Nilai: {data['nilai']}")
        print(f"Status: {data['status']}")
        print("----------------------------------")

    print(f"Rata-rata nilai: {statistik['rata_rata']:.2f}")
    print(f"Nilai tertinggi: {statistik['tertinggi']}")
    print(f"Nilai terendah: {statistik['terendah']}")
    print(f"Jumlah siswa lulus: {statistik['jumlah_lulus']}")
    print(f"Jumlah siswa belum lulus: {statistik['jumlah_belum_lulus']}")


def simpan_laporan(siswa, statistik):
    with open("laporan_nilai.txt", "w", encoding="utf-8") as file:
        file.write("LAPORAN ANALISIS NILAI MATEMATIKA\n")
        file.write("==================================\n\n")

        for data in siswa:
            file.write(f"Nama: {data['nama']}\n")
            file.write(f"Nilai: {data['nilai']}\n")
            file.write(f"Status: {data['status']}\n\n")

        file.write(f"Rata-rata: {statistik['rata_rata']:.2f}\n")
        file.write(f"Nilai tertinggi: {statistik['tertinggi']}\n")
        file.write(f"Nilai terendah: {statistik['terendah']}\n")
        file.write(f"Jumlah lulus: {statistik['jumlah_lulus']}\n")
        file.write(f"Jumlah belum lulus: {statistik['jumlah_belum_lulus']}\n")

    print("\nLaporan berhasil disimpan ke laporan_nilai.txt")
