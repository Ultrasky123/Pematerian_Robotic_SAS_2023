import rumus

print()
print("===== KALKULATOR SEDERHANA =====")
print()

awal = int(input("Masukkan nilai awal  : "))
akhir = int(input("Masukkan nilai akhir : "))

print()

print("Nilai awal : ",awal)
print("Nilai akhir : ",akhir)

print()
print("1. Penjumlahan")
print("2. Pegurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Selesai")
print()

while True: 

    pilihan = int(input("Masukkan pilihan : "))

    if pilihan == 1:
        print("Hasil :",rumus.tambah(awal, akhir))
        print()
    elif pilihan == 2:
        print("Hasil :",rumus.kurang(awal, akhir))
        print()
    elif pilihan == 3:
        print("Hasil :",rumus.kali(awal, akhir))
        print()
    elif pilihan == 4:
        if akhir == 0:
            print("Angka tidak bisa dibagi dengan 0")
            print()
        else: 
            print("Hasil :",rumus.bagi(awal, akhir))
            print()
    elif pilihan == 5:
        print("Program selesai.")
        print()
        break
    else:
        print("Input invalid")
        print()
        break