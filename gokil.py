awal = int(input("Masukkan Nilai awal = "))
akhir = int(input("Masukkan nilai akhir = "))

print(awal)
print(akhir)

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b

print ("PROGRAM KALKULATOR SEDERHANA")
print ("Pilih program : ")
print ("1. Tambah")
print ("2. Kurang")
print ("3. Kali")
print ("4. Bagi")

pilihan = int(input("masukkan pilihan = "))

if pilihan == 1:
    print(tambah(awal, akhir))

if pilihan == 2:
    print(kurang(awal, akhir))

if pilihan == 3:
    print(kali(awal, akhir))

if pilihan == 4:
    print(bagi(awal, akhir))

if pilihan == 4:
    print(bagi(awal, akhir) == 0)
    print("Tidak bisa dibagi 0")
