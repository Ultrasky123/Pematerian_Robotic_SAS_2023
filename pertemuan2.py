def main():
    size = int(input())
    i = 0

    
    #untuk setiap i sebanyak size
    #selama kondisi i < size adalah TRUE
    while i <= size :
        j = size
        while j >= i:
            print('*',end='')
            j -= 1
        #break line 
        print ('')
        i += 1


# untuk memastikan bahwa naem dari program ini adalah __main__
if __name__ == '__main__':
    main()