import fungsikalkulatorsederhana

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
        print(fungsikalkulatorsederhana.tambah(awal,akhir))

    if pilihan == 2:
        print (fungsikalkulatorsederhana.kurang(akhir, awal))

    elif pilihan == 3:
        print (fungsikalkulatorsederhana.perkalian(akhir, awal))

    elif pilihan == 4:
        
        if akhir == 0:
            print ("angka tidak bisa dibagi")
        else:
            print (fungsikalkulatorsederhana.bagi(akhir, awal))
    else:
        print ("pilihan tidak valid")

    hitunglagi = input("Apakah Anda Ingin Menggunakan Kalkulator lagi (y/n)?")
    if hitunglagi.lower() != 'y':
        print ("Program Selesai")
        break
    




