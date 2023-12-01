import calfunc

print()
print("===== PROGRAM KALKULATOR SEDERHANA =====")
print()

# loop tampilan
while True :
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

    # kondisi
    if pilihan == 1:
        print("Hasil :",calfunc.tambah(awal,akhir))
        print("============")
    elif pilihan == 2:
        print("Hasil :",calfunc.kurang(awal, akhir))
        print("============")
    elif pilihan == 3:
        print("Hasil :",calfunc.kali(awal, akhir))
        print("============")
    elif pilihan == 4:
        if akhir == 0:
            print("Angka tidak bisa dibagi dengan 0")
            print("============")
        else: 
            print("Hasil :",calfunc.bagi(awal, akhir))
            print("============")
    elif pilihan== 5:
        print("SELESAI")
        break
    else:
        print("Input invalid")
        print("============") 
    
   # Loop agar user menginput y/n saja
    while True:
        c = input("Jalankan program lagi? (y/n): ")
        # Menghentikan loop
        if c.lower() == 'n': # c.lower() untuk merubah input menjadi lowercase
            print("Program dimatikan. Terima kasih telah menggunakan!")
            exit()
        # Menjalankan loop
        elif c.lower() == 'y': # c.lower() untuk merubah input menjadi lowercase
            break
        # Meminta user agar input y/n -> loop juga
        else:
            print("Input tidak valid. Harap masukkan y/n")
        