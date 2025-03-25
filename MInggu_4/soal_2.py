class todo:
    def __init__(self):
        self.daftar_tugas = []

    def tambah_tugas(self, tugas):
        self.daftar_tugas.append(tugas)

    def remove_tugas(self, tugas):
        if tugas in self.daftar_tugas:
            self.daftar_tugas.remove(tugas)
        else:
            print("Tugas tidak ditemukan!!")

    def tampilkan_tugas(self):
        if not self.daftar_tugas:
            print("Tidak ada tugas dalam daftar.")
        else:
            print("Daftar Tugas:")
            for i, tugas in enumerate(self.daftar_tugas, 1):
                print(f"{i}. {tugas}")

to_do = todo()
while True:
    try:
        print("\n1. Tambah Tugas")
        print("2. Hapus Tugas")
        print("3. Tampilkan Tugas")
        print("4. Keluar")
        pilihan = int(input("pilihan(1/2/3/4): "))

        if pilihan == 1:
            tugas = str(input("Masukkan tugas: ")).lower()
            to_do1.tambah_tugas(tugas)

        elif pilihan == 2:
            tugas = str(input("Masukkan tugas yang ingin dihapus: ")).lower()
            to_do.remove_tugas(tugas)

        elif pilihan == 3:
            to_do.tampilkan_tugas()

        elif pilihan == 4:
            break

        else:
            raise ValueError("Input tidak valid!!")
    except ValueError as e:
        print(e)
