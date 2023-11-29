def main():

    size = int(input("Masukkan input : "))
    i = 1

    while i <= size:
        j = size
        while j >= i:
            print("*", end='')
            j -= 1
        print('')
        i += 1

if __name__ == '__main__':
    main()