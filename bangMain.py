from login import *
from dataBase import *
from bankMenu import menuBank


def inputLogin(x, y, kesempatan):
    for x in range(3) :

        
        uname = str(input("Masukkan Username : "))
        pasw = str(input("Masukkan Password : "))
        y = login(uname, pasw)

        if y == True :

            menuBank()
            main()
            break
        else :

            print("=============================================")
            print("-          Kesempatan anda tinggal", kesempatan, "       -")
            print("=============================================")
            if kesempatan == 0 :
                print("Kesempatan anda sudah habis")
                main()
            kesempatan= kesempatan -1

def main():
    print("==============================================")
    print("||                                          ||")
    print("||             - BANK WANGGA -              ||")
    print("||                                          ||")
    print("==============================================")
    print("   ||             1. Login               ||")
    print("   ||            2. Sign in              ||")
    print("   ||          0. Program Off            ||")
    print("   ========================================")

    opsi = int(input("Masukkan Pilihan : "))


    x = 0
    kesempatan = 2
    y = False



    if opsi == 1 :
        inputLogin(x, y, kesempatan)
    elif opsi == 2 :
        username1.append(str(input("Username : ")))
        pasword1.append(str(input("Password : ")))
        inputLogin(x,y, kesempatan)
    elif opsi == 0 :
        print("============================================================")
        print("-          TERIMAKASIH TELAH PERCAYA KEPADA KAMI           -")
        print("============================================================")
        print(len(pasword1))
    else :
        print("Pilihan tidak ada")
main()


