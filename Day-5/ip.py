name = input("Enter your Name: ")# input defaultly converts the input into String
print(name)
age = input("Enter your age: ")
print(age)
print(type(age))
age = int(input("Enter your age: "))
print(age)
print(type(age))
gpa = float(input("Enter your GPA: "))
print(gpa)
print(type(gpa)) 
List_names = input("Enter Names or Numbers: ").split() # Naga Subbu Veni Anil Ali Ajay
# input defaultly converts the huge input into list 
print(f'\nList_names: {List_names}')
print(f'\nType of List_names[0] : {type(List_names[0])}\n')
List_names_1 = list(map(int, input("Enter Numbers: ").split())) # 7 2 9 4 2 6 3 8 8 5 1
print(f'\nList_names_1: {List_names_1}')
print(f'\nType of List_names_1[0] : {type(List_names_1[0])}\n')
Tuple_names = tuple(map(int, input("Enter Numbers: ").split())) # 7 2 9 4 2 6 3 8 8 5 1
# Only takes integers as input
print(f'\nTuple_names: {Tuple_names}')
print(f'\nType of Tuple_names[0] : {type(Tuple_names[0])}\n')

Tuple_names_1 = tuple(input("Enter Names or Numbers: ").split()) # laptop mouse keyboard
# Only takes string as input
print(f'\nTuple_names_1: {Tuple_names_1}')
print(f'\nType of Tuple_names_1[0] : {type(Tuple_names_1[0])}\n')
Set_names = set(input("Enter Names or Numbers: ").split()) # in not in is is not and or not
print(f'\nSet_names: {Set_names}\n')
# print(type(Set_names[0])) 
Set_names_1 = set(map(int, input("Enter Numbers: ").split()))
print(f'\nSet_names_1: {Set_names_1}\n')
# print(type(Set_names_1[0])) 
# We can use float and other data types too

username, password = input('Enter Username & Password: ').split()
print(f'\nUsername: {username} & Password: {password}\n')

a,b,c,d = list(map(int, input("Enter Numbers: ").split()))
print(a,b,c,d)

price, dis = list(map(float, input("Enter Price & Discount: ").split()))
print(f'\nPrice: {price} & Discount: {dis}\n')

n= int(input("Enter your Number : "))
for i in range(n):
    a=eval(input('\nEnter Any Input in any Data Type: '))
    print('\n',a, type(a))

'''
Enter your Name: Ajay
Ajay
Enter your age: 21
21
<class 'str'>
Enter your age: 21
21
<class 'int'>
Enter your GPA: 7.5
7.5
<class 'float'>
Enter Names or Numbers: 7 2 9 4 2 6 3 8 8 5 1

List_names: ['7', '2', '9', '4', '2', '6', '3', '8', '8', '5', '1']

Type of List_names[0] : <class 'str'>

Enter Numbers: 7 2 9 4 2 6 3 8 8 5 1

List_names_1: [7, 2, 9, 4, 2, 6, 3, 8, 8, 5, 1]

Type of List_names_1[0] : <class 'int'>

Enter Numbers: 7 2 9 4 2 6 3 8 8 5 1

Tuple_names: (7, 2, 9, 4, 2, 6, 3, 8, 8, 5, 1)

Type of Tuple_names[0] : <class 'int'>

Enter Names or Numbers: 7 2 9 4 2 6 3 8 8 5 1

Tuple_names_1: ('7', '2', '9', '4', '2', '6', '3', '8', '8', '5', '1')

Type of Tuple_names_1[0] : <class 'str'>

Enter Names or Numbers: 7 2 9 4 2 6 3 8 8 5 1

Set_names: {'5', '7', '2', '4', '6', '1', '9', '3', '8'}

Enter Numbers: 7 2 9 4 2 6 3 8 8 5 1

Set_names_1: {1, 2, 3, 4, 5, 6, 7, 8, 9}

Enter Username & Password: Ajay 2146098765

Username: Ajay & Password: 2146098765

Enter Numbers: 2 4 5 7
2 4 5 7
Enter Price & Discount: 223566 24

Price: 223566.0 & Discount: 24.0

Enter your Number : 2

Enter Any Input in any Data Type: ['7', '2', '9', '4', '2', '6', '3', '8', '8', '5', '1']

 ['7', '2', '9', '4', '2', '6', '3', '8', '8', '5', '1'] <class 'list'>

Enter Any Input in any Data Type: (7, 2, 9, 4, 2, 6, 3, 8, 8, 5, 1)                      

 (7, 2, 9, 4, 2, 6, 3, 8, 8, 5, 1) <class 'tuple'>
'''