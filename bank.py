# loop, masukin username password salah 3 kali, pilihan tarik tunai, transfer, nabung, 

username = "Musthofa Anwari"
password = 12345

isLanjut = True
i = 0
while isLanjut == True:
    userName = input("Masukkan Username: ")
    Password = input("Masukkan Password: ")
    if username != userName and password != Password:
        print("Username atau Password salah")
        i+=1
        print("Percobaan ke", i, "dari 3")
        if i == 3:
            break
    else:
        print("Masuk ke menu")
        break


