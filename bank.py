import datetime

x = datetime.datetime.now()
print(x.strftime("%x"))  #print tanggal
print(x.strftime("%X"))  #print waktu
print(x) #lengkap

data_account:[{
    "name":"kalila",
    "date":"1/10/2022",
    "balance":5000,
    "transaction":[{
        "date":"1/1/2022",
        "type":"D",
        "desc":"transfer",
        "amount":500},
        {"date":"1/2/2022",
        "type":"D",
        "desc":"withdraw",
        "amount":1500}
        ]
      }]

def transfer_withdraw():
    #cek dulu apakah sdh login?
    amount_tt_wd = int(input('Amount transfer or withdaw ?'))
    #cek apakah duitnya ada?
    #masukkan transaksi ke key ->transaction
    #jgn lupa update balance dan tanggal terkhir balance diupdate

def saving():
    #cek apaakh sdh login
    amount_saving = int(input('Amount saving ?'))
    #update tanggal
    #update data transaksi
    #update balance

# user dan PIN
user_PIN = [("kalila",234),("airin",345)]

# Login 
error_login_counter = 0
is_succes= True

while error_login_counter <3 and not is_succes:
    input_PIN = int(input('Enter PIN : '))
    for user in user_PIN:
        if input_PIN == user[1]:
            print('Login success')
            print('Hai '+user[0])
            is_succes = True
            #dari sini bikin route ke transfer / withdraw / saving
            break
    error_login_counter +=1
    
 
if not is_succes:
    exit('Login failed')
    
#Logout
def log_out():
    is_succes = False