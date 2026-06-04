#Sets
s={1,2,3,4}
print(s)

s=set()
s={1,1,1,1,1,1,1}
print(s)

s={123,643,7644,7,975,90,6,908,3}
print(s)

s=set()
print(s.add(1))
print(s)

s={123,643,7644,7,975,90,6,908,3}
print(s)

# print(s.add(47,48))
# Traceback (most recent call last):
#   File "<pyshell#64>", line 1, in <module>
#     s.add(47,48)
# TypeError: set.add() takes exactly one argument (2 given)

s=set()
print(s.add(1),s)
# add() will return None

print(s.add(54.43),s)
s.add("dfghj")
print(s,
    1 in s,
    2 in s,
    43 not in s,sep='\n')

a={1,2,3,5,6,8,9,10}
b={6,7,8,9}
print(a | b,
    a.union(b),
    a.intersection(b),
    a & b,
    a - b,
    a ^ b,
    a,
    #{1}{2}{3}{4}{5{6}
    a<={1},
    a>={1},
    a.isdisjoint(b),
    a.isdisjoint({90,80}),
    a,
    a.add(69),
    a,
    a.add(19),
    a,
    a.update({11,12,13}),
    a,
    a.pop(),
    a.pop(),
    a.remove(13),
    s,
    a,
    a.remove(11),
    a,
    s.discard(6),
    a.discard(6),
    a,
    a.discard(3),
    a,
    a.clear(),sep='\n')

a={1,4,23,57,235}
print(a)

b={1,2,4,34}
print(b,
      a.intersection_update(b),
    a,
    b,sep='\n')

c=b
print(c.add(12), c,sep='\n')

d=c.copy()
print(d.add(10),
    d,
    c,
    len(c),
    min(c),
    max(c),
    sorted(c),
    sum(c),sep='\n')