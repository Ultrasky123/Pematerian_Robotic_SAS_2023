def main():
    # For loop 1
    #for i in range(0,5, 2):
    #    print(i)

    # For loop 2
    #x = int(input())
    #for i in x:
    #    print(i)

    # For loop 3
    #for i in 'ROBOTIC':
    #    print(i)

    # For loop 4
    #size = int(input())
    #for i in range(0,size):
    #    for j in range(0,i):
    #        print("*", end=' ')
    #    print('')

    # For loop 4
    #size = int(input())
    #for i in range(size):
    #    for j in range(size):
    #        print('*' , end=' ')
    #    print()

    # For loop 5
    row = int(input())
    # Bagian atas hollow diamond
    for i in range(1, row+1):
        for j in range(1,row-i+1):
            print(" ", end="")
        for j in range(1, 2*i):
            if j==1 or j==2*i-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    # Bagian bawah hollow diamond
    for i in range(row-1,0, -1):
        for j in range(1,row-i+1):
            print(" ", end="")
        for j in range(1, 2*i):
            if j==1 or j==2*i-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # While loop 1
    #size = int(input())
    #i = 1
    #while i <= size:
    #    j = size
    #    while j >= i:
    #        print('*' , end='')
    #        j -= 1
    #    print('')
    #    i += 1


if __name__ == '__main__':
    main()
