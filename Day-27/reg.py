import re
pattern1 = '[a-z]'
pattern2 = '[A-Z]'
pattern3 = '[0-9]'
pattern4 = '[ @#!$%^&*()_-]'

text = 'python@_Version_3.11'
'''
res = re.match(pattern1,text)
print(res)
print(res.group)
print(res.group() if res else "No Match Found")

res = re.search(pattern3,text)
print(res)
# print(res.group) Error occurs whihle searching no obj is returned
print(res.group() if res else "No Match Found")

res = re.search(pattern2,text)
print(res)
# print(res.group) Error occurs whihle searching no obj is returned
print(res.group() if res else "No Match Found")

res = re.search(pattern4,text)
print(res)
# print(res.group) Error occurs whihle searching no obj is returned
print(res.group() if res else "No Match Found")

res = re.findall(pattern1,text)
print(res)
res = re.findall(pattern2,text)
print(res)
res = re.findall(pattern3,text)
print(res)
res = re.findall(pattern4,text)
print(res)


res = re.finditer(pattern1,text)
for i in res:
    print(i.group(), i.start())

res = re.finditer(pattern2,text)
for i in res:
    print(i.group(), i.start())

res = re.finditer(pattern3,text)
for i in res:
    print(i.group(), i.start())

res = re.finditer(pattern4,text)
for i in res:
    print(i.group(), i.start())
'''

pattern5 = '[0-9]{9}'
text1 = '123456709'

res= re.fullmatch(pattern5, text1)
print(res.group() if res else "No Match Found")


pattern6 = r'[,a+yn]'
text2 = 'java,python,c++,html'

res = re.split(pattern6,text2)
print(res)

pattern7 = r'[0-9]{2}'
text3 = 'java: 97, python: 99, c++: 43, html: 98'

res = re.sub(pattern7,"@@",text3)
print(res)

