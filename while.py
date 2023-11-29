def main():
    size = int(input("Masukkan ukuran: "))
    # for loop
    # untuk setiap i dari 0 s.d 5
    
    i = 0
    # Untuk setiap i sebanyak size
    # Selama kondisi while i < size+1 TRUE
    while i <= size:
        j = size
        while j < i:
            print(" ", end="")
            j += 1
        j = 0
        while j < i:
            print("* ", end="")
            j += 1
        print("")
        i+=1
    

    '''
    for i in range(0, size+11) :
        for j in range (0, i):
            # Tampilkan * sebanyak j
            print("*", end="")
        print("")
    '''

# Untuk memastikan bahwa name dari program ini adalah __main__
if __name__ == '__main__':
    main()