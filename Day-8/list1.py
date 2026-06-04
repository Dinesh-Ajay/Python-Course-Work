
l=[10,20,30,40,90]

print(l, l.insert(1,20), l,
    l.insert(6,69),l,
    l.extend([80,90,110]),l,
    l,
    l.pop(),
    l,
    l.pop(),
    l,
    l.pop(3),
    l,
    # l.pop(9), pop index out of range 
    l,
    l.pop(2),
    l,
    l.remove,
    l,
    # l.remove(50), list.remove(x): x not in list 
    #l.remove(300), list.remove(x): x not in list
    l,sep='\n')
del l[1] # because del does not return anything and cannot be assigned.
print(l)
print(l.clear(),l)
'''
clear() removes all elements from the list.
Since Python evaluates all arguments to print() before printing, by the time many references to l are displayed, l has already become an empty list.
'''
l=[200,30,45,456,68,456,900,469]

print('new', l,
    sorted(l),
    l.sort(),
    l,
    min(l),
    max(l),
    l,
    l.reverse(),
    l,
    l.reverse(),
# l.sorted(reverse=True)
# Traceback (most recent call last):
#   File "<pyshell#124>", line 1, in <module>
#     l.sorted(reverse=True)
# AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
# l.sorted(l,reverse=True)
# Traceback (most recent call last):
#   File "<pyshell#125>", line 1, in <module>
#     l.sorted(l,reverse=True)
# AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
    sorted(l,reverse=True),
    l,
    l.index,
    l.index(200),
    l.index(469),
    l.count(900),
    l.append(30),
    l,
    l.count(30),
    l,
    any([1,2,3,4,0,0,0,0,0,0]),
    all([1,2,3,4,5,0,0,0,0]),sep='\n')