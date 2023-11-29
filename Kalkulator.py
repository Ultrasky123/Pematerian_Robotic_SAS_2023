def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if a == 0 or b == 0:
        print("Tidak bisa dibagi dengan 0")
        return None
    return a / b

def kalkulator():
    while True:
        awal = int(input("Masukkan Nilai awal = "))
        akhir = int(input("Masukkan nilai akhir = "))

        print(awal)
        print(akhir)

        print("PROGRAM KALKULATOR SEDERHANA")
        print("Pilih program : ")
        print("1. Tambah")
        print("2. Kurang")
        print("3. Kali")
        print("4. Bagi")

        pilihan = int(input("Masukkan pilihan = "))

        if pilihan == 1:
            print(tambah(awal, akhir))
        elif pilihan == 2:
            print(kurang(awal, akhir))
        elif pilihan == 3:
            print(kali(awal, akhir))
        elif pilihan == 4:
            hasil = bagi(awal, akhir)
            if hasil is not None:
                print(hasil)

        ulangi = input("Apakah Anda ingin menghitung kembali? (y/n): ")
        if ulangi.lower() != 'y':
            break

kalkulator()
