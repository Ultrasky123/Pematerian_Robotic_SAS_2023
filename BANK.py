i = 1
saldo = 1000000

print("======PROGRAM BANK======")
print(" 1. Login")
print(" 0. Exit")
pilihan = int(input("Enter Pilihan : "))

if pilihan == 1:
    while i <= 3:
        password =(input("MASUKKAN PASSWORD : "))
        if password == "123" :
            while True: 
                print("==============")
                print("SALDO =",saldo) 
                print("MENU")
                print("1. TRANSFER")
                print("2. TARIK TUNAI")
                print("3. TABUNG")
                print("4. EXIT")
                pilihmenu = int(input("MASUKKAN PILIHAN MENU : "))
                if pilihmenu == 1 :
                    tujuanbank= (input("BANK TUJUAN = "))
                    nominal=int(input("MASUKKAN NOMINAL = "))
                    saldo = saldo - nominal
                elif pilihmenu == 2:
                    nominal=int(input("BERAPA NOMINAL YANG INGIN DI TARIK = "))
                    saldo = saldo - nominal
                elif pilihmenu == 3 :
                    nominal=int(input("INGIN MENABUNG BERAPA = "))
                    saldo = saldo + nominal
                elif pilihmenu == 4 :
                    print("TERIMA KASIH DAN JANGAN LUPA AMBIL KARTU ATM KEMBALI !!!")
                    flag = True
                    break
                else :
                    print("SILAHKAN MEMILIH PILIHAN YANG TERSEDIA") 

            if flag == True :
                break
        else:
            print("PASSWORD SALAH !!")
        i = i+1
elif pilihan == 0:
    print("TERIMA KASIH DAN JANGAN LUPA AMBIL KARTU ATM KEMBALI !!!")
    SystemExit