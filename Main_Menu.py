import sys
import os

print("===Kalkulator Canggih===")
print("1. Matematika Dasar")
print("2. Bangun Datar")
print("3. Bangun Ruang")
print("4. Pythagoras")
print("5. Keluar")

while True:
    try:
        choice = int(input("Masukkan pilihan (1-6): "))
        if choice < 1 or choice > 6:
            print("Pilihan tidak valid. Silakan pilih antara 1-6.")
            continue
        if choice == 1:
            os.system('py -3 Matematika_Dasar.py')
            break
        if choice == 2:
            os.system('py -3 Bangun_Datar.py')
            break
        if choice == 3:
            os.system('py -3 Bangun_Ruang.py')
            break
        if choice == 4:
            os.system('py -3 Pythagoras.py')
            break
        if choice == 5:
            print("Terima kasih telah menggunakan Kalkulator Canggih!")
            sys.exit()
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")
        continue