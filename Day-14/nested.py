'''
n = int(input("Enter the size: "))
m=n//2

for i in range(n):
    if i<=m:
        print(' '*(m-i),end=' ')
        print('* '*(i+1),end=' ')
    else:
        print(' '*(i-m),end=' ')
        print('* '*(n-i),end=' ')
    print()

for i in range(n):
    if i<=m:
        print(' '*(m-i)+'* '*(i+1),end=' ')
        
    else:
        print(' '*(i-m)+'* '*(n-i),end=' ')
    print()

'''


n = int(input("Enter the size: "))
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# output:
# Enter the size: 8
# * * * * * * * * 
# *             * 
# *             * 
# *             * 
# *             * 
# *             * 
# *             * 
# * * * * * * * * 


# m=n//2
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1 or i==m or j==m:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# output:
# Enter the size: 5
# * * * * * 
# *   *   * 
# * * * * * 
# *   *   * 
# * * * * * 

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or j+i == (n-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Output:
# Enter the size: 5
# * * * * * 
# * *   * * 
# *   *   * 
# * *   * * 
# * * * * * 