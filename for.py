def main():
    ARR = [0,1,2,3,4,5,6,7]
    size = int(input("Masukkan ukuran: "))
    # for loop
    # untuk setiap i dari 0 s.d 5

    for i in range(0, size+11) :
        for j in range (0, i):
            # Tampilkan * sebanyak j
            print("*", end="")
        print("")

# Untuk memastikan bahwa name dari program ini adalah __main__
if __name__ == '__main__':
    main()