import os
def kataKebalik(kata): # Paling Simpel
    return kata[::-1]

def kataKebalik2(kata): # Pakai for loop
    str = "" # String Kosong
    for i in kata:
        # print("i = ", i)
        str = i + str 
        # print ("str = ", str)
    return str

def main():
    kata = str(input("Masukkan kata: "))
    kata = kata.lower()
    if kata == kataKebalik2(kata=kata):
        print("True") 
    else:
        print("False")

if __name__ == '__main__':
    main()
    while True:
        lanjut = str(input("Apakah anda ingin memasukkan kata lagi (y/n)? "))
        if lanjut.lower() == 'y':
            os.system('clear')
            main()
        else:
            print("Program Selesai")
            break