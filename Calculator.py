print("===== PROGRAM KALKULATOR SEDERHANA =====")

a = int(input("Masukkan nilai a : "))
b = int(input("Masukkan nilai b : "))

print("Nilai a : ",a)
print("Nilai b : ",b)

print("1. Penjumlahan")
print("2. Pegurangan")
print("3. Perkalian")
print("4. Pembagian")

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
    print("Hasil :",tambah(a, b))
elif pilihan == 2:
    print("Hasil :",kurang(a, b))
elif pilihan == 3:
    print("Hasil :",kali(a, b))
elif pilihan == 4:
    if b != 0:
        print("Angka tidak bisa dibagi dengan 0")
    else: 
        print("Hasil :",bagi(a, b))
else:
    print("Input invalid")