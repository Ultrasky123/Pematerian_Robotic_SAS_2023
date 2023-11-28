awal = int(input ("Masukkan nilai awal = "))
akhir = int (input ("Masukkan nilai akhir = "))

print(awal)
print(akhir)

def tambah(a,b):
    return a + b
print(tambah(akhir, awal ))

def perkalian(a,b):
    return a * b
print (perkalian(akhir, awal))

def kurang(a,b):
    return a - b 
print (kurang(akhir, awal))

def bagi(a,b):
    return a / b 
print (bagi(akhir, awal))

print ("PROGRAM KALKULATOR SEDERHANA")
print ("1. Penjumlahan")
print ("2. Pengurangan")
print ("3. perkalian")
print ("4. pembagian")
pilihan = int(input("Masukkan pilihan = "))

if pilihan == 1:
    print(tambah(awal,akhir))

if pilihan == 2:
    print (kurang(akhir, awal))

elif pilihan == 3:
    print (perkalian(akhir, awal))

elif pilihan == 4:
    
    if akhir == 0:
        print ("angka tidak bisa dibagi")
    else:
        print (bagi(akhir, awal))
else:
    print ("pilihan tidak valid")

    




