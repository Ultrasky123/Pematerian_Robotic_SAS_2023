import os

# def palindrom_simple():
#     text = str(input("Masukkan text : "))
#     print(text == text[::-1])

def palindrom_for():

    text = str(input("Masukkan text : "))

    reverse_text = ""

    for i in range(len(text)-1, -1, -1):
        reverse_text += text[i]

    if text == reverse_text:
        print("True")
    else:
        print("False")

if __name__ == '__main__':
    palindrom_for()

    while True:
        confirm = input("Apakah Anda ingin memasukkan kata lagi? (y/n) : ")
        print()
        if confirm == "y":
            os.system("clear")
            palindrom_for()
        elif confirm == "n":
            break