# syntax:
# var = lambda agr : exp

add = lambda a,b: a+b
print(add(60,9))
print(add(6,19))

wish = lambda name: f'Welcome the python course {name}'
print(wish('Dinesh'))
print(wish('Ajay'))

gst = lambda price: price+ price*0.18
print(gst(100000))
print(gst(159220))
print(gst(874565))

#less than or Greater
greatest=lambda a,b:a if a>b else b
print(greatest(10,3))
print(greatest(9,22))
print(greatest(4,4))


#Even or Odd
iseven=lambda a:f'{a}--Even Number' if a%2==0 else f'{a}--Odd Number'
print(iseven(9))
print(iseven(10))
print(iseven(124))


bill=lambda charge:charge if charge>99 else charge+30
print(bill(990))
print(bill(90))
print(bill(190))
print(bill(100))
print(bill(99))



#less than or Greater
greatest=lambda a,b:a if a>b else b
print(greatest(10,3))
print(greatest(9,22))
print(greatest(4,4))


#Even or Odd
iseven=lambda a:f'{a}--Even Number' if a%2==0 else f'{a}--Odd Number'
print(iseven(9))
print(iseven(10))
print(iseven(124))


#
bill=lambda charge:charge if charge>99 else charge+30
print(bill(990))
print(bill(90))
print(bill(190))
print(bill(100))
print(bill(99))


#
login=False
instock=False

status=lambda login,instock:("you can buy product" if instock else "product is out of stack") if login else "login to buy a product"
print(status(login,instock))


##---MAP---##
#List
l=[1,2,3,4,5,6,7]
res=list(map(lambda i:i**3,l))
print(res)


#Title
names=['Naresh','akhil','ajay']
t=list(map(lambda i:i.title(),names))
print(t)


#Filter
l=[1,2,3,4,5,6,7,8,9,10,11,12]
res=list(filter(lambda i:i%2==0,l))
print(res)


l=[1,2,3,4,5,6,7,8,9,10,11,12]
res=list(filter(lambda i:i>5,l))
print(res)


l=[1,2,3,4,5,6,7,8,9,10,11,12]
res=list(filter(lambda i:i%3==0,l))
print(res)


from functools import reduce
l=[1,2,3,4,5,6,7,8,9]
s=reduce(lambda sum,i:sum+i,l)
p=reduce(lambda pro,i:pro*i,l)
print(s,p)


from functools import reduce
l=[1,2,3,4,5,6,7,8,9]
s=reduce(lambda sum,i:sum+i,l)
p=reduce(lambda pro,i:pro*i,l)
m=reduce(lambda max,i:max if max>i else i,l)
mi=reduce(lambda max,i:max if max<i else i,l)

print(s,p,m,mi)


d={'subbu':50,'nagendra':40,'naresh':60,'dinesh':80,'sahith':70}
print(dict(sorted(d.items())))
print(dict(sorted(d.items(),key=lambda i:i[1])))
print(dict(sorted(d.items(),reverse=True)))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))

d={'sugar':40, 'salt':20,'cooking oil':80,'chilli':60}
res=dict(map(lambda i: (i[0],i[1]+i[1]*0.18), d.items()))
res1=dict(map(lambda i: (i[0],i[1]-i[1]*0.5), d.items()))
print(res)
print(res1)

res=dict(filter(lambda i: i[1]>50, d.items()))
res1=dict(filter(lambda i: i[1]<50, d.items()))
print(res)
print(res1)