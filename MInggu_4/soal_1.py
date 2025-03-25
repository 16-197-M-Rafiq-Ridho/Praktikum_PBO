import math

while True:
    try: 
        nilai = float(input("Masukkan nilai: "))
        if nilai < 0:
            raise ValueError("Input tidak valid!!. Nilai harus positif")

        print(f"Akar kuadrat dari {nilai} adalah {math.sqrt(nilai)}")
        break

    except ValueError as e:
        if str(e) == "Input tidak valid!!. Nilai harus positif":
            print(e)
        else:
            print("Input tidak valid, Input harus Int!!")
