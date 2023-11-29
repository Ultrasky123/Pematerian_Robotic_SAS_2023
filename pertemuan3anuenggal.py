'''def main():

    size = int(input("* = " ))

    for i in range(0, size):
        for j in range(0, i):
            print ('*', end='')
        print()

if __name__== '__main__':
    main()'''

''''''''''''''''''''''''''''''''

'''def main():

    size = int(input(" = "))

    i = 1
    while i <= size+1:
        j = size
        while j > i:
            print('*', end='')
            j -= 1
        print('')
        i += 1

if __name__== '__main__':
    main()'''

def main():

    row = int(input())

    for i in range(1, row+1):
        for j in range(1,row-i+1):
            print(" ", end="")
        for j in range(1, 2*i):
            if j==1 or j==2*i-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    for i in range(row-1,0, -1):
        for j in range(1,row-i+1):
            print(" ", end="")
        for j in range(1, 2*i):
            if j==1 or j==2*i-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
if __name__== '__main__':
    main()