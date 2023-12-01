class BankAccount:

    no_of_cust = 0
    acc_num = 12345

    def init (self, name, mobile_no, initial_depo, pin):

        self.name               = name
        self.cust_acc_num       = BankAccount.acc_num
        self.mobile_no          = mobile_no
        self.acc_balance        = initial_depo
        self.pin                = pin
    
        BankAccount.acc_num     = BankAccount.acc_num + 1
        BankAccount.no_of_cust  = BankAccount.no_of_cust + 1

def basic_details(self):
    print(f'User: {self.name}\t Nomer Akun: {self.cust_acc_num}\t Saldo: Rp.{self.acc_balance}')

def deposit(self):
    amount = int(input('Masukan Jumlah Deposito: '))
    if amount > 0:
        self.acc_balance       = self.acc_balance + amount
        print(f'Transaksi Berhasil. Total saldo saat ini: Rp.{self.acc_balance}')
    else:
        print('Jumlah Transaksi Invalid. Transaksi Diberhentikan..')
    
def withdrawl(self):
        amount = int(input('Masukkan Jumlah Penarikan: '))
        if amount <= self.acc_balance and amount > 0:
            self.acc_balance      = self.acc_balance - amount
            print(f'Transaksi Berhasil. Total saldo saat ini: Rp.{self.acc_balance}')
        else:
            print('Jumlah Transaksi Invalid. Transaksi Diberhentikan..')

def payment(self, other):
        amount = int(input('Masukan Metode Pembayaran: '))
        if amount <= self.acc_balance and amount > 0:
            self.acc_balance      = self.acc_balance - amount
            other.acc_balance     = other.acc_balance + amount
            print(f'Transaksi Berhasil. Total saldo saat ini: Rp.{self.acc_balance}')
        else:
            print('Jumlah Transaksi Invalid. Transaksi Diberhentikan..')