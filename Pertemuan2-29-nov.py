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

    # While loop 1
    size = int(input())
    i = 1
    while i <= size:
        j = size
        while j >= i:
            print('*' , end='')
            j -= 1
        print('')
        i += 1


if __name__ == '__main__':
    main()
