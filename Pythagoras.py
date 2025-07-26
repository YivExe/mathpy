import os
import math

def sisi_miring(b, c, d, e):
    sisi_lurus = b ** c
    sisi_tegak = d ** e
    return math.sqrt (sisi_lurus + sisi_tegak)
def sisi_lurus(b, c, d, e):
    sisi_miring = b ** c
    sisi_tegak = d ** e
    return math.sqrt (sisi_miring - sisi_tegak)
def sisi_tegak(b, c, d, e):
    sisi_miring = b ** c
    sisi_lurus = d ** e
    return math.sqrt (sisi_miring - sisi_lurus)

while True:
    print("===Menu Pythagoras===")
    print("1. Mencari Sisi Miring")
    print("2. Mencari Sisi Lurus")
    print("3. Mencari Sisi Tegak")
    print("4. Kembali Ke Menu Utama")
    choice = input("Masukkan Pilihan (1-4)")
    if choice == ('1'):
        try:
            num1 = int(input("Masukkan Angka Sisi Lurus: "))
            num2 = int(input("Masukkan Pangkat Pada Angka Sisi Lurus: "))
            num3 = int(input("Masukkan Angka Sisi Tegak: "))
            num4 = int(input("Masukkan Pangkat Pada Angka Sisi Tegak: "))
        except ValueError:
            print("Input Tidak Valid. Tolong Masukkan Angka")
            continue
        print(f"Hasil Sisi Miring: {math.sqrt(sisi_miring(num1, num2, num3, num4))}")
        next_calculation = (input("Kalkulasi Telah Selesai, Apakah Anda Ingin Kalkulasi Ulang? (y/n)"))
        if next_calculation == 'n':
            os.system('py -3 Main_Menu.py')
            break
    elif choice == ('2'):
        try:
            num1 = int(input("Masukkan Angka Sisi Miring: "))
            num2 = int(input("Masukkan Pangkat Pada Angka Sisi Miring: "))
            num3 = int(input("Masukkan Angka Sisi Tegak: "))
            num4 = int(input("Masukkan Pangkat Pada Angka Sisi Tegak: "))
        except ValueError:
            print("Input Tidak Valid. Tolong Masukkan Angka")
            continue
        print(f"Hasil Sisi Miring: {math.sqrt(sisi_lurus(num1, num2, num3, num4))}")
        next_calculation = (input("Kalkulasi Telah Selesai, Apakah Anda Ingin Kalkulasi Ulang? (y/n)"))
        if next_calculation == 'n':
            os.system('py -3 Main_Menu.py')
            break
    elif choice == ('3'):
        try:
            num1 = int(input("Masukkan Angka Sisi Miring: "))
            num2 = int(input("Masukkan Pangkat Pada Angka Sisi Miring: "))
            num3 = int(input("Masukkan Angka Sisi Lurus: "))
            num4 = int(input("Masukkan Pangkat Pada Angka Sisi Lurus: "))
        except ValueError:
            print("Input Tidak Valid. Tolong Masukkan Angka")
            continue
        print(f"Hasil Sisi Miring: {math.sqrt(sisi_tegak(num1, num2, num3, num4))}")
        next_calculation = (input("Kalkulasi Telah Selesai, Apakah Anda Ingin Kalkulasi Ulang? (y/n)"))
        if next_calculation == 'n':
            os.system('py -3 Main_Menu.py')
            break
    elif choice == ('4'):
        print("Kembali Ke Menu Utama...")
        os.system('py -3 Main_Menu.py')
        break