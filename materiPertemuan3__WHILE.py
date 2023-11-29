def main():
    i = 1
    size = int(input("Size : "))
    while i < size:
        j = 0
        k = size
        while k > i:
            print("*", end='')
            k-=1

        while j < i :
            print(j, end = '')
            j=j+1

        print('')
        i+=1



#untuk memastikan bahwa nama dari progam ini adalah __main__
if __name__ == '__main__' :
    main()