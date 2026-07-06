import re

pattern=r'h.t\b'
text='hot hit het hrt hat hate hood heart hjt h$t'

res=re.findall(pattern,text)
print(res)

#^ starts with
pattern=r'^h'
text='hot hit het hrt hat hate hood heart hjt h$t'

res=re.findall(pattern,text)
print(res)

#$ checking for ends
pattern=r't$'
text='hot hit het hrt hat hate hood heart hjt h$t'
res=re.findall(pattern,text)
print(res)


#* 1 or many
pattern=r'to*'
text='too to t toooooo tooooooooo'

res=re.findall(pattern,text)
print(res)


#? atleast 1 or 0
pattern=r'to?\b'
text='too to t toooooo tooooooooo'

res=re.findall(pattern,text)
print(res)


#{}
pattern=r'[a-z]{5}'
text='gfd f ergde ugrdf hotde ghy tfrdtrs'

res=re.findall(pattern,text)
print(res)


#() exactly match pattern
pattern=r'(python)'
text='pyth  pythn python pythh'

res=re.findall(pattern,text)
print(res)



# Form validation

#Name validate
pattern=r'^[a-zA-Z] {2,15} ([a-zA-Z] {2,15})+$'
text=input("Enter the text:")
res=re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid format")


#Email validate
pattern=r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
text=input("Enter the text:")
res=re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid format")


#Phone number valid
pattern=r'^(?:\+91|0)?[6-9]\d{9}$'
text=input("Enter the text:")
res=re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid format")

#Password validate
pattern=r'^(?=.*[A-Z]) (?=.*[a-z]) (?=.*\d) (?=.*[@$!%*?&]) [A-Za-z\d@$!%*?&] {8,} $'
text=input("Enter the text:")
res=re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid format")

#Username validate
pattern=r'^[a-zA-Z0-9]{5,15}$'
text=input("Enter the text:")
res=re.fullmatch(pattern,text)
print("Valid format" if res else "Invalid format")


