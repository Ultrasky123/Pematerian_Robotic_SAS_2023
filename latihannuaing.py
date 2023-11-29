import fungsilatihannuaing

print("Kalkulator Sederhana")
awal = int(input("Masukan Nilai Awal = "))
akhir = int(input("Masukan Nilai Akhir = "))

print( "Nilai Awal", awal)
print("Nilai Akhir", akhir)
print("Beberapa Pilihan Operasi")
print("1. penambahan")
print("2. pengkurangan")
print("3. pengkalian")
print("4. pembagian")

pilihan = int(input("Input Operasi = "))

if pilihan == 1:
    print (fungsilatihannuaing.penambahan(awal,akhir))
elif pilihan == 2:
    print (fungsilatihannuaing.pengkurangan(awal,akhir))
elif pilihan == 3:
    print (fungsilatihannuaing.pengkalian(awal,akhir))
elif pilihan == 4:
    if akhir == 0:
        print("Tidak bisa dipembagian 0")
    else:
        print (fungsilatihannuaing.pembagian(awal,akhir))
else:
    print ("Masukan pilihan operasi yang benar")