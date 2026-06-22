'''# Generator
def display():
    for i in range(1,11):
        yield i

n = display()
for i in range(10):
    print(next(n))

# factors
def factor(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i

n=factor(56)
try:
    while True:
        print(next(n))
except StopIteration:
    print("End of the programm")
'''
def factors(n):
    return [i for i in range(1,n+1) if n%i==0]

def generators(res):
    for i in res:
        yield i

res=factors(60)
facts=generators(res)
for i in range(len(res)):
    print(next(facts))

def primes():
    res=[]
    for num in range(2,101):
        for i in range(2,num//2+1):
            if num%i==0:
                break
        else:
            res.append(num)
    return res
def generators(res):
    for i in res:
        yield i

res=primes()
g=generators(res)
for i in range(len(res)):
    print(next(g))
