import tkinter as tk
import math
# membuat kalkulator menggunakan gui
class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Sederhana") # judul untuk window

        self.entry = tk.Entry(root, width=20, font=('Arial', 16))
        self.entry.grid(row=0, column=0, columnspan=4) # membuat entry untuk menampilkan angka

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        row = 1
        col = 0
        # membuat button untuk kalkulator
        for button in buttons:
            tk.Button(root, text=button, width=5, height=3, font=('Arial', 14),
                      command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1
    # fungsi yang akan berjaln jika button di klik
    def on_button_click(self, value):
        if value == '=':
            try: # melakukan evaluasi pada string yang di inputkan pada entry
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except: # jika terjadi error maka akan menampilkan error pada entry
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif value == 'C': # jika button C di klik maka akan menghapus semua yang ada di entry
            self.entry.delete(0, tk.END)
        else: # jika button selain = dan C di klik maka akan menambahkan value ke entry
            self.entry.insert(tk.END, value)

# membuat kalkulator menggunakan command line
class Kalkulator:
    def __init__(self, nilai):
        self.nilai = float(nilai)
    # melakukan operasi matematika menggunakan overloading operator
    def __add__(self, other):
        return Kalkulator(self.nilai + other.nilai)

    def __sub__(self, other):
        return Kalkulator(self.nilai - other.nilai)

    def __mul__(self, other):
        return Kalkulator(self.nilai * other.nilai)

    def __truediv__(self, other):
        if other.nilai == 0:
            raise ValueError("Tidak dapat dibagi dengan 0!!")
        return Kalkulator(self.nilai / other.nilai)

    def __pow__(self, other):
        return Kalkulator(self.nilai ** other.nilai)

    def __str__(self):
        return str(self.nilai)


def logaritma(nilai):
    if nilai <= 0:
        raise ValueError("Logaritma hanya didefinisikan untuk bilangan positif!")
    return Kalkulator(math.log10(nilai))

# main program untuk menjalankan kalkulator
def main():
    while True:
        print("\n====== Kalkulator Sederhana ======")
        print("Operasi: ( +, -, *, /, ^, log )")
        print("Ketik 'exit' untuk keluar")

        try:
            user = input("Masukkan operasi: ").lower()

            if user == "exit":
                print("Terima kasih telah menggunakan kalkulator ini")
                break

            if user == "log":
                nilai1 = float(input("Masukkan nilai: "))
                hasil = logaritma(nilai1)
                print(f"Log {nilai1} = {hasil}")
            else:
                angka1 = float(input("Masukkan bilangan pertama: "))
                angka2 = float(input("Masukkan bilangan kedua: "))

                nilai1 = Kalkulator(angka1)
                nilai2 = Kalkulator(angka2)

                if user == "+":
                    hasil = nilai1 + nilai2
                elif user == "-":
                    hasil = nilai1 - nilai2
                elif user == "*":
                    hasil = nilai1 * nilai2
                elif user == "/":
                    hasil = nilai1 / nilai2
                elif user == "^":
                    hasil = nilai1 ** nilai2
                else:
                    print("Operasi tidak valid")
                    continue

                print(f"{nilai1} {user} {nilai2} = {hasil}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")


if __name__ == "__main__":
    print("Pilih cara menggunakan kalkulator:")
    print("1. Command Line")
    print("2. GUI")
    try:
        user = int(input("Masukkan pilihan (1/2): "))
        if user == 1:
            main()
        elif user == 2:
            root = tk.Tk()
            app = CalculatorGUI(root)
            root.mainloop()
        else:
            print("Pilihan tidak valid")
    except ValueError:
        print("Input harus berupa angka (1 atau 2)!")