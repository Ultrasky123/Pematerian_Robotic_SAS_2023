import os

def login():
    login_choice = input("Apakah anda ingin melanjutkan program (y/n)? ")
    if login_choice.lower() == 'n' or 'N':
        print("Program Selesai")
        return False
    return True

print("Bank Sederhana\n")
username = "admin"
password = "admin"
attempt_count = 0
max_attempts = 3

while True:
    print("Masukan Username dan Password")
    input_username = input("Username: ")
    input_password = (input("Password: "))

    if username != input_username or password != input_password:
        print("Username atau Password salah!")
        attempt_count += 1
        os.system('clear')
        print("Sisa Percobaan ", attempt_count, "/", max_attempts)
        if attempt_count == max_attempts:
            print("Anda telah melebihi percobaan, silahkan coba lagi beberapa saat..")
            break
    else:

        total_saldo = 100000

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

            if choice == 1:
                # Transfer logic goes here
                transfer = int(input("Masukan nominal: Rp "))
                total_saldo -= transfer
                if not login():
                    break

            elif choice == 2:
                # Tarik Tunai logic goes here
                if not login():
                    tariktunai = int(input("Masukan nominal: Rp "))
                    total_saldo -= tariktunai
                    break

            elif choice == 3:
                # Setor Tunai logic goes here
                setortunai = int(input("Masukkan nominal: Rp "))
                total_saldo += setortunai
                print("Total saldo anda sekarang Rp ", total_saldo)
                if not login():
                    break