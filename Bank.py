class Bank:
    def __init__(self,name,address) -> None:
        self.name=name
        self.address=address
        self.available_balance=0
        self.given_loan=0
        self.loan_feature=True

class Person:
    def __init__(self,name,email) -> None:
        self.name=name
        self.email=email

class User(Person):
    def __init__(self,bank,name, email) -> None:
        self.bank=bank
        super().__init__(name, email)
        self.available_balance=0
        self.transactions=[]
        self.loan_taken=0
    
    acc_counter=1000

    def create_account(self,password):
        self.__password=password
        self.acc_no=User.generate_acc_no()
    
    @classmethod
    def generate_acc_no(self):
        acc_no=self.acc_counter
        self.acc_counter+=100
        return acc_no
    
    def deposit(self,amount):
        self.available_balance+=amount
        self.bank.available_balance+=amount
        self.transactions.append(f'Deposited amount :{amount}')

    def withdrawal(self,amount):
        if self.available_balance>=amount and self.bank.available_balance>=amount:
            self.available_balance-=amount
            self.bank.available_balance-=amount

            self.transactions.append(f'Withdrawal amount :{amount}')

        else:
            if self.available_balance<amount:
                print(f'Withdrawal amount can not exceed the available balance')
            elif self.bank.available_balance<amount:
                print('The bank is bankrupt')


    @property
    def check_balance(self):
        return self.available_balance
    
    def transfer_balance(self,user,amount):
        if amount<=self.available_balance:
            user.available_balance+=amount
            self.available_balance-=amount
            self.transactions.append(f'Transfered :{amount} to user name:{user.name}')
        else:
            print(f'Transfered amount can not exceed the available balance')

    def take_loan(self,amount):
        if self.bank.loan_feature==True and amount<= 2*(self.available_balance):
            self.loan_taken+=amount
            self.bank.available_balance-=amount
            self.bank.given_loan+=amount
        else:
            if amount>2*(self.available_balance):
                print('Amount exceed the limit')
            elif self.bank.loan_feature==False:
                print('Sorry! The loan feature is currently unavailable')

    
    def show_transactions(self):
        for transaction in self.transactions:
            print(transaction)


    def __repr__(self) -> str:
        return f'Name:{self.name} with acc_no :{self.acc_no} currently has {self.available_balance} as balance'
    
class Admin(Bank):
    def __init__(self,bank) -> None:
        self.bank_admin=bank
    
    def create_acc(self,admin_name,email):
        self.admin_name=admin_name
        self.email=email

    def check_balance(self):
        print(self.bank_admin.available_balance)

    def check_loan_amount(self):
        print(self.bank_admin.given_loan)

    def off_loan(self):
        self.bank_admin.loan_feature=False


    def __repr__(self) -> str:
        return f'Admin name:{self.admin_name}'
    


bank=Bank('Brac','zindabazar')

user1=User(bank,'affan','affan@user1')
user1.create_account(12345)
user2=User(bank,'aroshi','aroshi@user2')
user2.create_account(12345)
user3=User(bank,'mushfiq','mushfiq@user3')
user3.create_account(12345)


print(user1)
print(user2)
print(user3)

print(user1.check_balance)

user1.deposit(1000)
user1.withdrawal(400)

print(user1.check_balance)

user1.transfer_balance(user2,200)
user1.show_transactions()
print(user1.check_balance)
print(user2.check_balance)

print(bank.available_balance)

user1.take_loan(700)

print(bank.available_balance)
print(bank.given_loan)
user2.withdrawal(150)



admin1=Admin(bank)
admin1.create_acc('mr. afridi','afridi@admin1')
admin2=Admin(bank)
admin2.create_acc('ms.afsana','afridi@admin2')
print(admin1)
print(admin2)
admin1.check_balance()
admin1.check_loan_amount()
admin1.off_loan()
user1.take_loan(2)


        