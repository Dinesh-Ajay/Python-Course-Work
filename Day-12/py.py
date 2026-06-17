'''
user = input('Enter User name: ')
password = int(input("Enter the password: "))
print("--Login--")
u_id=input('Enter User name: ')
a=5
for i in range(a):
    p_id=int(input("Enter the password: "))
    if password == p_id:
        print(f"Successfully logined {u_id}")
        break
    else:
        print(f"Try again u have {a-i} chances")
'''
'''
l=[2,3,5,6,8,10,34,12]
a=int(input('Enter the Number: '))
# if a in l:
#     print(f'Index of the Number {a} is {l.index(a)}')
# else:
#     print("Entered wrong Number",a)
# or
for i in range(len(l)):
    if l[i] == a:
        print(f'Index of the Number {a} is {i}')
        break
else:
    print("Entered wrong Number",a)
'''

'''
user = input('Enter User name: ')
password = input("Enter a strong password(Capital, Numeric, Special Characters, with atleast 8 chartacters): ")
if len(password)>=8:
    s=set()
    for i in password:
        if i.isupper():
            s.add("U")
        elif i.islower():
            s.add("l")
        elif i.isdigit():
            s.add("d")
        else:
            s.add("S")
    if len(s) == 4:
        print("Strong password")
    else:
        print('Weak password')

else:
    print('The password should have atleast 8 chatacters Try again')

'''

# s= None
# assert s!=None, "Update it"
# print(s)

'''
# Leetcode
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l=[]
        for i in range(1,n+1):
            if i %3 == 0 and i%5==0:
                l.append("FizzBuzz")
            elif i%3==0:
                l.append("Fizz")
            elif i%5==0:
                l.append("Buzz")
            else:
                l.append(f"{i}")
            
        return l


'''
