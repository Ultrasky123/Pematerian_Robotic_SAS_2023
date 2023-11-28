def add(a, b):
    return(a+b)

def sub(a, b):
    return(a-b)

def mul(a, b):
    return(a*b)

def div(a, b):
    return(a/b)

n1 = input("Enter a number:")
n1 = int(n1)
n2 = input("Enter another number:")
n2 = int(n2)

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

ch = input("Enter your choice:")

if ch == '1':
    print(add(n1, n2))
elif ch == '2':
    print(sub(n1, n2))
elif ch == '3':
    print(mul(n1, n2))
elif ch == '4':
    if n2 == 0:
        print('Cannot divide by zero')
    else:
        print(div(n1, n2))
else:
    print("Invalid option")