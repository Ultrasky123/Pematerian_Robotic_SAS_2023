import CalFunc

awal = int(input("Masukkan nilai awal = "))
akhir = int(input("Masukkan nilai akhir = "))

print("Ini Nilai Awal = ", awal)
print("Ini Nilai Awal = ", akhir)

print("PROGRAM CALCULATOR SEDERHANA")
print(" 1. Pertambahan")
print(" 2. Pengurangan")
print(" 3. Pengkalian")
print(" 4. Pembagian")
pilihan = int(input("Enter Pilihan : "))

if pilihan == 1:
    print(awal, " + ", akhir, " = ", CalFunc.tambah(awal, akhir))
elif pilihan == 2:
    print(awal, " - ", akhir, " = ", CalFunc.kurang(awal, akhir))
elif pilihan == 3:
    print(awal, " * ", akhir, " = ", CalFunc.kali(awal, akhir))
elif pilihan == 4:
    if akhir == 0:
        print("Tidak bisa dibagi 0")
    else:
        print(awal, " / ", akhir, " = ", CalFunc.bagi(awal, akhir))
else:
    print("Invalid Input")

