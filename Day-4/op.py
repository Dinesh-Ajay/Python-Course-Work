# Operators 

# 1. Arithmatic Operators (+, -, *, /, %, //, **)
# 2. Comparsion Operators (<, >, ==, <=, >=, )
# 3. Assignment Operators (=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, <<=, >>=)
# 4. Logical Operators (and, or, not)
# 5. Membership Operators (in, not in)
# 6. Idetity Operators (is, is not) **checks the object reference**
# 7. Bitwise Operators (&, |, ^, ~, <<, >>)

a = 8
b = 4
print(f'a = {a}, b = {b}')
print("1. Arithmetic Operators")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / 3 =", a / 3)
print("a % 3 =", a % 3)
print("a // 3 =", a // 3)
print("a ** b =", a ** b)

print("\n2. Comparison Operators")
print("a < b =", a < b)
print("a > b =", a > b)
print("a == b =", a == b)
print("a <= b =", a <= b)
print("a >= b =", a >= b)
print("a != b =", a != b)

print("\n3. Assignment Operators")

x = a
x += b
print("a += b :", x)

x = a
x -= b
print("a -= b :", x)

x = a
x *= b
print("a *= b :", x)

x = a
x /= 3
print("a /= 3 :", x)

x = a
x %= 3
print("a %= 3 :", x)

x = a
x //= 3
print("a //= 3 :", x)

x = a
x **= 2
print("a **= b :", x)

x = a
x &= b
print("a &= b :", x)

x = a
x |= b
print("a |= b :", x)

x = a
x ^= b
print("a ^= b :", x)

x = a
x <<= 2
print("a <<= b :", x)

x = a
x >>= 2
print("a >>= b :", x)

a=20
b=10
print(f'\na = {a}, b = {b}')
print("\n4. Logical Operators")
print("(a > 10) and (b > 10) =", (a > 10) and (b > 10))
print("(a > 10) or (b > 20) =", (a > 10) or (b > 20))
print("not(a > b) =", not(a > b))

print("\n5. Membership Operators")

lst = [10, 20, 30, 40]
print("20 in lst =", 20 in lst)
print("12 not in lst =", 12 not in lst)

print("\n6. Identity Operators")

c = a
print(f'\nc = {c}')
print("a is c =", a is c)
print("a is not b =", a is not b)

a = 8
b = 4
print(f'\na = {a}, b = {b}')
print("\n7. Bitwise Operators")
print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("~a =", ~a)
print("~b =", ~b)
print("a << 2 =", a << 2)
print("a >> 2 =", a >> 2)

a=12
b=12.34
c='python'
print('a=',a,'b=',b,'c=',c)
print('a=',a,'b=',b,'c=',c,sep="")
print('a=',a,'b=',b,'c=',c,sep="@")
print('a=',a,'b=',b,'c=',c,end="\n\n")
print('a=',a,'b=',b,'c=',c,end="\n")
print('a=',a,'b=',b,'c=',c,sep="\t",end="@\n\n@")
print(f"a={a}, b={b}, c={c}")
print("a={}, b={}, c={}".format(a,b,c))
print("a={2}, b={0}, c={1}".format(a,b,c))
