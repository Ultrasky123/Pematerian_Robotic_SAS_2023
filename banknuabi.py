# Panggil library 'os'
import os

# Keputusan Pengulangan
def login():
    os.system('clear')
    print("Transaksi berhasil!")
    login_choice = input("Apakah anda ingin melanjutkan program (y/n)? ")
    if login_choice.lower() != 'y' or 'Y':
        print("Program Selesai")
        return False

# Username dan Password
print("Bank Sederhana\n")
username = "admin"
password = "admin"
attempt_count = 0
max_attempts = 3

# Menu login
while True:
    print("Masukan Username dan Password")
    input_username = input("Username: ")
    input_password = (input("Password: "))

    # Pengulangan Username dan Password
    if username != input_username or password != input_password:
        os.system('clear')
        print("Username atau Password salah!")
        attempt_count += 1
        print("Sisa Percobaan ", attempt_count, "/", max_attempts)
        if attempt_count == max_attempts:
            print("Anda telah melebihi percobaan, silahkan coba lagi beberapa saat..")
            break
    else:

        # Total Saldo Pada Bank
        total_saldo = 100000

        # Perulangan Menu Transaksi Bank
        while True:
            os.system('clear')
            print("Total saldo pada akun:")
            print("Rp.", total_saldo, "\n")
            print("Pilih transaksi yang di inginkan")
            print("1. Transfer")
            print("2. Tarik Tunai")
            print("3. Setor tunai")
            print("0. Keluar")
            choice = int(input("Masukkan pilihan transaksi: "))

            # Transfer logic goes here
            if choice == 1:
                transfer = int(input("Masukan nominal: Rp "))
                total_saldo -= transfer
                login()

            # Tarik Tunai logic goes here
            elif choice == 2:
                    tariktunai = int(input("Masukan nominal: Rp "))
                    total_saldo -= tariktunai
                    login()

            # Setor Tunai logic goes here
            elif choice == 3:
                setortunai = int(input("Masukkan nominal: Rp "))
                total_saldo += setortunai
                print("Total saldo anda sekarang Rp ", total_saldo)
                login()

            # Exit
            elif choice == 0:
                exit()
            
            else:
                print("Pilihan transaksi tidak ada!")
                breaker = True
                break