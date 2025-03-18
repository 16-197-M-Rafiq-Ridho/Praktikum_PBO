import random

class father:
    def __init__(self, gol_ayah):
        self.gol_ayah = gol_ayah.upper()
        self.allele = self._kemungkinan_allele()
    #Mencari kemungkinan allele yang dimiliki berdasarkan golongan darah
    def _kemungkinan_allele(self):
        if self.gol_ayah == "O":
            return ["O", "O"]
        elif self.gol_ayah == "A":
            return ["A", "O"]
        elif self.gol_ayah == "B":
            return ["B", "O"]
        elif self.gol_ayah == "AB":
            return ["A", "B"]
        else:
            raise ValueError("Golongan darah tidak valid")
    #memilih secara allele acak dari fungsi _kemungkinan_allele menggunakan fungsi random.choice()
    def random_allele(self):
        print("memilih allele secara acak dengan perbandingan 50:50")
        return random.choice(self.allele)

class mother:
    def __init__(self, gol_ibu):
        self.gol_ibu = gol_ibu.upper()
        self.allele = self._kemungkinan_allele()

    def _kemungkinan_allele(self):
        if self.gol_ibu == "O":
            return ["O", "O"]
        elif self.gol_ibu == "A":
            return ["A", "O"]
        elif self.gol_ibu == "B":
            return ["B", "O"]
        elif self.gol_ibu == "AB":
            return ["A", "B"]
        else:
            raise ValueError("Golongan darah ibu tidak valid")

    def random_allele(self):
        print("Memilih secara acak allele dengan perbandingan 50:50")
        return random.choice(self.allele)

class child:
    def __init__(self, father, mother):
        self.father = father.random_allele() 
        self.mother = mother.random_allele()
        self.allele = self._kemungkinan_golongan()
    #mencari kemungkinan allele yang dimiliki oleh anak berdasarkan allele yang telah didapat
    def _kemungkinan_golongan(self):
        allele = sorted([self.father, self.mother]) #mengurutkan allele ex: [B, A] -> [B, A] untuk mempermudah inisialisasi
        if allele == ["O", "O"]:
            return "O"
        elif "A" in allele and "B" in allele:
            return "AB"
        elif "A" in allele:
            return "A"
        elif "B" in allele:
            return "B"
    
    def __str__(self):
        print(f"Golongan darah pada anak: {self.allele}")

def main():
    try:
        golongan_ayah = input("Masukkan golongan darah ayah: ")
        golongan_ibu = input("Masukkan golongan darah ibu: ")

        ayah = father(golongan_ayah)
        ibu = mother(golongan_ibu)

        anak = child(ayah, ibu)

        print(f"Allele ayah: {ayah.allele}")
        print(f"Allele ibu: {ibu.allele}")
        print(anak)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()