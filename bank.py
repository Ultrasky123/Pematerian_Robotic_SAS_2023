print()
print("=== WELCOME TO A BANK ===")
print()

username = "arya"
password = "asd"
pin = 123
saldo = 0

def cek_saldo():
    print("====== SALDO ======")
    print()
    print("Jumlah Saldo Anda :", saldo)
    print()

    confirm = input("Apakah Anda ingin melakukan transaksi lagi? (y/n) : ")
    print()
    while True:
        if confirm == "y":
            menu_utama()
        elif confirm == "n":
            print("Terima kasih sudah menggunakan layanan kami.")
        break

def transfer():
    print("===== TRANSFER =====")
    print()

    global saldo

    bank_tujuan = input("Bank Tujuan    : ")
    norek_tujuan = int(input("Nomor Rekening : "))
    
    while True: 
        nominal_transfer = int(input("Nominal Uang   : Rp "))
        
        if saldo < nominal_transfer:
            print()
            print("Saldo Anda tidak mencukupi.")
            print()
            menu_utama()
        elif nominal_transfer < 10000:
            print()
            print("!!!Minimal transfer adalah Rp 10000!!!")
            print("Silahkan Masukkan Nominal Kembali")
            print()
        else:
            while True:
                pin_transfer = int(input("PIN            : "))
                print()

                if pin_transfer == pin:
                    print("Transaksi Anda ke Bank", bank_tujuan, "dengan Nomor Rekening", norek_tujuan, "telah berhasil!")
                    print()
                    saldo = saldo - nominal_transfer
                    print("Sisa Saldo Anda :", saldo)
                    print()
                    confirm = input("Apakah Anda ingin melakukan transaksi lagi? (y/n) : ")
                    print()
                    if confirm == "y":
                        menu_utama()
                    elif confirm == "n":
                        print("Terima kasih sudah menggunakan layanan kami.")
                    break
                else:
                    print("PIN salah!")
                    print()
                break
            break

def tarik_tunai():
    print("==== TARIK TUNAI ====")
    print()

    global saldo

    while True:
        nominal_tarik = int(input("Nominal Uang   : Rp "))
        
        if saldo <= 0 or saldo < nominal_tarik:
            print()
            print("Saldo Anda tidak mencukupi.")
            print()
            menu_utama()
        elif nominal_tarik % 50000 != 0:
            print()
            print("Tarik tunai hanya bisa untuk nominal kelipatan Rp 50000")
            print()
        else:
            while True:
                pin_transfer = int(input("PIN            : "))
                print()

                if pin_transfer == pin:
                    print("Penarikan uang sejumlah", nominal_tarik, "telah berhasil!")
                    print()
                    saldo = saldo - nominal_tarik
                    print("Sisa Saldo Anda :", saldo)
                    print()
                    confirm = input("Apakah Anda ingin melakukan transaksi lagi? (y/n) : ")
                    print()
                    if confirm == "y":
                        menu_utama()
                    elif confirm == "n":
                        print("Terima kasih sudah menggunakan layanan kami.")
                    break
                else:
                    print("PIN salah!")
                    print()
                break
            break

def setor_tunai():
    print("===== SETOR TUNAI =====")
    print()

    global saldo

    nominal_setor = int(input("Nominal Uang   : Rp "))
    
    while True:
        pin_transfer = int(input("PIN            : "))
        print()

        if pin_transfer == pin:
            print("Setor tunai sejumlah", nominal_setor, "telah berhasil!")
            print()
            saldo = saldo + nominal_setor
            print("Sisa Saldo Anda :", saldo)
            print()
            confirm = input("Apakah Anda ingin melakukan transaksi lagi? (y/n) : ")
            print()
            if confirm == "y":
                menu_utama()
            elif confirm == "n":
                print("Terima kasih sudah menggunakan layanan kami.")
            break
        else:
            print("PIN salah!")
            print()
        break

def menu_utama():

    print("====== MENU UTAMA ======")
    print()
    print("1. Cek Saldo")
    print("2. Transfer")
    print("3. Tarik Tunai")
    print("4. Setor Tunai")
    print("5. Exit")
    print()

    while True:

        transaksi = int(input("Pilih layanan : "))
        print()

        if transaksi == 1:
            cek_saldo()
            break
        elif transaksi == 2:
            transfer()
            break
        elif transaksi == 3:
            tarik_tunai()
            break
        elif transaksi == 4:
            setor_tunai()
            break
        elif transaksi == 5:
            print("Terima kasih sudah menggunakan layanan kami.")
            break
        else: 
            print("Layanan tidak tersedia! Pilih layanan yang tersedia!")
            print()


def login():    
           
    print("         LOGIN")
    print()

    kesempatan = 0

    while kesempatan < 3:

        input_username = input("Username : ")
        input_password = input("Password : ")

        if input_username == username and input_password == password:
            print()
            print("Anda berhasil masuk!")
            print()
            menu_utama()
            break
        elif kesempatan < 2 and input_username != username and input_password != password:
            print("Username dan Password salah! Silahkan ulangi!")
            kesempatan += 1
            print()
        elif kesempatan == 2 and input_username != username and input_password != password:
            print("Username dan Password salah! Anda telah melebihi batas untuk memasukkan Username dan Password!")
            print()
            break
login()