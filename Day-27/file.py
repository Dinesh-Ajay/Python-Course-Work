'''
file = open('data.txt','r')

print(len(file.readlines()))
file.seek(0)
print(file.read())
file.seek(55)
print(file.readline())
file.seek(200)
print(file.readlines())

file.close()

try:
    file = open('data.txt','r')

except FileNotFoundError:
    print("file is not available")

else:
    print(len(file.readlines()))
    file.seek(0)
    print(file.read())
    file.seek(55)
    print(file.readline())
    file.seek(200)
    print(file.readlines())

    file.close()

# we can open the file and it will automatically close the file
with open('data.txt','r') as file:
    print(len(file.readlines()))
    file.seek(0)
    print(file.read())
    file.seek(55)
    print(file.readline())
    file.seek(200)
    print(file.readlines())




# We can append the data in the file
with open('names.txt','a') as file:
    file.write("Ajay\nshiva\nDinesh\nVijay")

# we can write the code but it will override the code in the file
with open('names.txt','w') as file:
    file.write("Ajay\nshiva\nAj")


# we can perform multiple mode operations with + when declaring the mode 
with open('names.txt','a+') as file:
    file.seek(0)
    print("data in the file before operation:\n",file.read())   
    file.write("Aj\nshiva\nAj\nVijay")
    file.seek(0)
    print("data in the file after append operation:\n",file.read())

with open('names.txt','w+') as file:
    file.seek(0)
    print("data in the file before operation:\n",file.read())    
    file.write("Ajay\nshiva\nDinesh\nVijay")
    file.seek(0)
    print("data in the file after write operation:\n",file.read())
'''


import os

# os.mkdir("sample")
os.rmdir("sample")
