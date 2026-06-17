'''
#Local Access
def display():
    n=10
    print("Inside:",n)
display()


#Global Access
n=10
def display():
    print("Inside:",n)
display()
print("Outside:",n)
    

#Inside Global access
def display():
    global n
    n=10
    print("Inside:",n)
display()
print("Outside:",n)
    

def display():
    global n
    n+=10
    print("Inside:",n)
n=10
display()
print("Outside:",n)
    

#Inner Fun
def outer():
    n=10
    def inner():
        nonlocal n
        n+=10
        print("Inner function:",n)
    inner()
    print("Outer function:",n)
outer()


#Scope Loss
s='Python'
print(len(s))
len=5
print(len(s))

'''


'''
# Immutable (or pass by values) can be updated only inside and not outside like integer, float, string, tuple, bool
# Muttable (or pass by reference) can be updated on both inside and outside like list, set, dictionary

#Pass by value

# Integer
def update(n):
    n += 1
    print("Inside:",n)

n=5
update(n)
print("Outside:",n)

# Output:
# Inside: 6
# Outside: 5

# Float
def update(x):
    x += 1.5
    print("Inside :", x)

x = 2.5
update(x)
print("Outside:", x)

# Output:
# Inside : 4.0
# Outside: 2.5

# Complex
def update(c):
    c += 1 + 2j
    print("Inside :", c)

c = 3 + 4j
update(c)
print("Outside:", c)

# Output:
# Inside : (4+6j)
# Outside: (3+4j)

# String
def update(s):
    s += " World"
    print("Inside :", s)

s = "Hello"
update(s)
print("Outside:", s)

# Output:
# Inside : Hello World
# Outside: Hello

# Tuple
def update(t):
    t += (4,)
    print("Inside :", t)

t = (1, 2, 3)
update(t)
print("Outside:", t)

# Output:
# Inside : (1, 2, 3, 4)
# Outside: (1, 2, 3)

# Bollean
def update(s):
    s = False
    print("Inside :", s)

s = True
update(s)
print("Outside:", s)

# Output:
# Inside : False
# Outside: True

# Pass by reference

# List
def update(lst):
    lst.append(4)
    print("Inside :", lst)

lst = [1, 2, 3]
update(lst)
print("Outside:", lst)

# Output:
# # Inside : [1, 2, 3, 4]
# Outside: [1, 2, 3, 4]

# Set
def update(s):
    s.add(4)
    print("Inside :", s)

s = {1, 2, 3}
update(s)
print("Outside:", s)

# Output:
# Inside : {1, 2, 3, 4}
# Outside: {1, 2, 3, 4}


# Dicitonary
def update(d):
    d["age"] = 25
    print("Inside :", d)

d = {"name": "John"}
update(d)
print("Outside:", d)

# Output:
# Inside : {'name': 'John', 'age': 25}
# Outside: {'name': 'John', 'age': 25}
'''


# Recursion: A function calling itself

# syntax
# def func(attribute):
#     if base_condition:
#         return 
#     func(attribute_logic)

# looping using recursion
def func(n):
    if n == 0:
        return 
    print(n,end='') #54321
    func(n-1)

    print(n,end=' ') #1 2 3 4 5

func(5)


# reverse a string
def rev(s,ind):
    if ind == 0:
        return s[0]
    return s[ind]+rev(s,ind-1)

a="Python"
print(rev(a, len(a)-1))