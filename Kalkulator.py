# Modul
import CalFunc

# Looping terus menerus
while True:
    # Input nilai
    awal = int(input("Masukkan nilai awal = "))
    akhir = int(input("Masukkan nilai akhir = "))

    # Menampilkan nilai
    print("Ini Nilai Awal = ", awal)
    print("Ini Nilai Awal = ", akhir)

    # Program Kalkulator sederhana
    print("PROGRAM CALCULATOR SEDERHANA")
    print(" 1. Pertambahan")
    print(" 2. Pengurangan")
    print(" 3. Pengkalian")
    print(" 4. Pembagian")
    pilihan = int(input("Enter Pilihan : "))

    # Kodisi
    if pilihan == 1:
        print(awal, " + ", akhir, " = ", CalFunc.tambah(awal, akhir)) # Memanggil fungsi CalFunc
    elif pilihan == 2:
        print(awal, " - ", akhir, " = ", CalFunc.kurang(awal, akhir))
    elif pilihan == 3:
        print(awal, " * ", akhir, " = ", CalFunc.kali(awal, akhir))
    elif pilihan == 4:
        if akhir == 0: # Logic jika nilai awal dibagi dengan 0
            print("Tidak bisa dibagi 0")
        else:
            print(awal, " / ", akhir, " = ", CalFunc.bagi(awal, akhir))
    else:
        print("Input tidak valid") # Bersambung ke line 48 jika user tidak input angka 1-4

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
