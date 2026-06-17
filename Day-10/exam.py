

# salary=int(input())
# bonus=0
# if salary >= 70000:
#     bonus=salary*0.2
# elif salary >= 50000:
#     bonus=salary*0.15
# elif salary >= 30000:
#     bonus=salary*0.1
# else:
#     bonus=salary*0.05
# print("Bonus:",bonus)



# tup=tuple(input("Tuple:").split())
# pro=input("Product:")
# pri=int(input("Price:"))
# s=set(map(int,input("Set values:").split()))
# print("Tuple:",tup)
# d={}
# d[pro]=pri
# print("Dictionary:",d)
# print("Set:",s)




# n=list(map(int,input().split()))
# print("Length:",len(n))
# print("sorted list:",sorted(n))
# print("maximum:",max(n))
# print("minimum:",min(n))



# age=int(input())
# if age>=18:
#     print("Eligible for Voting")
# else:
#     print("Not Eligible for Voting")

'''

marks=int(input())
if marks>=35:
    print("Pass")
else:
    print("Fail")'''


# data={
#     'subbu':{'status':True,'python':98,'mysql':95,'flask':94},
#     'naresh':{'status':True,'python':78,'mysql':85,'flask':84},
#     'dinesh':{'status':False,'python':None,'mysql':None,'flask':None},
#     'nagendra':{'status':True,'python':68,'mysql':65,'flask':54},
#     'rishi':{'status':True,'python':33,'mysql':25,'flask':34},
#     }
# name=input("Enter the name: ")
# if name in data:
#     if data[name]['status']:
#         total=data[name]['python']+data[name]['mysql']+data[name]['flask']
#         avg=total/3
#         if avg > 90:
#             print(f"Congrations {name}, you got first class!!!")
#         elif avg > 70:
#             print(f"Good {name}, keep it the next time!!")
#         elif avg>35:
#             print(f"Better {name}, work hard next time!")
#         else:
#             print(f" {name}, you have failed in the exam.Bring your paresnts.")
#     else:
#         print(f"{name} did't write the exam.Bring your parents")
# else:
#     print(f"{name}'s data is not found")

budget=int(input("Enter the budget: "))
if budget > 50000:
    print("you can go for the trip")
elif budget > 30000:
    print("you can go for the pub")
elif budget > 10000:
    print("you can go for the shopping")
elif budget > 5000:
    print("you can go for the cafe")
elif budget > 2000:
    print("you can go for the movie")
elif budget > 500:
    print("you can recharge your phone")
else:
    print("Take Rest")

