def main():
    size = int(input())

   # For Loop
    for i in range(0, size):
        for j in range(0, i):
            print('*', end='')
        print('')
       
if __name__ == '__main__':
    main()
