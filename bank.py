# loop, masukin username password salah 3 kali, pilihan tarik tunai, transfer, nabung, 
def isLanjut():
        isLanjut = input("Apakah anda ingin melanjutkan program (y/n)? ")
        if isLanjut.lower() != 'y':
            print("Program Selesai")
            return False

username = "Must"
password = 123
i = 0
print("---Selamat Datang Di Bank Tanpa Minimal Apapun---")
while True:
    input_username = input("Masukkan Username: ")
    input_password = int(input("Masukkan Password: "))
    if username != input_username or password != input_password:
        print("Username atau Password salah")
        i+=1
        print("Percobaan ke", i, "dari 3")
        if i == 3:
            print("Anda telah melebih jumlah percobaan!. ANDA KELUAR!!!")
            break
    else:
        totalSaldo = 0
        while True:
            print("Masuk ke Menu")
            print("1. Menabung")
            print("2. Transfer")
            print("3. Tarik Tunai")
            print("4. Cek Saldo")
            pilihan = int(input("Masukkan pilihan anda: "))
            if pilihan == 1:
                nabung = int(input("Masukkan uang yang anda ingin tabung: Rp"))
                totalSaldo += nabung
                print("Total saldo anda sekarang Rp", totalSaldo)
                if isLanjut() == False:
                    breaker = True
                    break
            elif pilihan == 2:
                bankTujuan = input("Masukkan bank tujuan: ")
                noRekening = int(input("Masukkan no rekening: "))
                transfer = int(input("Masukkan jumlah transfer: Rp"))
                if totalSaldo >= transfer:
                    totalSaldo -= transfer
                    print("Transfer berhasil menuju bank", bankTujuan, "dengan no rekening", noRekening, "sejumlah", transfer)
                    print("Total saldo anda sekarang Rp", totalSaldo)
                else:
                    print("Saldo anda kurang, segera menabung supaya cepat kaya!!!")    
                if isLanjut() == False:
                    breaker = True
                    break
            elif pilihan == 3:
                tarikTunai = int(input("Masukkan uang yang ingin ditarik: Rp"))
                if totalSaldo >= tarikTunai:
                    totalSaldo -= tarikTunai
                    print("Tarik tunai berhasil sejumlah", tarikTunai)
                    print("Total saldo anda sekarang Rp", totalSaldo)
                else:
                    print("Saldo anda kurang, segera menabung supaya cepat kaya!!!")
                if isLanjut() == False:
                    breaker = True
                    break
            elif pilihan == 4:
                print("Total saldo anda Rp", totalSaldo)
                if isLanjut() == False:
                    breaker = True
                    break
    if breaker:
        break

        


