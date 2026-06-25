'''
class Filpkart():
    dis = 0
    pro = ["Laptop", "phone", 'mouse', 'charger']

    @classmethod
    def showpro(cls):
        print(cls.pro)

    def login(self, user, password):
        self.user= user
        self.password=password
        print(f'Welcome to the filpkart {self.user}')
    
    @staticmethod
    def banner():
        print('10% zdiscount is avilable')
    


dinesh = Filpkart()
dinesh.login("Dinesh", "aj@y")

dinesh.banner()
dinesh.showpro()

Filpkart.banner()
Filpkart.showpro()
'''

class Insta:
    def __init__(self,user,password):
        self.user = user
        self.__password = password
        self.followers = []
        print(f"Welcome to instagram, {self.user}")

    def getpass(self):
        return self.__password
    
    def setpass(self, newpassword):
        self.__password = newpassword

ajay =Insta("Ajay", "Aj@y")
print(f'Before Username: {ajay.user}')
ajay.user = 'Dinesh Ajay'
print(f'After Username: {ajay.user}')

print(f'Before Password: {ajay.getpass()}')
ajay.setpass("@j@y")
print(f'After Password: {ajay.getpass()}')