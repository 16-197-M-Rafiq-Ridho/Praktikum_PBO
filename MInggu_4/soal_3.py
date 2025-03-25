from abc import ABC, abstractmethod

class animal(ABC):
    def __init__(self, name, age, tipe):
        self.__name = name
        self.__age = age
        self.__type = tipe

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name or name.strip() == "":
            raise ValueError("Nama tidak boleh kosong!!")
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0 :
            raise ValueError("umur tidak boleh negatif")
        self.__age = age

    @property
    def tipe(self):
        return self.__type

    @tipe.setter
    def tipe(self, tipe):
        if not tipe or tipe.strip() == "":
             raise ValueError("Tipe tidak boleh kosong!!")
        self.__type = tipe

    @abstractmethod
    def make_sound(self):
        pass

    def tampilkan_info(self):
        print(f"Nama: {self.__name}, Jenis: {self.__type}, Umur: {self.__age}")
        self.make_sound()

class Kucing(animal):
    def make_sound(self):
        print("suara: miaw miaw miaw...")

class Burung(animal):
    def make_sound(self):
        print("suara: cit cit cit...")

class Anjing(animal):
    def make_sound(self):
        print("suara: guk guk guk...")

class Zoo:
    def __init__(self):
        self.__list_hewan = []

    def tambah_hewan(self, hewan):
        self.__list_hewan.append(hewan)
        print(f"Hewan dengan {hewan.name} berhasil di tambah.")

    def tampil_info(self):
        if not self.__list_hewan:
            print("tidak ada hewan dikebun bnatang")
        else:
            for hewan in self.__list_hewan:
                hewan.tampilkan_info()
                print('='*10)

    def cari_hewan(self, nama):
        for hewan in self.__list_hewan:
            if hewan.name.lower() == nama.lower():
                hewan.tampilkan_info()
                return
        print(f"hewan dengan nama '{nama}' tidak ditemukan.")

def main():
    
    kebun_binatang = Zoo()
    while True:
        print("\n=====Kebun binatang Zura=====")
        print("1. Tambah hewan")
        print("2. Tampilkan hewan")
        print("3. Cari hewan")
        print("4. Keluar")
        pilih = int(input("Maukkan pilihan(1/2/3/4): "))

        try:
            if pilih == 1:
                tipe = str(input("Masukkan tipe hewan(Kucing/Burung/Anjing): ")).capitalize()
                nama = str(input("Masukkan nama hewan: "))
                umur = int(input('Masukkan umur hewan: '))
                jenis = str(input("Masukkan jenis: "))

                try:
                    if tipe == "Kucing":
                        hewan = Kucing(nama, umur, jenis)
                    elif tipe == "Burung":
                        hewan = Burung(nama, umur, jenis)
                    elif tipe == "Anjing":
                        hewan = Anjing(nama, umur, jenis)
                    else:
                        print("tipe hewan tidak valid")
                        continue

                    kebun_binatang.tambah_hewan(hewan)

                except ValueError as e:
                    print(f"Error: {e}")

            elif pilih == 2:
                kebun_binatang.tampil_info()
            elif pilih == 3:
                nama = str(input("Masukkan nama hewan yang ingin dicari: "))
                kebun_binatang.cari_hewan(nama)
            elif pilih == 4:
                print("Terimakasih telah menggunakan program:)")
                break
            else:
                print("Pilihan tidak valid")
        except ValueError:
            print(f"Input tidak Valid")

if __name__ == "__main__":
    main()

