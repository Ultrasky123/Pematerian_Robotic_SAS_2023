def main():
    #x = 9
    #for i in range(0, x):
    #    print(i)

    #for i in 'jkjkjk':
    #    print(i)

    #x = 10
    #for i in range(0, x):
    #    for i in range(0, i):
    #        print('*', end=' ')
    #    print('')

    #x = 12
    #i = 1

    #while i<=x:
    #    j = 1
    #    while j < i:
    #        print('*', end = '')
    #        j+=1
    #    print('')
    #    i+=1
    

    #   *   > 0
    #  * *  > 1
    # *   * > 3
    #top part

    #*     * middle part > 5

    #bottom part
    # *   * > 3
    #  * *  > 1
    #   *   > 0
    
    size = int(input("Enter the size: "))

    for i in range(1, size + 1):
        print(' ' * (size - i) + "*" + ' ' * (2 * i - 3) + ("*" if i > 1 else ""))

    for i in range(size - 1, 0, -1):
        print(' ' * (size - i) + "*" + ' ' * (2 * i - 3) + ("*" if i > 1 else ""))

if __name__ == '__main__':
    main()