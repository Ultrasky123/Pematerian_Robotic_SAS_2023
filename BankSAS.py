import os

username = "tisya"
password = "oke12"
pin = 123
saldo = 100000

def login():
    i = 0
    while i < 3:
        i  += 1
        usn = input("Masukkan username: ")
        psw = input("Masukkan password: ")
        if usn == username and psw == password:
            i = 3
            print("Login berhasil! ")
            return True
        elif i == 3:
            print("Login gagal!")
            return False
            break
        else:
            print(f"username / password salah, percobaan ke-{i}")


    
def cek_saldo():
    print(f"Saldo anda sekarang adalah {saldo}")


def tarik_tunai():
    t = 0
    tarik = int(input("Jumlah saldo yang ingin ditarik: "))
    while t < 3:
        t += 1
        pin1 = int(input("Masukkan pin: "))
        if pin1 == pin:
            t = 3
            global saldo
            if saldo < tarik:
                print("Saldo anda kurang")
                print(f"Sisa saldo anda saat ini {saldo}")
            else:
                saldo -= tarik
                print(f"Berhasil, Saldo anda tersisa {saldo}")
        elif t == 3:
            print("Percobaan habis, kembali ke menu awal")
            break
        else:
            print(f"Pin anda salah!, percobaan ke-{t}")
            


def transfer():
    x = 0
    listbank = input("Masukkan bank tujuan: ")
    rekening = input("Masukkan rekening: ")
    while x < 3:
        x += 1
        pin1 = int(input("Masukkan pin: "))
        if pin1 == pin:
            x = 3
            global saldo
            nominal = int(input("Masukkan nominal transfer: "))
            if saldo < nominal:
                print("Saldo anda kurang")
                print(f"Sisa saldo anda saat ini {saldo}")
            else:
                saldo -= nominal
                print(f"Berhasil, Saldo anda tersisa {saldo}")
        elif x == 3:
            print("Percobaan habis, kembali ke menu awal")
            break
        else:
            print(f"Pin anda salah!, percobaan ke-{x}")
            

def setor_tunai():
    y = 0
    nominal = int(input("Masukkan nominal yang ingin di setor: "))
    while y < 3:
        y += 1
        pin1 = int(input("Masukkan pin: "))
        if pin1 == pin:
            y = 3
            global saldo
            saldo += nominal
            print(f"Berhasil, saldo anda sekarang adalah {saldo}")
        elif y == 3:
            print("Percobaan habis, kembali ke menu awal")
            break
        else:
            print(f"Pin anda salah!, percobaan ke-{y}")

    
if login() == True:
    while True:
        print("==== Welcome to SAS BANK ====")
        print("1. Cek Saldo ")
        print("2. Tarik Tunai")
        print("3. Transfer ")
        print("4. Setor Tunai ")
        print("5. Exit")
        pilih = int(input("Pilih Menu: "))

        if pilih == 1:
            cek_saldo()
        elif pilih == 2:
            tarik_tunai()
        elif pilih == 3:
            transfer()
        elif pilih == 4:
            setor_tunai()
        elif pilih == 5:
            os.system('cls')
            print("Terima kasih!")
            break
        else:
            print("Inputan tidak tersedia, pilih sesuai menu!")
else:
    print("Selamat tinggal!")
