# def main():
#     size = int(input())
#     i= 1

#     #untuk setiap i sebanyak size
#     #selama kondisi i < size adalah TRUE
#     while i <=  size:
#         j = size
#         while j >= i:
#             print('*',end='')
#             j -=1
#         print('')
#         i += 1
    
# #untuk memastikan bahwa name dari program ini adalah _main_
# if __name__== '__main__':
#     main()

# def main():
#     size = int(input())

#     for i in range (0,size):
#         for j in range ()

row = int(input('Enter number of row: '))

for i in range(1, row+1):
    for j in range(1,row-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower part of hollow diamond
for i in range(row-1,0, -1):
    for j in range(1,row-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()