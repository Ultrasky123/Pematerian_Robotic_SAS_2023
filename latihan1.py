import kalkulator

awal = int(input("masukkan nilai awal = "))
akhir = int(input("masukkan nilai akhir= "))

def tambah(a,b):
    return a + b

def kurang(a,b):
    return a - b

def kali(a,b):
    return a * b

def bagi(a,b):
    return a / b

print("PROGRAM KALKULATOR SEDERHANA")
print("1. PENJUMLAHAN")
print("2. PENGURANGAN")
print("3. PERKALIAN")
print("4. PEMBAGIAN")

pilihan=int(input("Masukkan pilihan = "))

if pilihan == 1:
    print(tambah(awal,akhir))
if pilihan == 2:
    print(kurang(awal,akhir))
if pilihan == 3:
    print(kali(awal,akhir))
if pilihan == 4:
    if akhir == 0:
        print("tidak bisa dibagi")
    else :
        print(kurang(awal,akhir))
   


