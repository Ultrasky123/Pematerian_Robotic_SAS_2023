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

    x = 12
    i = 1

    while i<=x:
        j = 1
        while j < i:
            print('*', end = '')
            j+=1
        print('')
        i+=1

if __name__ == '__main__':
    main()