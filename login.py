from dataBase import *

def login(uname, pasw) :
        
##### MENGGUNAKAN METODE SEQUENTIAL SEARCH

        d = len(pasword1)
        i = 0
        ketemu = False
        

        while (i < len(pasword1)) and (uname is not username1) and (pasw is not pasword1) :
             
             if (uname == username1[i]) and (pasw == pasword1[i]) :
                  ketemu = True
             
             i = i + 1

        if ketemu == True :
             return True
        else :
             return False


        # try :

        #     x = username1.index(uname)
        #     y = pasword1.index(pasw)

        #     if uname == username1[x] and pasw == pasword1[y] :    
        #         print("Anda berhasil login")
        #         return True

        # except :
        #     print("Username dan Password Tidak Ada")

        #     return False


        



        # else : 
        #     if uname is not username1[x] : 
        #         print("Username yang anda masukkan salah!!!!!!!")
        #     elif pasw is not pasword1[x] :
        #         print("Password salah!!!!!!")
        #     else :
        #         print("Password dan Username salah!!!!!")

        #     return False

def loginPin(pin) : 

        # try :

        #     x = pin.index(pin)
            

        # except :
        #     print("Pin salah!!!!!!!!")

        #     return False


        # if pin == pinDataBase[x]:
        #     return True
    
        n = len(pinDataBase)
        i = 0
        ketemu = False

        while(i <= n-i) and (pin is not pinDataBase[i]) :
        
            if pin == pinDataBase[i] :
                ketemu = True
            i= i+1

        if ketemu == True :
          return True
        else :
          return False
        
def CariNoRek(i, noRekening) :
    n = len(noRekDataBase)
    i = 0 
    ketemu = False
    while (i<n) and (noRekening is not noRekDataBase[i]) :
        
        if noRekening == noRekDataBase[i] :
            ketemu = True
            print("Index Pencarian No Rek", i)
        i = i + 1
    
    if ketemu == True :
        print("Cek Index Penerima di Modul Login " , i)
        return True
    else :
        return False
    


