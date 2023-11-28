# from bangMain import *
from dataBase import *
from login import *

def menuBank(saldoNow, uname) :

    saldoNow = username1.index(uname)

    # Nabung
    # Tarik Tunai
    # Transfer
    print("=============================")
    print("||        MENU BANK        ||")
    print("=============================")
    print(" Saldo Anda : Rp", saldo[saldoNow])
    print("=============================")
    print("1. Isi Saldo")
    print("2. Tarik Tunai")
    print("3. Tranfer")
    print("4. Info Akun")
    print("0. Keluar")

    x = int(input("Pilihan anda : "))


    if x==1 :
        print("=========================================")
        print("||              ISI SALDO              ||")
        print("=========================================")
        isiSaldo(saldoNow)
        menuBank(saldoNow, uname)
    elif x == 2 :

        kesempatan = 2
        for n in range(3) :
            pinLogin=int(input("MASUKKAN PIN YANG TERDIRI DARI 4 DIGIT\n=> "))
            cek = loginPin(pinLogin)
            if cek == True : 
                 tarikTunai(saldoNow, uname)

            else :
                print("Pin yang anda masukkan salah!!!!!!! Kesempatan tinggal", kesempatan)
                if kesempatan == 0 :
                    print("===================================================")
                    print("||          KESEMPATAN ANDA SUDAH HABIS          ||")
                    print("===================================================")
                
                kesempatan = kesempatan - 1

    elif x == 3 :
        bankName = str(input("Masukkan Nama Bank\n=> "))
        noRekening = int(input("Masukkan No. Rekeneing Tujuan (8 Digit)\n=>"))

        cekNoRek = noRekDataBase.index(noRekening)

        if noRekening == noRekDataBase[cekNoRek] :

            print("SILAHKAN TRANSFER :)")
             
            nominal = int(input("Nominal Transfer\n=>"))

            if nominal > saldo[saldoNow] : 
                print("Saldo anda tidak mencukupi untuk melakukan transfer")

            else : 

                saldo[cekNoRek]= saldo[cekNoRek] + nominal
                saldo[saldoNow] = saldo[saldoNow] - nominal
        else :
            print("NO REKENING TIDAK DITEMUKAN!!!!!!!!!!")

    elif x == 4 :
        print("=============================================")
        print("||            - AKUN ANDA -                ||")
        print("=============================================")
        print("USERNAME\t: ", username1[saldoNow])
        print("PIN ANDA\t: ", pinDataBase[saldoNow])
        print("NO REKENING\t: ", noRekDataBase[saldoNow])




    # elif x ==  0:

    #     main()
        
    else :
        print("Pilihan Tidak Ada")

def isiSaldo(saldoNow) :
    print("Saldo : ", saldo[saldoNow])
    isi = int(input("Isi Berapa ??\n=> "))

    saldo[saldoNow] = saldo[saldoNow] + isi

def tarikTunai(saldoNow, uname) :

        print("SALDO ANDA", saldo[saldoNow])

        tarik = int(input("NOMINAL YANG INGIN ANDA TARIK\n=> Rp "))

        if tarik > saldo[saldoNow] :
             print("==================================================")
             print("||          SALDO ANDA TIDAK MENCUKUPI          ||")
             print("==================================================")
             menuBank(saldoNow, uname)
        else :
             saldo[saldoNow] = saldo[saldoNow]-tarik



