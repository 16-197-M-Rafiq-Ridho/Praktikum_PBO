
#soal no 1
tinggi = int(input("Masukkan tinggi : "))

for i in range(1, tinggi + 1):
        print(" " * (tinggi - i) + "* " * i)

#soal no 2
jumlah = int(input("Masukkan jumlah mahasiswa: "))
data_maha= {}

for i in range(1, jumlah + 1):
    nama = str(input(f"\nMasukkan nama mahasiswa ke-{i}: "))
    nilai = input(f"Masukkan nilai mahasiswa {nama}: ")
    data_maha[nama] = nilai

print(data_maha)

#soal no 3
file = open("Me.txt", "w")

tulis = input("\nMasukkan nama: ")
nim = input("Masukkan NIM: ")
resolusi = input("Masukkan resolusi tahun ini: ")

file.write(f"\nNama: {tulis}")
file.write(f"\nNIM: {nim}")
file.write(f"\nResolusi tahun ini: {resolusi}")
print(f"file {file} telah di buat.")

file.close()

f = open("Me.txt", "r")
print(f.read())

