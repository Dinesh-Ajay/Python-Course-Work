# syntax mistake is compiler error
# logical mistakes causes run time error
# value,name,index,key,type error are all run time error

'''
#Exception Handlings

try:
    a=int(input("Enter tha age:"))
except ValueError:
    print("Enter the age in a digit[0-9] format")
else:
    print("Age:",a)
finally:
    print("Thankyou")






#Multiple Errors

try:
    a=int(input("Enter tha age:"))
    print(12/0)
    print(b)
    print(13+'14')
    d={1:1,2:2,3:322,4:4}
    print(d[5])
    l=[1,2,3]
    print(l[10])
except ValueError:
    print("Enter the age in a digit[0-9] format")
except ZeroDivisionError:
    print("Can't divid with zero")
except NameError:
    print("define the war")
except TypeError:
    print("Add the same datatypes")
except KeyError:
    print("Key is not present")
except IndexError:
    print("Index is out of range")
    
else:
    print("Age:",a)
finally:
    print("Thankyou")




#
try:
    a=int(input("Enter tha age:"))
    print(12/0)
    print(b)
    print(13+'14')
    d={1:1,2:2,3:3,4:4}
    print(d[5])
    l=[1,2,3]
    print(l[10])
except (ValueError,ZeroDivisionError,NameError,TypeError,KeyError,IndexError) as a:
    print("Error Occured:",e)
else:
    print("No Error Occured")
finally:
    print("Thankyou")


'''
try:
    a=int(input("Enter tha age:"))
    print(12/0)
    print(b)
    print(13+'14')
    d={1:1,2:2,3:3,4:4}
    print(d[5])
    l=[1,2,3]
    print(l[10])
except Exception as e:
    print("Error Occured:",e)
else:
    print("No Error Occured")
finally:
    print("Thankyou")

try:
    amount = int(input("Enter amount to withdraw: "))
    if amount<0:
        raise Exception("Enter the amount grater than zero")

except Exception as e:
    print("Error occured:",e)
else:
    print("No Error occured")
finally:
    print("Thank You")