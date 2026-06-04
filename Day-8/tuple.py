#Tuple
t=(1,1,1,1,1,1)
print(t)
t=(10,20,30,40)
h=(50,60,70)
print(t+h,
    t*4,
    t,
    t[2],
    t[3],
    t[-2],
    t[-1],
    t,
# t(:3)
# SyntaxError: invalid syntax
    t[:3],
    t,
    t[3:],
    t[1:4],
    t[2:],
    t[::2],
    t[-1:-4:-1],
    t,
    10 in t,
    90 in t,
    100 not in t,
    len(t),
    sorted(t),
    min(t),
    max(t),t.count(10),
    t.index(10),
    sep='\n')

a=(1,2,3)
print(a)

x,y,z=a
print(x,y,z,sep='\n')

t=(1,2,3,[4,5,6],7,8)
print(t,
    t[3].append(10),
    t,
    t[3],
    t,sep='\n')