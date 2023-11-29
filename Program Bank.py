import os

# Informasi saldo
uang_user = 10000

# Fungsi Kembali Menu
def main_menu():
    os.system('clear')
    global c  # Menandakan bahwa 'c' adalah variabel global
    print("====== PROGRAM BANK ======")
    print("Saldo Anda : Rp. ", uang_user)
    print(" 1. Transfer")
    print(" 2. Nabung")
    print(" 3. Tarik")
    print(" 0. Exit")
    c = input("Enter Pilihan : ")

    # Transfer menu
    if c == '1':
        os.system('clear')
        transfer_menu()

    # Nabung menu
    elif c == '2':
        os.system('clear')
        nabung_menu()

    # Tarik saldo
    elif c == '3':
        os.system('clear')
        tarik_menu()

    # Exit
    elif c == '0':
        print("Program dimatikan. Terima kasih telah menggunakan!")
        exit()

# Narik menu
def tarik_menu():
    global c, uang_user
    os.system('clear')
    print("====== MENU TARIK ======")
    tarik_saldo = int(input("Masukkan Saldo Yang Ditarik : "))
    uang_user -= tarik_saldo
    print("Tarik Berhasil !")
    input("Tekan Enter untuk kembali ke Main Menu...")
    main_menu()


# Nabung menu
def nabung_menu():
    global c, uang_user
    os.system('clear')
    print("====== MENU NABUNG ======")
    tambahan_nabung = int(input("Masukkan Uang Anda : "))
    uang_user += tambahan_nabung
    print("Nabung Berhasil !")
    input("Tekan Enter untuk kembali ke Main Menu...")
    main_menu()

# Transfer menu
def transfer_menu():
    global c, uang_user
    os.system('clear')
    print("====== MENU TRANSFER ======")
    rekening_tujuan = int(input("Masukkan rekening tujuan : "))
    transfer_nabung = int(input("Masukkan Jumlah Transfer : "))
    uang_user -= transfer_nabung
    print("Transfer Berhasil !")
    input("Tekan Enter untuk kembali ke Main Menu...")
    main_menu()


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

            break  # Keluar dari loop setelah login berhasil

        else:
            print("Login gagal. Silahkan coba lagi")
            coba += 1

    if coba == max_coba:
        print("Login gagal terus-menerus. Program dihentikan")
        exit()

# Menu awal
print("====== PROGRAM BANK ======")
print(" 1. Login")
print(" 0. Exit")
c = input("Enter Pilihan : ")

if c == '1':
    os.system('clear')  # Membersihkan screen terminal
    login()
    main_menu()
elif c == '0':
    print("Program dimatikan. Terima kasih telah menggunakan!")
    exit()