username = "Rinwldr"
pin = 4321
max_attempts = 3
attempts = 0

print("SELAMAT DATANG DI BANK ABC")

while attempts < max_attempts:
    input_username = input("Masukkan Username: ")
    input_pin = int(input("Masukkan PIN Anda: "))

    if input_pin == pin & username:
        print("Selamat datang!")
        break
    else:
        print("\nPIN salah. Coba lagi.")
        attempts += 1

    if attempts == max_attempts:
        print("\nAnda telah melebihi batas percobaan PIN. Program selesai.")
        break
    
while attempts < max_attempts:
    print("\n=== ATM Menu ===")
    print("1. Setor Tunai")
    print("2. Transfer")
    print("3. Tarik Tunai")
    print("4. Cek Saldo")
  
    pilihan = int(input("Masukkan Pilihan Anda: "))

    saldo = 100000  # bisa diganti saldo awal sesuai yang diinginkan

    if pilihan == 1:
        setor = int(input("Masukkan Uang Anda Rp "))
        saldo += setor
        print("Total Saldo Anda Rp ", saldo)
    elif pilihan == 2:
        namatujuan = input("Masukkan nama rekening tujuan: ")
        rekening = int(input("Masukkan no rekening tujuan: "))
        jumlahtransfer = int(input("Masukkan Jumlah Uang: "))
        if saldo >= jumlahtransfer:
            print("Konfirmasi Transfer:")
            print(f"Transfer ke rekening {namatujuan} dengan no rekening {rekening} senilai {jumlahtransfer}")
            konfirmasi = input("Apakah Anda yakin? (y/n): ")
            if konfirmasi.lower() == 'y':
                saldo -= jumlahtransfer
                print(f"Transfer berhasil ke rekening {namatujuan} dengan no rekening {rekening} senilai {jumlahtransfer}")
            else:
                print("Transfer dibatalkan.")
        else:
            print("Transaksi Gagal, Saldo Anda Tidak Cukup")
    elif pilihan == 3:
        jmlhtarik = int(input("Masukkan nominal yang akan di tarik: "))
        if saldo >= jmlhtarik:
            saldo -= jmlhtarik
            print("Tarik Tunai Berhasil Senilai", jmlhtarik)
            print("Sisa Saldo Anda", saldo)
        else:
            print("Transaksi Gagal, Saldo Anda Tidak Cukup")
    elif pilihan == 4:
        print("Saldo Anda Rp ", saldo)
 
    else:
        print("Pilihan Invalid. Silakan coba lagi.")

    transaksi_lagi = input("Apakah Anda ingin melakukan transaksi lagi? (y/n): ")
    if transaksi_lagi.lower() == 'n':
        print ("Terimakasih , Program Selesai")
        break

# Set ulang attempts menjadi 0 setelah setiap transaksi
    attempts = 0