n=int(input("enter the num: "))

if n>0:
    print("+ve")
elif n<0:
    print("-ve")
else:
    print("Zero")
    
data = ('abc','123')


username,password = input("enter the username and password: ").split()

if data ==(username,password):
    print("login succesful")
else:
    print("invalid login")
    
products = {
    'laptops':0,
    'mouse':10,
    'charger':5,
    'phones':30,
    'keyboard':0
}

product = input("Enter the product: ")

if product in products:
    if products[product]!=0:
        print(f"you can buy {product}!!")
    else:
        print(f"{product} is out of stock")
else:
    print(f"{product} is not available")


s='python programming'
if 'python' in s:
    print('python found')

if s[0]=='p':
    print("string is starting with p")
