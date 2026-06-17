#---Functions---


'''
def function_name(arg):
    #stmts
    return
function_name(para)



def wish(name):
    print(f'Welcome to the python course {name}!')
wish('subbu')
wish('Naresh')
wish('ajay')
wish('akhil')




#Check Even or Odd
def iseven(num):
    if num%2==0:
        return f'{num} - Even Number'
    else:
        return f'{num} - Odd Number'
print(iseven(12))
print(iseven(13))



#Factorial

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
num=int(input("Enter the number: "))
print("Factorial:",factorial(num))


#Prime
def isprime(num):
    for i in range(2,num//2):
        if num%i==0:
            return f'{num} - Not Prime Number'
    return f'{num} - Prime Number'
num=int(input("Enter the number :"))
print(isprime(num))


#Position
def display(name,email,pwd):
    print('Name:',name)
    print('Email:',email)
    print('Password:',pwd)
display('Naresh','naresh@gmail.com','Naresh@123')
display('Naresh@gmail.com','Naresh','Naresh@123')



#Keyword

def display(name,email,pwd):
    print('Name:',name)
    print('Email:',email)
    print('Password:',pwd)
display(name='Naresh',email='naresh@gmail.com',pwd='Naresh@123')
display(email='naresh@gmail.com',name='Naresh',pwd='Naresh@123')

'''

#Default
def display(name,email,pwd=''):
    print('Name:',name)
    print('Email:',email)
    print('Password:',pwd)
display('Naresh','naresh@gmail.com','Naresh@123')
display('Naresh@gmail.com','Naresh')

#Default
def display(name,email,pwd=''):
    print('Name:',name)
    print('Email:',email)
    print('Password:',pwd)
display('Naresh','naresh@gmail.com','Naresh@123')
display('Naresh@gmail.com','Naresh')







def display(*names):
    print("Names:",names)
display('subbu','naresh','ajay','akhil')
display('subbu','naresh','akhil')
display('akhil')






#Keyword variable
def display(**names):
    print("Names:",names)
display(k1='subbu',k2='naresh',k3='ajay')
display(k1='subbu',k2='naresh',k3='akhil')
display(k1='akhil')