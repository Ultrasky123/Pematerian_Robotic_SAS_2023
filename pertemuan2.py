
def main():
    size = int(input())
    
    for i in range(0,size +1):
        for j in range(0,size - i + 1):
            print(' ', end='')
        for j in range(0, 2 * i):
            if j == 1 or j == 2 * i - 1:
                print('*', end='')
            else:
                print(' ', end='')
        
        print('')
    
    for i in range(size - 1, 0, -1):
        for j in range(0, size - i + 1):
            print (' ', end='')
        for j in range(0, 2 * i):
            if j == 1 or j == 2 * i - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
            



# untuk memastikan bahwa naem dari program ini adalah __main__
if __name__ == '__main__':
    main()