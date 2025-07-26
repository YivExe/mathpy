import os

def tambah (a, b):
    return a + b
def kurang (a, b):
    return a - b
def kali (a, b):
    return a * b
def bagi (a, b):
    if b == 0:
        return "Tidak bisa dibagi dengan nol"
    return a / b
def pangkat (a, b):
    return a ** b
def akar (a):
    if a < 0:
        return "Tidak bisa mengambil akar dari bilangan negatif"
    return a ** 0.5

while True:    
    print("===Menu Matematika Dasar===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Pangkat")
    print("6. Akar")
    print("7. Kembali ke Menu Utama")
    choice = input("Masukkan pilihan (1-7): ")

    if choice in ('1', '2', '3', '4', '5', '6'):
        try:
            num1 = float(input("Masukkan bilangan pertama: "))
            num2 = float(input("Masukkan bilangan kedua: ")) 
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")
            continue
        if num1.is_integer() and num2.is_integer():
            num1int = int(num1)
            num2int = int(num2)
            if choice == '1':
                print(f"Hasil Penjumlahan: {tambah(num1int, num2int)}")
            elif choice == '2':
                print(f"Hasil Pengurangan: {kurang(num1int, num2int)}")
            elif choice == '3':
                print(f"Hasil Perkalian: {kali(num1int, num2int)}")
            elif choice == '4':
                print(f"Hasil Pembagian: {bagi(num1int, num2int)}")
            elif choice == '5':
                print(f"Hasil Pangkat: {pangkat(num1int, num2int)}")
            elif choice == '6':
                print(f"Hasil Akar: {akar(num1int)}")
        else:
            if choice == '1':
                print(f"Hasil Penjumlahan: {tambah(num1, num2)}")
            elif choice == '2':
                print(f"Hasil Pengurangan: {kurang(num1, num2)}")
            elif choice == '3':
                print(f"Hasil Perkalian: {kali(num1, num2)}")
            elif choice == '4':
                print(f"Hasil Pembagian: {bagi(num1, num2)}")
            elif choice == '5':
                print(f"Hasil Pangkat: {pangkat(num1, num2)}")
            elif choice == '6':
                print(f"Hasil Akar: {akar(num1)}")
        next_calculation = input("Apakah Anda ingin melakukan perhitungan lain? (y/n): ")
        if next_calculation == 'n':
            print("Terima kasih telah menggunakan Kalkulator Canggih!")
            os.system('py -3 MainMenu.py')
    elif choice in ('7'):
        try:
            print("Kembali ke Menu Utama...")
            os.system('py -3 Main_Menu.py')
            break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            continue