def main():
    size= int(input())

    #For loop 
    #untuk setiap i dari 0 s.d. size
    for i in range(0,size+1):
        #untuk setiap j dari 0 s.d 1
        print(i)
        for i in range(0,1):
            print ('*', end='')

#untuk memastikan bahwa name dari program ini adalah _main_
if __name__== '__main__':
    main()