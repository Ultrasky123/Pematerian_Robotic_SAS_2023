def tambah(a,b):
    return a + b

def perkalian(a,b):
    return a * b

def kurang(a,b):
    return a - b 

def bagi(a,b):
    if b == 0:
        return "Angka Tidak Bisa Dibagi"
    else :
        return a/b
    
    
while True:
    print ("PROGRAM KALKULATOR SEDERHANA")
    awal = int (input("Masukkan nilai awal : "))
    akhir = int (input("Masukkan nilai akhir : "))

    print ("MENU PROGRAM KALKULATOR SEDERHANA")
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

    hitunglagi = input("Apakah Anda Ingin Menggunakan Kalkulator lagi (y/n)?")
    if hitunglagi.lower() != 'y':
        print ("Program Selesai")
        break