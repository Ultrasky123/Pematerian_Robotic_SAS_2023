def tambah(a,b):
    return  a + b

def kurang(a,b):
    return  a - b

def kali(a,b):
    return  a * b

def bagi(a,b):
    return  a / b


while True:

    print("===== PROGRAM KALKULATOR  =====")
    
    print("1. Penjumlahan")
    print("2. Pegurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Exit")
    pilihan = int(input("Masukkan pilihan : "))


    if pilihan == 1:
        a = int(input("Masukkan nilai a : "))
        b = int(input("Masukkan nilai b : "))
        print("Hasil :",tambah(a, b))
    elif pilihan == 2:
        a = int(input("Masukkan nilai a : "))
        b = int(input("Masukkan nilai b : "))
        print("Hasil :",kurang(a, b))
    elif pilihan == 3:
        a = int(input("Masukkan nilai a : "))
        b = int(input("Masukkan nilai b : "))
        print("Hasil :",kali(a, b))
    elif pilihan == 4:
        a = int(input("Masukkan nilai a : "))
        b = int(input("Masukkan nilai b : "))
        if b != 0:
            print("Angka tidak bisa dibagi dengan 0")
        else: 
            print("Hasil :",bagi(a, b))
    elif pilihan == 5:
        break
    else:
        print("Input invalid")