awal = int(input("Masukkan nilai awal : "))
akhir = int(input("Masukkan nilai awal : "))

print(awal)
print(akhir)


def tambah(a, b):
    return a + b 

def pengurangan(a,b) :
    return a - b

def perkalian(a,b) :
    return a * b

def pembagian(a,b) :
    return a / b


print("===================================================")
print("||        MENU UNTUK KALKULATOR SEDERHANA        ||")
print("===================================================")
print("||   1 . Penjumlahan                             ||")
print("||   2 . Pengurangan                             ||")
print("||   3 . Perkalian                               ||")
print("||   4 . Pembagian                               ||")
print("===================================================")
pilihan = int(input("Masukkan Pilihan\n=> "))

if pilihan == 1 :
    print(tambah(awal, akhir))
    
elif pilihan == 2 :
    print(pengurangan(awal, akhir))
    

elif pilihan == 3 :
    print(perkalian(awal, akhir))

elif pilihan == 4 :

    if akhir == 0 : 
        print("Tidak bisa dibagi 0")
    else :
        print(pembagian(awal, akhir))

    # try :
    #     print(pembagian(awal, akhir))
    # except :
    #     print("tidak bisa dibagi 0")


