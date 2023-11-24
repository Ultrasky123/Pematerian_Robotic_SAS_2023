awal = int(input("Masukkan nilai awal= "))
akhir = int(input("Masukkan nilai akhir= "))

print("Nilai awal", awal)
print("Nilai akhir", akhir)

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return print("Angka tidak bisa dibagi 0")
    else:
        return a / b

print("Kalkulator Sederhana")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilihan = int(input("Masukkan Pilihan: "))
if pilihan == 1:
    print(tambah(awal, akhir)) 
elif pilihan == 2:
    print(kurang(awal, akhir))
elif pilihan == 3:
    print(kali(awal, akhir))
elif pilihan == 4:
    print(bagi(awal, akhir))
else:
    print("Masukkan pilihan yang benar")
