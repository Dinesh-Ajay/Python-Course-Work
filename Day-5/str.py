#string
# 1. Concatination

a="Aj"
b="ay "
c=a+b
print(a + b,c)
#Output: Ajay Ajay

# 2. Reptection

a='*'
print(a*10, c*7)
b=5
print(b*5) # this will be an operation not repeation

# 3. Indexing

s = "Python"

print(s[0])    # P (First Character)
print(s[1])    # y
print(s[2])    # t
print(s[-1])   # n (Last Character)
print(s[-2])   # o (Second Last Character)


# 4. Slicing

s = "Python"

print(s[0:3])   # Pyt
print(s[1:5])   # ytho
print(s[:4])    # Pyth
print(s[2:])    # thon
print(s[:])     # Python
print(s[::-1])  # nohtyP (Reverse String)


# 5. Membership

s = "Python Programming"

print("Python" in s)      # True
print("Java" in s)        # False
print("Java" not in s)    # True
print("gram" in s)        # True
