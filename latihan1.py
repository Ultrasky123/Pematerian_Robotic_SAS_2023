#aritmatika dasar
awal = int(input ("masukan nilai awal = "))
akhir = int(input("masukan nilai akhir= "))

#print(awal)
#print(akhir)

def tambah (a,b):
    return a+b
#print(tambah (awal,akhir))

def perkalian (a,b):
    return a*b
#print(perkalian(awal,akhir))

def pengurangan(a,b):
    return a-b
#print(pengurangan(awal,akhir))

def pembagian(a,b):
    return a/b
#print(pembagian(awal,akhir))

print("program kalkulator sederhana")
print ("1.Penjumlahan")
print ("2.Pengurangan")
print ("3.Perkalian")
print ("4.Pembagian")
pilihan = int(input("masukan pilihan = "))

if pilihan ==1 :
    print(tambah(awal,akhir))

if pilihan ==2 :
    print(pengurangan(awal,akhir))

if pilihan ==3 :
    print(perkalian(awal,akhir))

if pilihan ==4 :
    if akhir == 0:
        print ("angka tidak bisa dibagi dengan angka nol")
    
    else:
        print(pembagian(awal,akhir))