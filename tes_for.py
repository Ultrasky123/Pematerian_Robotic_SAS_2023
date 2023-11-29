def main():

    # 1. Contoh Dasar
    x = int(input("Masukkan input : "))

    for i in range(0,x):
        print(i)
    
    print()

    # 2. Array
    arr = [0, 1, 2, 3]
    
    for i in arr:
        print(i)
    
    print()

    # 3. Pola Bintang
    size = int(input("Masukkan input : "))

    for i in range(size):
        for j in range(i+1):
            print("*", end='')
        print()

    print()

# Untuk memastikan bahwa name dari program ini adalah __main__
if __name__ == '__main__':
    main()