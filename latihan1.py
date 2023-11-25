# module
import calfunc

awal = int(input("masukkan nilai awal = "))
akhir = int(input("masukkan nilai akhir= "))

print("PROGRAM KALKULATOR SEDERHANA")
print("1. PENJUMLAHAN")
print("2. PENGURANGAN")
print("3. PERKALIAN")
print("4. PEMBAGIAN")

pilihan=int(input("Masukkan pilihan = "))

if pilihan == 1:
    print(calfunc.tambah(awal,akhir))
if pilihan == 2:
    print(calfunc.kurang(awal,akhir))
if pilihan == 3:
    print(calfunc.kali(awal,akhir))
if pilihan == 4:
    if akhir == 0:
        print("tidak bisa dibagi")
    else :
        print(calfunc.kurang(awal,akhir))
   


