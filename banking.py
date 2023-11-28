import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

user = 'user1'
pas = 'pass1'
bal = 0

clear_screen()

def login(a, b):
    for i in range(3):
        u = input("Enter username: ")
        p = input("Enter password: ")
        if u == a and p == b:
            print("Login Successful")
            mainmenu()
            break
        else:
            if i < 2:
                print("Username or password is incorrect. Please try again.")
            else:
                print("Failed to login, maximum login attempts reached.")

def mainmenu():

    while True:

        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Check your balance")
        print("5. Exit")

        op = input("Enter an option:")

        if op == '1':
            print("Deposit")
            deposit()
        elif op == '2':
            print("Withdraw")
            withdraw()
        elif op == '3':
            print("Transfer")
        elif op == '4':
            print("Balance")
            balance()
        elif op == '5':
            print("Exiting PY Bank...")
            exit()
        else:
            print("Please choose a valid option")

def deposit():
    global bal
    print('Your current balance:', bal)
    print("1. Deposit")
    print("2. Exit to menu")
    op = input("Enter an option: ")

    if op == '1':
        dep = int(input("Enter how much to deposit: "))
        bal += dep
        print(f"Deposit successful. Your updated balance is {bal}")
        deposit()
    elif op == '2':
        mainmenu()
    else:
        print("Please choose a valid option")

def withdraw():
    global bal
    print('Your current balance:', bal)
    print("1. Withdraw")
    print("2. Exit to menu")
    op = input("Enter an option: ")

    if op == '1':
        wit = int(input("Enter how much to withdraw: "))
        if wit>bal:
            print("Failed to withdraw, not enough balance")
            withdraw()
        else:
            bal -= wit
            print(f"Withdrawn successful. Your updated balance is {bal}")
            withdraw()
    elif op == '2':
        mainmenu()
    else:
        print("Please choose a valid option")

def transfer():
    global bal
    print('Your current balance:', bal)
    print("1. Transfer")
    print("2. Exit to menu")
    op = input("Enter an option: ")

    if op == '1':
        input("Enter the user account you'd like to transfer to: ")
        wit = int(input("Enter how much to transfer: "))
        if wit>bal:
            print("Failed to transfer, not enough balance")
            transfer()
        else:
            bal -= wit
            print(f"Transfer successful. Your updated balance is {bal}")
            transfer()
    elif op == '2':
        mainmenu()
    else:
        print("Please choose a valid option")

def balance():
    global bal
    print("Your current balance: ", bal)
    print("Press any button to go back to the main menu")
    input()
    mainmenu()

while True:

    print("Welcome to PY Bank")
    print("1. Login")
    print("2. Exit")

    op = input("Enter an option: ")

    if op == '1':
        login(user, pas)
    elif op == '2':
        print("Exiting PY Bank...")
        exit()
    else:
        print("Please choose a valid option")