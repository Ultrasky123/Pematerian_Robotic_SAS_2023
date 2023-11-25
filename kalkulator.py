print()
print("===== PROGRAM KALKULATOR SEDERHANA =====")
print()

awal = int(input("Masukkan nilai awal : "))
akhir = int(input("Masukkan nilai akhir : "))

print()

print("MASUKKAN PILIHAN")
print("1. Penjumlahan")
print("2. Pegurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Exit")

pilihan = int(input("Masukkan pilihan : "))

def tambah(a,b):
    return  a + b

def kurang(a,b):
    return  a - b

def kali(a,b):
    return  a * b

def bagi(a,b):
    return  a / b

while pilihan != 5 :
    if pilihan == 1:
        print("Hasil :", tambah(awal,akhir))
        print("============")
        pilihan = int(input("Masukkan pilihan : "))
        if pilihan == 5 :
            break 
    elif pilihan == 2:
        print("Hasil :",kurang(awal, akhir))
        print("============")
        pilihan = int(input("Masukkan pilihan : "))
        if pilihan == 5 :
            break
    elif pilihan == 3:
        print("Hasil :",kali(awal, akhir))
        print("============")
        pilihan = int(input("Masukkan pilihan : "))
        if pilihan == 5 :
            break
    elif pilihan == 4:
        if akhir == 0:
            print("Angka tidak bisa dibagi dengan 0")
            print("============")
            pilihan = int(input("Masukkan pilihan : "))
            if pilihan == 5 :
                break
        else: 
            print("Hasil :",bagi(awal, akhir))
            print("============")
            pilihan = int(input("Masukkan pilihan : "))
            if pilihan == 5 :
                break
    else:
        print("Input invalid")
        print("============") 
        pilihan = int(input("Masukkan pilihan : "))
    if pilihan == 5:
        break
    awal = int(input("Masukkan nilai awal : "))
    akhir = int(input("Masukkan nilai akhir : "))
    print("============")