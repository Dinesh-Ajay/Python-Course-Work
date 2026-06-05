#empty dic
d={}
d=dict()
print(type(d))

#dict-key
d={}
d[1]='int'
print(d)

d[2.34]='float'

print(d)

d[2+3j]='complex'
print(d)

d['str']='string'

print(d)

# d[[1,2,3,4]]='list'cannot use 'list' as a dict key

d[(1,2,3,4)]='tuple'
print(d)

# d[{1,2,3,4,5}]='set' cannot use 'set' as a dict key

# d[{'s1':1,'s2':2,'s3':3}]='dictionary' cannot use 'dict' as a dict key

d[False]='bool'
print(d)
#dict-key are must be mutable & uniqe

#dict-values

d={}
d[1]=1
print(d)

d[23]=23.4
print(d)

d[3]='werer'
print(d)

d[4]=3+4j
print(d)

d[5]=[1,2,3,4]
d[6]=(1,2,3,4)
d[7]={1,3}
d[8]={1:1,2:2}
d[9]=False
print(d)
#dict-values are allow all datatypes & duplicate values also

d={}
d[1]=14
print(d)

d={}
d[1]=2
d[2]=2
d[3]=2
d[4]=2
print(d)
#dict-values are allow duplicate values

#to acces values

d={1:2,2:4,3:6,4:8,5:10}
print(d,d[4],d[5],d[1])

d={'shiva':78,'kiran':90,'sunny':78,'ravi':23}
print(d,
  d['sunny'],
  d['shiva'],
  # d['rahul'], Their will be an error here
  d.get('rahul'),
  d.get("shiva"),
  d.get('rahul','user not found'),
  d.get("shiva","user not found"),

  #if value is not in dict then you can use above type
  d,
  'shiva' in d,
  'ramu' not in d,sep='\n')


#methods-dict

print(d.keys(),
d.values(),
d.items(),
sorted(d),
min(d),
max(d),
len(d),sep='\n')