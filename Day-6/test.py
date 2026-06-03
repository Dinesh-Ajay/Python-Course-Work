name=input()
rollno = int(input())
s1=int(input())
s2=int(input())
s3=int(input())
total=s1+s2+s3
avg=total/3
print(f"Student Name: {name}\nRoll Number: {rollno}\nTotal Marks: {total}\nAverage marks: {avg}")

a=input()

print("Total Characters:",len(a))
print("First Characters:",a[0])
print("Last Characters:",a[-1])
print("Uppercase:",a.upper())
print("Reversed String:",a[::-1])

a,b,c=list(map(int,input().split()))
total=a+b+c
avg=total/3
print(f"Sum: {total}\nAverage: {avg}\nProduct: {a*b*c}")