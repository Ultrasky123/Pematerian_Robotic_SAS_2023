awal = int(input("Masukan Nilai Awal = "))
akhir = int(input("Masukan Nilai Akhir = "))

print( "Nilai Awal", awal)
print("Nilai Akhir", akhir)

print(" ")

def pertambah(a,b) :
    return a + b

def pengkurangan(a,b) :
    return a - b

def pengkalian(a,b) :
    return a * b

def pembagian(a,b) :
    return a / b

print("Beberapa Pilihan Operasi")
print("1. tambah")
print("2. kurang")
print("3. kali")
print("4. bagi")

pilihan = int(input("Input Operasi = "))

if pilihan == 1:
    print (tambah(awal,akhir))

elif pilihan == 2:
    print (kurang(awal,akhir))
elif pilihan == 3:
    print (kali(awal,akhir))
elif pilihan == 4:
    if akhir == 0:
        print("Tidak bisa dibagi 0")
    else:
        print (bagi(awal,akhir))
else:
    print ("Masukan pilihan operasi yang benar")