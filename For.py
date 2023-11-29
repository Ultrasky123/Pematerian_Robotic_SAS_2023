def main():
    size = int(input())

   # For Loop
    for i in range(0, size + 1):
        for j in range(0, i + 1):
            print('*', end='')
        print('')
       
if __name__ == '__main__':
    main()
