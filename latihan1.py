import fungsikalkulator
isLanjut = True
while isLanjut:
    print("Selamat Datang di Kalkulator Sederhana")
    awal = int(input("Masukkan nilai awal= "))
    akhir = int(input("Masukkan nilai akhir= "))

    print("Nilai awal", awal)
    print("Nilai akhir", akhir)

    print("Kalkulator Sederhana")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    pilihan = int(input("Masukkan Pilihan: "))
    if pilihan == 1:
        print(fungsikalkulator.tambah(awal, akhir)) 
    elif pilihan == 2:
        print(fungsikalkulator.kurang(awal, akhir))
    elif pilihan == 3:
        print(fungsikalkulator.kali(awal, akhir))
    elif pilihan == 4:
        print(fungsikalkulator.bagi(awal, akhir))
    else:
        print("Masukkan pilihan yang benar")
    
    isLanjut = input("Apakah anda ingin melanjutkan (Y/N)? ")
    if isLanjut == 'N' or 'n':
        isLanjut = False
    else:
        isLanjut == True
