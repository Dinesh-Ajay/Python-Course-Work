#Control Statements------
#for loop -----> iterates over seq.

'''
for var in seq:
    print(var)


#string

s='python programming'
for ch in s:
    print(ch)
    

#List

l=['sugar','salt','rice','oil']
for ch in l:
    print(ch)




#tuple

t=('1.token','2.Tokens','3.Data types')
for i in t:
    print(i)




#set

s={'laptop','mouse','kayboard','monitor'}
for i in s:
    print(i)




#dict

d={'name':'naresh','batch':55,'course':'pfs','skills':['python','flask','mysql']}
for i in d:
    print(i)



#range(start,stop+1,step) => (0,n,1)

for i in range(1,11):
    print(i)



for i in range(2,51,2):
    print(i)



for i in range(5,101,5):
    print(i)
    


for i in range(20,0,-1):
    print(i)




for i in range(6):
    print(i)




for i in range(30,2,-3):
    print(i)



s='looping Statements'
for i in range(len(s)):
    print(i,s[i])






l=[2,4,6,7,3,6,9,6,9]
for i in range(len(l)):
    print(i,l[i])






l=(3,5,7,9,4,6,7,79)
for i in range(len(l)):
    print(i,l[i])




s='looping'
for i in enumerate(s):
    print(i[0],i[1])



l=[4,6,7,4,3,6,9,8]
for i in enumerate(l):
    print(i[0],i[1])




t=(4,5,6,8,9,4,2,5,7)
for i in enumerate(t):
    print(i[0],i[1])




k={2,4,6,8,0,4,6,8,9}
for i in enumerate(k):
    print(i[0],i[1])

'''
a='looping Statement'

for i in a:
    if i in 'AEIOUaeiou':
        print(i,"is a vowel")
    # else:
    #     print(i,"is not vowel")
'''
l=[56,86,9,45,3,6,7,9,98,67,45,43,55,78,68]
for i in l:
    if i%2==0:
        print(i)



d={'loptops':0,'chargers':2,'keyboard':10,'phone':12,'tab':23,'mouse':21}
for i in d:
    if d[i]:
        print(i)




t=(5,6,7,8,9,3,2,4)
for i in range(len(t)):
    print(i*t[i])



names={'subbu','naresh','dinesh','sahith','rushi','praneeth'}
for i in names:
    print(i.upper())
'''