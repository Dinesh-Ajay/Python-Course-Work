'''res=[]
for i in range(1,11):
    res.append(i)

res1=[i for i in range(1,11)]

print(res,res1)

res2=[]
for i in range(3,31,3):
    res2.append(i)

res3=[i for i in range(3,31,3)]
res4=[i for i in range(2,51,2)]

print(res2,res3,res4)

a="python Programming"
l=[]
for i in a:
    if i in "aeiouAEIOU":
        l.append(i)
print(l)

l1=[i for i in a if i in "aeiouAEIOU"]
print(l1)


a=[1,2,35,68,90,15,79,3,6,0,26,89,13,56,23,232,567766,456]
l2=[]
for i in a:
    if i%2==0:
        l2.append(i)
    else:
        l2.append(0)

print(l2)

l3=[i if i%2==0 else 0 for i in a ]
print(l3)

l4=[int(input(f'Enter the number - {i+1} : ')) for i in range(10)]
print(l4)

l5=[]
for i in range(3):
    res=[]
    for j in range(1,4):
        res.append(j)
    l5.append(res)
print(l5)

l6=[[j for j in range(1,4)] for i in range(3) ]
print(l6)

s=set()
for i in range(1,11):
    s.add(i)
print(s)

#Comp
s1={i for i in range(1,11)}
print(s1)


##Dict Comp
d={}
for i in range(1,11):
    d[i]=i*i
print(d)


#comp
res={i:i*i for i in range(1,20)}
print(res)



#Comp
res={input("Enter the name: "):int(input("Enter the Mark: "))for i in range(5)}
print(res)
'''

def display():
    l=['1...50','51...100','101...150','151...200']
    yield l[0]
    yield l[1]
    yield l[2]
    yield l[3]
scroll=display()

print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))