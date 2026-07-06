#abstraction
from abc import ABC,abstractmethod

class BankAccount(ABC):
    def checkbalance(self):
        print("you can checkout your balance")

    def viewhistory(self):
        print("you can your transactions")
        
    def userinfo(self):
        print("you can see your details")

    def transaction(self):
        print("you can transfer money through netbanking")

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

class currentAccount(BankAccount):
    def deposit(self):
        print("you can deposit - CA")
    def withdraw(self):
        print("you can withdraw - CA")

class savingAccount(BankAccount):
    def deposit(self):
        print("you can deposit - SA")
    def withdraw(self):
        print("you can withdraw - SA")

class FixedDeposit(BankAccount):
    def deposit(self):
        print("you can deposit - FD")
    def withdraw(self):
        print("you can withdraw - FD")

class salaryAccount(BankAccount):
    def deposit(self):
        print("you can deposit - SAA")
    def withdraw(self):
        print("you can withdraw - SAA")

class ZeroBalanceAccount(BankAccount):
    def deposit(self):
        print("you can deposit - SAA")
    def withdraw(self):
        print("you can withdraw - SAA")

subbu=ZeroBalanceAccount()
subbu.deposit()
subbu.withdraw()
subbu.checkbalance()
subbu.viewhistory()
subbu.userinfo()
subbu.transaction()
print("================")
shiva=FixedDeposit()
shiva.deposit()
shiva.withdraw()
shiva.checkbalance()
shiva.viewhistory()
shiva.userinfo()
shiva.transaction()
