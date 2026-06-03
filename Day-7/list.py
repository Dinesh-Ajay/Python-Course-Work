l=[]
l=list()
print(type(l))
l=[1,2,3,4]
m=[5,6,7,8,9]

print(l+m,l*4,sep='\n')



l=[10,20,30,40,90]
print(l[4],l[2],l,
    l[-3],
    l[-1],
    l[1],
    l[1:4],
    l[::-1],
    l[-1:-4:-1],
    l[-3::-1],
    l,
    20 in l,
    40 in l,
    100 in l,
    90 not in l,
    70 in l,
    l,
    id,
    l,
    id(l),
    l[1],
    l,sep='\n')
l[1]=70

print(l,id(l),sep='\n')

l[4]=90

print(l,
    l,
    l.append(120),
    l,
    l.append(300),
    l,sep='\n')