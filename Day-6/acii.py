print(ord('a'),ord('A'),ord('m'),ord('M'),ord('f'),ord('c'),chr(97),chr(65),chr(37),chr(102),chr(46),chr(35),chr(40),chr(50),chr(99),chr(42),chr(63),chr(57),sep="\n")
'''
97
65
109
77
102
99
a
A
%
f
.
#
(
2
c
*
?
9
'''
s='Python Programming'
print(s.upper(),
      s.lower(),
      s.capitalize(),
      s.title(),
      s.swapcase(),
      "SCHWYFOWTDBAJWHV".casefold(),sep="\n")

'''
PYTHON PROGRAMMING
python programming
Python programming
Python Programming
pYTHON pROGRAMMING
schwyfowtdbajwhv
'''

print(s.center(38,'*'),
      s.center(28,'*'),
      s.center(28,'-'),
      s.ljust(28,'-'),
      s.rjust(28,'-'),
      '123'.zfill(5),
      '123'.zfill(10),
      '123'.zfill(3),
      '123'.zfill(2),sep="\n")

'''
**********Python Programming**********
*****Python Programming*****
-----Python Programming-----
Python Programming----------
----------Python Programming
00123
0000000123
123
123
'''

print(s.find('0'),
      s.find('o'),
      s.find('g'),
      s.rfind('o'),
      s.find('z'),
      s.index('o'),
      s.rindex('o'),
      s.count('y'),
      s.count('g'),
      s.count('m'),
      s.count('a'),
      sep='\n')

'''
-1
4
10
9
-1
4
9
1
2
2
1
'''

print(s.replace('python','java'),
      s.replace('python','java'),
      s.replace('Python','Java'),
      s.maketrans('Python','123456'),
      s.translate(s.maketrans('Python','123456')),sep='\n')

'''
Python Programming
Python Programming
Java Programming
{80: 49, 121: 50, 116: 51, 104: 52, 111: 53, 110: 54}
123456 1r5grammi6g
'''

s='java,python,javascript,c,c++'
print(s.split(','),
      s.split(',',2),
      s.rsplit(',',2),sep='\n')

'''
['java', 'python', 'javascript', 'c', 'c++']
['java', 'python', 'javascript,c,c++']
['java,python,javascript', 'c', 'c++']
'''

g='''gdsagdhwe
gerah;
dfsgD
DSGAWDGTEG'''
print(g)
'''
gdsagdhwe
gerah;
dfsgD
DSGAWDGTEG
'''

print(s.splitlines(), 
      g.splitlines(),sep='\n')

'''
['java,python,javascript,c,c++']
['gdsagdhwe', 'gerah;', 'dfsgD', 'DSGAWDGTEG']
'''

l=['java','python','javascript','c','c++']
print(''.join(l),
      '-'.join(l),
      '@'.join(l),
      ' '.join(l),
      ','.join(l),
      s,
      s.partition(','),
      s.rpartition(','),sep='\n')

'''
javapythonjavascriptcc++
java-python-javascript-c-c++
java@python@javascript@c@c++
java python javascript c c++
java,python,javascript,c,c++
java,python,javascript,c,c++
('java', ',', 'python,javascript,c,c++')
('java,python,javascript,c', ',', 'c++')
'''
