
KKM = 75


def tentukan_status(nilai):
    if nilai >= KKM:
        return "Lulus"
    else:
        return "Belum Lulus"


def hitung_statistik(siswa):
    daftar_nilai = [data["nilai"] for data in siswa]

    rata_rata = sum(daftar_nilai) / len(daftar_nilai)
    nilai_tertinggi = max(daftar_nilai)
    nilai_terendah = min(daftar_nilai)

    jumlah_lulus = 0
    jumlah_belum_lulus = 0

    for data in siswa:
        data["status"] = tentukan_status(data["nilai"])

        if data["status"] == "Lulus":
            jumlah_lulus += 1
        else:
            jumlah_belum_lulus += 1

    return {
        "rata_rata": rata_rata,
        "tertinggi": nilai_tertinggi,
        "terendah": nilai_terendah,
        "jumlah_lulus": jumlah_lulus,
        "jumlah_belum_lulus": jumlah_belum_lulus
    }
