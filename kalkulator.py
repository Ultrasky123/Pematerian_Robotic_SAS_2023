print()
print("===== PROGRAM KALKULATOR SEDERHANA =====")
print()

awal = int(input("Masukkan nilai awal : "))
akhir = int(input("Masukkan nilai akhir : "))

print()

print("Nilai awal : ",awal)
print("Nilai akhir : ",akhir)

print()
print("1. Penjumlahan")
print("2. Pegurangan")
print("3. Perkalian")
print("4. Pembagian")
print()

pilihan = int(input("Masukkan pilihan : "))

def tambah(a,b):
    return  a + b

def kurang(a,b):
    return  a - b

def kali(a,b):
    return  a * b

def bagi(a,b):
    return  a / b

if pilihan == 1:
    print("Hasil :",tambah(awal, akhir))
elif pilihan == 2:
    print("Hasil :",kurang(awal, akhir))
elif pilihan == 3:
    print("Hasil :",kali(awal, akhir))
elif pilihan == 4:
    if akhir == 0:
        print("Angka tidak bisa dibagi dengan 0")
    else: 
        print("Hasil :",bagi(awal, akhir))
else:
    print("Input invalid")