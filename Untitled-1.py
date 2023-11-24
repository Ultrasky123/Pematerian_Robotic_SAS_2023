

def menu ():
    print('[1]pertambahan\n[2]pengurangan\n[3]perkalian\n[4]pembagian')

def pertambahan (a,b):
    hasil = a + b
    return hasil

def pengurangan (a,b):
    hasil = a - b
    return hasil

def perkalian (a,b):
    hasil = a * b
    return hasil

def pembagian (a,b):
    hasil = a / b
    return hasil

awal = float(input('masukan nilai 1 = '))
akhir = float(input('masukan nilai 2 = '))
menu ()
pilihan = int(input('masukan pilihan = '))


if pilihan == 1 :
    print(pertambahan(awal,akhir))

elif pilihan == 2 :
    print(pengurangan(awal,akhir))

elif pilihan == 3 :
    print(perkalian(awal,akhir))

elif pilihan == 4 :
    print(pembagian(awal,akhir))
    if pembagian < 0:
        print ('tidak bisa di bagi nol')

else :
    print ('tidak ada')
    

