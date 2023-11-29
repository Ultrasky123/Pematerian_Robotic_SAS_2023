def main():
    size = int(input())
    i = 0
    j = 0

    while i <= size:
        j = size
        while j >= i:
            print('*', end='')
            j -= 1
        print('')
        i += 1

if __name__ == '__main__':
    main()