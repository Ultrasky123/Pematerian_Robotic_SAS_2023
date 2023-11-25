from dataBase import *

def login(uname, pasw) :
        

        try :

            x = username1.index(uname)
            y = pasword1.index(pasw)

        except :
            print("Username dan Password Tidak Ada")

            return False


        if uname == username1[x] and pasw == pasword1[y] :    
            print("Anda berhasil login")
            return True
        # else : 
        #     if uname is not username1[x] : 
        #         print("Username yang anda masukkan salah!!!!!!!")
        #     elif pasw is not pasword1[x] :
        #         print("Password salah!!!!!!")
        #     else :
        #         print("Password dan Username salah!!!!!")

        #     return False