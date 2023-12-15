#1..


def main():
    size = int(input())
    for i in range (0, size +1):
        for j in range(0, i):
            print('*' , end="")
            print('')

if __name__ == '__main__':
    main()

#2..

def main():
    size = int(input())
    i = 1
# untuk setiap i sebanyak size
#selama kondisi i < size adalah TRUE 

    while i <= size:
        j = size
        while j >= i:
            print('*', end='')
            j -= 1
        print('')
        i += 1

#untuk memastikan bahwa name dari program ini adalah__main__
if __name__ == '__main__':
    main()

#3.. program 
#    *
#   *  *
#  *    *
# *      *
#  *    *
#   *  *
#    *

rows = 5
i = 1
while i <= rows:
    j = rows 
    while j > i:
        #spacenya
        print('', end='')
        j -= 1
    print('*', end='')
    k = 1
    while k < 2
