'''
#Polymorphism
class Hotstar:
    def __init__(self,name):
        self.name=name
        print(f'Hi {self.name}, Welcome to the hotstar')
    def login(self):
        print("you can login")
    def dashboard(self):
        print("you can see the dashboard items")
    def search(self):
        print("you can search")
    def lang(self):
        print("you can select the languages")
    def playcontrollers(self):
        print("you can pause and play the video")
    def ads(self):
        print("ads will run")
    def movies(self):
        print("you have limited access for movies")
    def sports(self):
        print("you can have limited time to watch sports")
    def quality(self):
        print("limited quality to watch videos")



class PremiumHotstar(Hotstar):
    def __init__(self,name):
        self.name=name
        print(f'Hi {self.name}, Welcome to the Premium hotstar')
    def ads(self):
        print("ads won't run")
    def movies(self):
        print("you can have access to unlimited movies")
    def sports(self):
        print("you can have unlimited time to watch sports")
    def quality(self):
        print("High quality to watch videos")


print(f"\n========hi========\n")
naresh=Hotstar('naresh')
naresh.login()
naresh.dashboard()
naresh.search()
naresh.lang()
naresh.playcontrollers()
naresh.ads()
naresh.movies()
naresh.sports()
naresh.quality()
print(f"\n========Thank you========\n")

print(f"\n========Hi========\n")
Ajay=PremiumHotstar('Ajay')
Ajay.login()
Ajay.dashboard()
Ajay.search()
Ajay.lang()
Ajay.playcontrollers()
Ajay.ads()
Ajay.movies()
Ajay.sports()
Ajay.quality()
print(f"\n========Thank you========\n")
'''

# Operator Overloading
class Number:
    def __init__(self,n):
        self.n=n
    def __add__(self, other):
        return self.n+other.n
    def __sub__(self, other):
        return self.n - other.n
    def __mul__(self, other):
        return self.n * other.n
    def __truediv__(self, other):
        return self.n / other.n
    def __eq__(self, other):
        return self.n == other.n
    def __lt__(self, other):
        return self.n < other.n
    def __gt__(self, other):
        return self.n > other.n
    
    def __str__(self):
        return str(self.n)
    
n1 = Number(30)
n2 = Number(10)

print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)

print(n1==n2)
print(n1<n2)
print(n1>n2)
print(str(n1))
