import os

# Informasi saldo
uang_user = 100000

# Fungsi Kembali Menu
def kembali_menu():
    global c  # Menandakan bahwa 'c' adalah variabel global
    input("Tekan Enter untuk kembali ke Main Menu...")
    os.system('clear')
    print("====== PROGRAM BANK ======")
    print(" 1. Cek Saldo")
    print(" 2. Transfer")
    print(" 3. Nabung")
    print(" 4. Tarik")
    print(" 0. Exit")
    c = input("Enter Pilihan : ")

# Cek Saldo menu
def cek_saldo():
    global uang_user  # Menandakan bahwa 'uang_user' adalah variabel global
    os.system('clear')
    print("====== MENU CEK SALDO ======")
    print(f"Saldo Anda saat ini: {uang_user}")
    kembali_menu()

# Narik menu
def tarik_menu():
    global c, uang_user
    os.system('clear')
    print("====== MENU TARIK ======")
    tarik_saldo = int(input("Masukkan Saldo Yang Ditarik : "))
    uang_user -= tarik_saldo
    print("Tarik Berhasil !")
    kembali_menu()


# Nabung menu
def nabung_menu():
    global c, uang_user
    os.system('clear')
    print("====== MENU NABUNG ======")
    tambahan_nabung = int(input("Masukkan Uang Anda : "))
    uang_user += tambahan_nabung
    print("Nabung Berhasil !")
    kembali_menu()

# Transfer menu
def transfer_menu():
    global c, uang_user
    os.system('clear')
    print("====== MENU TRANSFER ======")
    rekening_tujuan = int(input("Masos.system('clear')ukkan rekening tujuan : "))
    transfer_nabung = int(input("Masukkan Jumlah Transfer : "))
    uang_user -= transfer_nabung
    print("Transfer Berhasil !")
    kembali_menu()


# Login menu
def login():
    global c, uang_user  # Menandakan bahwa 'c' dan 'uang_user' adalah variabel global
    max_coba = 3
    coba = 0
    username_benar = "adit"
    password_benar = "123"
    while coba < max_coba:
        username = input("Masukkan username : ")
        password = input("Masukkan password : ")

        if username == username_benar and password == password_benar:
            os.system('clear')
            print("Berhasil Login!\n")
            print("====== PROGRAM BANK ======")
            print(" 1. Cek saldo")
            print(" 2. Transfer")
            print(" 3. Nabung")
            print(" 4. Tarik")
            print(" 0. Exit")
            c = input("Enter Pilihan : ")

            # Cek saldo
            if c == '1':
                os.system('clear')
                cek_saldo()
                kembali_menu()

            # Transfer menu
            elif c == '2':
                os.system('clear')
                transfer_menu()

            # Nabung menu
            elif c == '3':
                os.system('clear')
                nabung_menu()

            # Tarik saldo
            elif c == '4':
                os.system('clear')
                tarik_menu()

            # Exit
            elif c == '0':
                print("Program dimatikan. Terima kasih telah menggunakan!")
                exit()


            break  # Keluar dari loop setelah login berhasil

        else:
            print("Login gagal. Silahkan coba lagi")
            coba += 1

    if coba == max_coba:
        print("Login gagal terus-menerus. Program dihentikan")
        exit()

# Main menu
print("====== PROGRAM BANK ======")
print(" 1. Login")
print(" 0. Exit")
c = input("Enter Pilihan : ")

if c == '1':
    os.system('clear')  # Membersihkan screen terminal
    login()
elif c == '0':
    print("Program dimatikan. Terima kasih telah menggunakan!")
    exit()