import math
import os

def v_kubus(sisi):
    return sisi ** 3
def lp_kubus(sisi):
    return 6 * (sisi ** 2)
def v_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi
def lp_balok(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
def v_prismasegitiga(alas, tinggialas, tinggiprisma):
    return 0.5 * alas * tinggialas* tinggiprisma
def lp_prismasegitiga(alas, tinggialas, tinggiprisma):
    alas_segitiga = 0.5 * alas * tinggialas
    ksegitiga = alas + tinggialas + math.sqrt(alas**2 + tinggialas**2)
    return (2 * alas_segitiga) + (ksegitiga + tinggiprisma)
def v_tabung(jarijari, tinggi):
    return math.pi * (jarijari ** 2) * tinggi
def lp_tabung(jarijari, tinggi):
    return 2 * math.pi * jarijari * (jarijari + tinggi)
def v_bola(jarijari):
    return (4/3) * math.pi * (jarijari ** 3)
def lp_bola(jarijari):
    return 4 * math.pi * (jarijari ** 2)
def v_kerucut(jarijari, tinggi):
    return (1/3) * math.pi * (jarijari ** 2) * tinggi
def lp_kerucut(jarijari, sisi_miring):
    return math.pi * jarijari * (jarijari + sisi_miring)


while True:  
    print("===Menu Bangun Ruang===")
    print("1. Volume")
    print("2. Luas Permukaan")
    print("3. Kembali Ke Menu Utama")
    choice = input("Masukkan Pilihan (1-3): ")

    if choice in ('1'):
        print("===Menu Volume Bangun Ruang===")
        print("1. Volume Kubus")
        print("2. Volume Balok")
        print("3. Volume Prisma Segitiga")
        print("4. Volume Tabung")
        print("5. Volume Bola")
        print("6. Volume Kerucut")
        print("7. Kembali Ke Menu Utama")

        choice = input("Masukkan Pilihan (1-7): ")
        if choice in ('1', '5'):
            try:
                num1 = float(input("Masukkan Angka: "))
            except ValueError:
                print("Input Tidak Valid. Tolong Masukkan Angka")
                continue
            if num1.is_integer():
                num1int = int(num1)
                if choice == '1':
                    print(f"Hasil Volume Kubus: ", {v_kubus(num1int)})
                if choice == '5':
                    print(f"Hasil Volume Bola: ", {v_bola(num1int)})
            else:
                if choice == '1':
                    print(f"Hasil Volume Kubus: ", {v_kubus(num1)})
                if choice == '5':
                    print(f"Hasil Volume Bola: ", {v_bola(num1)})
            next_calculation = (input("Kalkulasi Telah Selesai, Apakah Anda Ingin Kalkulasi Ulang? (y/n)"))
            if next_calculation == 'n':
                os.system('py -3 Main_Menu.py')
                break
        elif choice in ('4', '6'):
            try:
                num1 = float(input("Masukkan Angka Pertama: "))
                num2 = float(input("Masukkan Angka Kedua: "))
            except ValueError:
                print("Input Tidak Valid. Tolong Masukkan Angka")
                continue
            if num1.is_integer() and num2.is_integer():
                num1int = int(num1)
                num2int = int(num2)
                if choice == '4':
                    print(f"Hasil Volume Tabung: ", {v_tabung(num1int, num2int)})
                if choice == '6':
                    print(f"Hasil Volume Kerucut: ", {v_kerucut(num1int, num2int)})
            else:
                if choice == '4':
                    print(f"Hasil Volume Tabung: ", {v_tabung(num1int, num2int)})
                if choice == '6':
                    print(f"Hasil Volume Tabung: ", {v_kerucut(num1int, num2int)})
            next_calculation = (input("Kalkulasi Telah Selesai, Apakah Anda Ingin Kalkulasi Ulang? (y/n)"))
            if next_calculation == 'n':
                os.system('py -3 Main_Menu.py')
                break
        elif choice in ('2', '3'):
            try:
                num1 = float(input("Masukkan Angka Pertama: "))
                num2 = float(input("Masukkan Angka Kedua: "))
                num3 = float(input("Masukkan Angka Ketiga: "))
            except ValueError:
                print("Input Tidak Valid. Tolong Masukkan Angka")
                continue
            if num1.is_integer() and num2.is_integer() and num3.is_integer:
                num1int = int(num1)
                num2int = int(num2)
                num3int = int(num3)
                if choice == '2':
                    print(f"Hasil Volume Balok: ", {v_balok(num1int, num2int, num3int)})
                if choice == '3':
                    print(f"Hasil Volume Prisma Segitiga: ", {v_prismasegitiga(num1int, num2int, num3int)})
            else:
                if choice == '2':
                    print(f"Hasil Volume Balok: ", {v_balok(num1int, num2int, num3int)})
                if choice == '3':
                    print(f"Hasil Volume Prisma Segitiga: ", {v_prismasegitiga(num1int, num2int, num3int)})
            next_calculation = (input("Kalkulasi Telah Selesai, Apakah Anda Ingin Kalkulasi Ulang? (y/n)"))
            if next_calculation == 'n':
                os.system('py -3 Main_Menu.py')
                break
        else:
            print("Kembali Ke Menu Bangun Ruang")
            continue
    elif choice == '2':
        print("===Menu Luas Bangun Ruang===")
        print("1. Luas Permukaan Kubus")
        print("2. Luas Permukaan Balok")
        print("3. Luas Permukaan Prisma Segitiga")
        print("4. Luas Permukaan Tabung")
        print("5. Luas Permukaan Bola")
        print("6. Luas Permukaan Kerucut")
        print("7. Kembali Ke Menu Bangun Ruang")

        choice = input("Masukkan Pilihan (1-7): ")
        if choice in ('1', '5'):
            try:
                num1 = float(input("Masukkan Angka: "))
            except ValueError:
                print("Input Tidak Valid. Tolong Masukkan Angka")
                continue
            if num1.is_integer():
                num1int = int(num1)
                if choice == '1':
                    print(f"Hasil Luas Permukaan Kubus: ", {lp_kubus(num1int)})
                if choice == '5':
                    print(f"Hasil Luas Permukaan Bola: ", {lp_bola(num1int)})
            else:
                if choice == '1':
                    print(f"Hasil Luas Permukaan Kubus: ", {lp_kubus(num1)})
                if choice == '5':
                    print(f"Hasil Luas Permukaan Bola: ", {lp_bola(num1)})
            next_calculation = (input("Kalkulasi Telah Selesai, Apakah Anda Ingin Kalkulasi Ulang? (y/n)"))
            if next_calculation == 'n':
                os.system('py -3 Main_Menu.py')
                break
        elif choice in ('4', '6'):
            try:
                num1 = float(input("Masukkan Angka Pertama: "))
                num2 = float(input("Masukkan Angka Kedua: "))
            except ValueError:
                print("Input Tidak Valid. Tolong Masukkan Angka")
                continue
            if num1.is_integer() and num2.is_integer:
                num1int = int(num1)
                num2int = int(num2)
                if choice == '4':
                    print(f"Hasil Luas Permukaan Tabung: ", {lp_tabung(num1int, num2int)})
                if choice == '6':
                    print (f"Hasil Luas Permukaan Kerucut: ", {lp_kerucut(num1int, num2int)})
            else:
                if choice == '4':
                    print(f"Hasil Luas Permukaan Tabung: ", {lp_tabung(num1, num2)})
                if choice == '6':
                    print(f"Hasil Luas Permukaan Kerucut: ", {lp_kerucut(num1, num2)})
            next_calculation = (input("Kalkulasi Telah Selesai, Apakah Anda Ingin Kalkulasi Ulang? (y/n)"))
            if next_calculation == 'n':
                os.system('py -3 Main_Menu.py')
                break
        elif choice in ('2', '3'):
            try:
                num1 = float(input("Masukkan Angka Pertama: "))
                num2 = float(input("Masukkan Angka Kedua: "))
                num3 = float(input("Masukkan Angka Ketiga: "))
            except ValueError:
                print("Input Tidak Valid. Tolong Masukkan Angka")
                continue
            if num1.is_integer() and num2.is_integer() and num3.is_integer:
                num1int = int(num1)
                num2int = int(num2)
                num3int = int(num3)
                if choice == '2':
                    print(f"Hasil Luas Permukaan Balok: ", {lp_balok(num1int, num2int, num3int)})
                if choice == '3':
                    print(f"Hasil Luas Permukaan Prisma Segitiga: ", {lp_prismasegitiga(num1int, num2int, num3int)})
            next_calculation = (input("Kalkulasi Telah Selesai, Apakah Anda Ingin Kalkulasi Ulang? (y/n)"))
            if next_calculation == 'n':
                os.system('py -3 Main_Menu.py')
                break
    else:
        print("Kembali Ke Menu Utama")
        os.system('py -3 Main_Menu.py')
        break