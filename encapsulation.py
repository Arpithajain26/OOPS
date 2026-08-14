class ATM:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__amount=amount
        print(f"deposited {amount}.new balance{self.__balance}")
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"withdraw amount {amount} now new balance is :{self.__balance}")
        else:
            print("insufficient balance")
atm=ATM(1000)
atm.deposit(100)
atm.withdraw(500)