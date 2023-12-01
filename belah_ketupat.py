import os

def belah_ketupat():

    while True:
        size = int(input("Masukkan ukuran : "))

        if size % 2 != 0:
            for i in range(1, (size // 2 + 1) +1):
                for j in range(1,size-i+1):
                    print(" ", end="")
                for j in range(1, 2*i):
                    if j==1 or j==2*i-1:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print()

            for i in range((size // 2 + 1)-1,0, -1):
                for j in range(1,size-i+1):
                    print(" ", end="")
                for j in range(1, 2*i):
                    if j==1 or j==2*i-1:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print()
            break
        else:
            print("Masukkan angka ganjil!")
            print()

    
        
if __name__ == '__main__':
    belah_ketupat()
    while True:     
        confirm = input("Apakah Anda ingin mencoba lagi? (y/n) : ")
        print()
        if confirm == "y":
            os.system("clear")
            belah_ketupat()
        elif confirm == "n":
            break