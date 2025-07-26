import sys
import os

def k_persegi(a):
    return 4 * a
def l_persegi(a):
    return a * a
def k_persegipanjang(a, b):
    return 2 * (a + b)
def l_persegipanjang(a, b):
    return a * b
def k_segitiga(a):
    return a + a + a
def l_segitiga(a, b):
    return 0.5 * a * b
def k_jajargenjang(a):
    return a + a + a + a
def l_jajargenjang(a, b):
    return a * b
def k_ketupat(a):
    return a + a + a + a
def l_ketupat(a, b):
    return 0.5 * a * b
def k_lingkaran(a):
    return 2 * 3.14 * a
def l_lingkaran(a, b=2):
    return 3.14 * (a ** b)

while True:
    print("===Menu Bangun Datar===")
    print("1. Keliling")
    print("2. Luas")
    print("3. Kembali Ke Menu Utama")
    choice = input("Masukkan Pilihan (1-3): ")
    if choice in ('1'):
        print("===Menu Keliling Bangun Datar")
        print("1. Keliling Persegi")
        print("2. Keliling Persegi Panjang")
        print("3. Keliling Segitiga")
        print("4. Keliling Jajar Genjang")
        print("5. Keliling Belah Ketupat")
        print("6. Keliling Lingkaran")
        print("7. Kembali Ke Menu Bangun Datar")

        choice = input("Masukkan Pilihan (1-7): ")
        if choice in ('1', '3', '4', '5' ,'6'):
            try:
                num1 = float(input("Masukkan Angka: "))
            except ValueError:
                print("Input Tidak valid, Silahkan Masukkan Angka")
                continue
            if num1.is_integer():
                num1int = int(num1)
                if choice == '1':
                    print(f"Hasil Keliling Persegi: {k_persegi(num1int)}")
                elif choice == '3':
                    print(f"Hasil Keliling Segitiga: {k_segitiga(num1int)}")
                elif choice == '4':
                    print(f"Hasil Keliling Jajar Genjang: {k_jajargenjang(num1int)}")
                elif choice == '5':
                    print(f"Hasil Keliling Belah Ketupat: {k_ketupat(num1int)}")
                elif choice == '6':
                    print(f"Hasil Keliling Lingkaran: {k_lingkaran(num1int)}")
            else:
                if choice == '1':
                    print(f"Hasil Keliling Persegi: {k_persegi(num1)}")
                elif choice == '3':
                    print(f"Hasil keliling Segitiga: {k_segitiga(num1)}")
                elif choice == '4':
                    print(f"Hasil Keliling Jajar Genjang: {k_jajargenjang(num1)}")
                elif choice == '5':
                    print(f"Hasil Keliling Belah Ketupat: {k_ketupat(num1)}")
                elif choice == '6':
                    print(f"Hasil keliling Lingkaran: {k_lingkaran(num1)}")
            next_calculation = (input("Kalkulasi Telah Selesai, Apakah Anda Ingin Kalkulasi Ulang? (y/n)"))
            if next_calculation == 'n':
                os.system('py -3 Main_Menu.py')
                break

        elif choice in ('2'):
            try:
                num1 = float(input("Masukkan Angka Pertama: "))
                num2 = float(input("Masukkan Angka Kedua: "))
            except ValueError:
                print("Input Tidak Valid, Tolong Masukkan Angka")
                continue
            if num1.is_integer() and num2.is_integer():
                num1int = int(num1)
                num2int = int(num2)
                print(f"Hasil Keliling Persegi Panjang: {k_persegipanjang(num1int, num2int)}")
            else:
                print(f"Hasil Keliling Persegi Panjang: {k_persegipanjang(num1, num2)}")
            next_calculation = (input("Kalkulasi Telah Selesai, Apakah Anda Ingin Kalkulasi Ulang? (y/n)"))
            if next_calculation == 'n':
                os.system('py -3 Main_Menu.py')
                break
        else:
            print("Kembali Ke Menu Bangun Datar")
            continue

    elif choice == ('2'):
        print("===Menu Luas Bangun Datar===")
        print("1. Luas Persegi")
        print("2. Luas Persegi Panjang")
        print("3. Luas Segitiga")
        print("4. Luas Jajar Genjang")
        print("5. Luas Ketupat")
        print("6. Luas Lingkaran")
        print("7. Kembali Ke Menu Bangun Datar")

        choice = input("Masukkan Angka (1-7): ")
        if choice in ('1', '6'):
            try:
                num1 = float(input("Masukkan Angka: "))
            except ValueError:
                print("Input Tidak Valid, Tolong Masukkan Angka")
                continue
            if num1.is_integer():
                num1int = int(num1)
                if choice == '1':
                    print(f"Hasil Luas Persegi: {l_persegi(num1int)}")
                if choice == '6':
                    print(f"Hasil Luas Lingkaran: {l_lingkaran(num1int)}")   
            else:
                if choice == '1':
                    print(f"Hasil Luas Persegi: {l_persegi(num1)}")
                if choice == '6':
                    print(f"Hasil Luas Lingkaran: {l_lingkaran(num1)}")
            next_calculation = (input("Kalkulasi Telah Selesai, Apakah Anda Ingin Kalkulasi Ulang? (y/n)"))
            if next_calculation == 'n':
                os.system('py -3 Main_Menu.py')
                break
        elif choice in ('2', '3', '4', '5'):
            try:
                num1 = float(input("Masukkan Angka Pertama: "))
                num2 = float(input("Masukkan Angka Kedua: "))
            except ValueError:
                print("Input Tidak Valid, Tolong Masukkan Angka")
                continue
            if num1.is_integer() and num2.is_integer():
                num1int = int(num1)
                num2int = int(num2)
                if choice == '2':
                    print(f"Hasil Luas Persegi Panjang: {l_persegipanjang(num1int, num2int)}")
                if choice == '3':
                    print(f"Hasil Luas Segitiga: {l_segitiga(num1int, num2int)}")
                if choice == '4':
                    print(f"Hasil Luas Jajar Genjang: {l_jajargenjang(num1int, num2int)}")
                if choice == '5':
                    print(f"Hasil Luas Belah Ketupat: {l_ketupat(num1int, num2int)}")
            else:
                if choice == '2':
                    print(f"Hasil Luas Persegi Panjang: {l_persegipanjang(num1, num2)}")
                if choice == '3':
                    print(f"Hasil Luas Segitiga: {l_segitiga(num1, num2)}")
                if choice == '4':
                    print(f"Hasil Luas Jajar Genjang: {l_jajargenjang(num1, num2)}")
                if choice == '5':
                    print(f"Hasil Luas Belah Ketupat: {l_ketupat(num1, num2)}")
            next_calculation = (input("Kalkulasi Telah Selesai, Apakah Anda Ingin Kalkulasi Ulang? (y/n)"))
            if next_calculation == 'n':
                os.system('py -3 Main_Menu.py')
                break
        elif choice == ('7'):
            print("Kembali Ke Menu Bangun Datar")
            continue
    else:
        print("Kembali Ke Menu utama")
        os.system ("py -3 Main_Menu.py")
        break

                


