# for

# def main ():
#     size = int(input())

#     for i in range(0,size+1) :
#         for j in range(0, i):
#             print('*', end='')
#         print('')

# if __name__ == '__main__':
#     main()

# while

def main ():
    size = int(input())
    i = 1
    while i <= size:
        j= size
        while j >= i:
            print('*', end='')
            j-=1
        print('')
        i+= 1

if __name__ == '__main__':
    main()
