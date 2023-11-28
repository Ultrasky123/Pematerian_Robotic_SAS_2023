import module_for_calculator

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
    print(module_for_calculator.add(n1, n2))
elif ch == '2':
    print(module_for_calculator.sub(n1, n2))
elif ch == '3':
    print(module_for_calculator.mul(n1, n2))
elif ch == '4':
    if n2 == 0:
        print('Cannot divide by zero')
    else:
        print(module_for_calculator.div(n1, n2))
else:
    print("Invalid option")