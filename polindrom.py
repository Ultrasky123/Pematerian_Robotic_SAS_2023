def kataKebalik(kata):
    return kata[::-1]

def main():
    kata = str(input("Masukkan kata: "))
    if kata == kataKebalik(kata=kata):
        print("True") 
    else:
        print("False") 
if __name__ == '__main__':
    main()