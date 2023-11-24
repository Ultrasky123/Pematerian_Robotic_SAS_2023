awal = int(input("Masukan Nilai Awal = "))
akhir = int(input("Masukan Nilai Akhir = "))

print( "Nilai Awal", awal)
print("Nilai Akhir", akhir)

print(" ")

def penambahan(a,b) :
    return a + b

def pengkurangan(a,b) :
    return a - b

def pengkalian(a,b) :
    return a * b

def pembagian(a,b) :
    return a / b

print("Beberapa Pilihan Operasi")
print("1. penambahan")
print("2. pengkurangan")
print("3. pengkalian")
print("4. pembagian")

pilihan = int(input("Input Operasi = "))

if pilihan == 1:
    print ("Hasil Penambahan = ", penambahan(awal,akhir))

elif pilihan == 2:
    print ("Hasil pengkurangan = ", pengkurangan(awal,akhir))
elif pilihan == 3:
    print ("Hasil Pengkalian = ", pengkalian(awal,akhir))
elif pilihan == 4:
    if akhir == 0:
        print("Tidak bisa dipembagian 0")
    else:
        print ("Hasil Penambahan = ", pembagian(awal,akhir))
else:
    print ("Masukan pilihan operasi yang benar")