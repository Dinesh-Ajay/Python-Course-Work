'''
import sys

print(sys.argv)
print(sys.path)
print(sys.version)

print("Before Exit")
sys.exit()
print("After  exit")

import platform

print(platform.system(), platform.release(),platform.processor())

import math

print(math.pi)
print(math.e)

print(math.sqrt(81))
print(math.pow(2,5))

print(math.ceil(12.3))
print(math.ceil(12.00001))
print(math.ceil(12.9))

print(math.floor(12.3))
print(math.floor(12.00009))
print(math.floor(12.8))

print(math.fabs(-12))
print(math.factorial(5))
print(math.gcd(8,28))

print(math.log(10,10))
print(math.sin(10))
print(math.cos(10))
print(math.tan(10))

print(math.degrees(20))
print(math.radians(20))


#random
import random

print(random.random())
print(random.randint(1,6))
print(random.uniform(1,6))

l=['python','c','c++','java','html']
print(random.choice(l))
print(random.choices(l,k=3))

s='rps'
print(random.choice(s))
print(l)
random.shuffle(l)
print(l)


#
import random

random.seed(9)
print(random.random())
print(random.randint(1,6))
print(random.uniform(1,6))

l=['python','c','c++','java','html']
print(random.choice(l))
print(random.choices(l,k=3))

s='rps'
print(random.choice(s))
print(l)
random.shuffle(l)
print(l)



import collections

a='Python programming language'
print(collections.Counter(a))

d={}

for i in a:
    d[i] = d.get(i,0)+1

print(d)

s=collections.defaultdict(int)
for i in a:
    s[i] += 1

print(s)

l=collections.deque([])

print("\nfrom right side")
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.popleft()
l.popleft()
l.popleft()
l.append(50)
l.append(60)
l.popleft()
print(l)

l=collections.deque([])

print('\nfrom left side')

l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.appendleft(40)
l.pop()
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(60)
l.pop()

print(l)

'''

import itertools

l=list(itertools.combinations('abcd',2))
print(l)
print(list(itertools.permutations('abcd',2)))

res=[''.join(i) for i in l]
print(*res)
