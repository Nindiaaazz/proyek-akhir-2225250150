def input_data():
    siswa = []

    while True:
        try:
            jumlah = int(input("Masukkan jumlah siswa: "))
            if jumlah > 0:
                break
            print("Jumlah siswa harus lebih dari 0.")
        except ValueError:
            print("Input harus berupa angka.")

    for i in range(jumlah):
        print(f"\nData siswa ke-{i + 1}")

        while True:
            nama = input("Masukkan nama siswa: ").strip()
            if nama:
                break
            print("Nama tidak boleh kosong.")

        while True:
            try:
                nilai = float(input("Masukkan nilai matematika: "))

                if 0 <= nilai <= 100:
                    break
                print("Nilai harus antara 0 sampai 100.")

            except ValueError:
                print("Nilai harus berupa angka.")

        siswa.append({
            "nama": nama,
            "nilai": nilai
        })

    return siswa