kata = input("Masukkan Kata: ")
palindrome = kata[:: -1]

if kata == palindrome:
    print("True")
else:
    print("False")