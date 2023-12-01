def cek_palindrom(kata):
    kata = kata.lower()

    if kata == kata[::-1]:
        return True
    else:
        return False

input_user = input("Masukkan sebuah kata: ")

if cek_palindrom(input_user):
    print("True")
else:
    print("False")
