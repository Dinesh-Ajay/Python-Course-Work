# alpha = input("Enter a alphabet: ") for single character
list_alpha = list(input("Enter a alphabets: ").upper()) # for multiple character
print(list_alpha)
n = int(input("Enter the size of the alphabets: "))
m=n//2
'''
# 1. for A
for i in range(n):
    for j in range(n):
        if i==0 or i==m or j==0 or j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# Output:
# Enter the size: 5
# * * * * * 
# *       * 
# * * * * * 
# *       * 
# *       * 

# 2. for B
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==m or j==0 or j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# Output:
# Enter the size: 5
# * * * * * 
# *       * 
# * * * * * 
# *       * 
# * * * * * 

# 3. for C
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# Output:
# Enter the size: 5
# * * * * * 
# *         
# *         
# *         
# * * * * * 

# 4. for D
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# Output:
# Enter the size: 5
# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * *

# 5. for E
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==m or j==0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# Output:
# Enter the size: 5
# * * * * * 
# *         
# * * * * * 
# *         
# * * * * * 

# 6. for F

for i in range(n):
    for j in range(n):
        if i==0 or i==m or j==0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# Output:
# Enter the size: 5
# * * * * * 
# *         
# * * * * * 
# *         
# *         

# 7. for G

for i in range(n):
    for j in range(n):
        if i==0 or (i==m and j>m) or (i==n-1 and j<=m) or (j==m and i>=m) or (j==n-1 and i>=m) or j==0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()

# Output:
# Enter the size: 5
# * * * * * 
# *         
# *   * * * 
# *   *   * 
# * * *   * 

# 8. for H

for i in range(n):
    for j in range(n):
        if i==m or j==0 or j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# Output:
# Enter the size: 5
# *       * 
# *       * 
# * * * * * 
# *       * 
# *       * 

# 9. for I

for i in range(n):
    for j in range(n):
        if j==m or i==0 or i==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# Output:
# Enter the size: 5
# * * * * * 
#     *     
#     *     
#     *     
# * * * * * 

# 10 for J

for i in range(n):
    for j in range(n):
        if j==m or i==0 or (i==n-1 and j<=m) or (j==0 and i>m):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# Output:
# Enter the size: 5
# * * * * * 
#     *     
#     *     
# *   *     
# * * *     

# 11. for K

for i in range(n):
    for j in range(n):
        if (i==m and j<m) or j==0 or (i==j and i>=m) or (j+i == (n-1) and j>=m):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# output:
# Enter the size: 5
# *       * 
# *     *   
# * * *     
# *     *   
# *       * 

# 12. for L
for i in range(n):
    for j in range(n):
        if i==n-1 or j==0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# output:
# Enter the size: 5
# *         
# *         
# *         
# *         
# * * * * * 

# 13. for M

for i in range(n):
    for j in range(n):
        if (i==j and j<=m) or j==0 or j==n-1 or (i+j == (n-1) and j>m):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# output:
# Enter the size: 5
# *       * 
# * *   * * 
# *   *   * 
# *       * 
# *       * 

# 14. for N

for i in range(n):
    for j in range(n):
        if (i==j) or j==0 or j==n-1 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# output:
# Enter the size: 5
# *       * 
# * *     * 
# *   *   * 
# *     * * 
# *       * 

# 15. for O
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# Output:
# Enter the size: 5
# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * *

# 16 for P

for i in range(n):
    for j in range(n):
        if i==0 or j==0 or (j==n-1 and i<=m) or i==m:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# Output:
# Enter the size: 5
# * * * * * 
# *       * 
# * * * * * 
# *         
# *         

# 17. for Q

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or (i==j and i >2 ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# Output:
# Enter the size: 7
# * * * * * * *
# *           *
# *           *
# *     *     *
# *       *   *
# *         * *
# * * * * * * * 

# 18. for R

for i in range(n):
    for j in range(n):
        if i==0 or j==0 or (j==n-1 and i<=m) or i==m or (i==j and j>=m):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# Output:
# Enter the size: 5
# * * * * * 
# *       * 
# * * * * * 
# *     *   
# *       * 

# 19. for s

for i in range(n):
    for j in range(n):
        if i==0 or (j==0 and i<m) or (j==n-1 and i>m) or i==m or i==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# Output:
# Enter the size: 5
# * * * * * 
# *         
# * * * * * 
#         * 
# * * * * * 

# 20. for T

for i in range(n):
    for j in range(n):
        if j==m or i==0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# Output:
# Enter the size: 5
# * * * * * 
#     *     
#     *     
#     *     
#     *     

# 21. for U
for i in range(n):
    for j in range(n):
        if i==n-1 or j==0 or j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# Output:
# Enter the size: 5
# *       * 
# *       * 
# *       * 
# *       * 
# * * * * * 

# 22. for v
for i in range(n):
    for j in range(n):
        if (j==0 and i<=m) or (j==n-1 and i<=m)or (i > m and j == i-m) or (i > m and j == (n-1)-(i-m)):
            print("*", end=" ")    
        else:
            print(" ", end=" ")
    print()
print()
# Output:
# Enter the size: 5
# *       * 
# *       * 
# *       * 
#   *   *     
#     *    

# Enter the size: 6
# *         * 
# *         * 
# *         * 
# *         * 
#   *     *   
#     * *     

# 23. for W

for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and j>=m) or (i+j == n-1 and j<=m):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# Output:
# Enter the size: 5
# *       * 
# *       * 
# *   *   * 
# * *   * * 
# *       * 

# 24. for X

for i in range(n):
    for j in range(n):
        if (i==j) or (i+j == n-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
# Output:
# Enter the size: 5
# *       * 
#   *   *   
#     *     
#   *   *   
# *       * 

# 25. for Y

for i in range(n):
    for j in range(n):
        if (i==j and j<=m) or (i+j == n-1 and j>=m) or (j==m and i>=m):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()

# Output:
# Enter the size: 5
# *       * 
#   *   *   
#     *     
#     *     
#     *     

# 26. for Z

for i in range(n):
    for j in range(n):
        if i==0 or (i+j == n-1) or i==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Output:
# Enter the size: 5
# * * * * * 
#       *   
#     *     
#   *       
# * * * * * 
'''

alphabets = {
    'A': lambda i, j: (i == 0 or i == m or j == 0 or j == n - 1),

    'B': lambda i, j: (i == 0 or i == n - 1 or i == m or j == 0 or j == n - 1),

    'C': lambda i, j: (i == 0 or i == n - 1 or j == 0),

    'D': lambda i, j: (i == 0 or i == n - 1 or j == 0 or j == n - 1),

    'E': lambda i, j: (i == 0 or i == n - 1 or i == m or j == 0),

    'F': lambda i, j: (i == 0 or i == m or j == 0),

    'G': lambda i, j: (
        i == 0 or
        (i == m and j > m) or
        (i == n - 1 and j <= m) or
        (j == m and i >= m) or
        (j == n - 1 and i >= m) or
        j == 0
    ),

    'H': lambda i, j: (i == m or j == 0 or j == n - 1),

    'I': lambda i, j: (j == m or i == 0 or i == n - 1),

    'J': lambda i, j: (
        j == m or
        i == 0 or
        (i == n - 1 and j <= m) or
        (j == 0 and i > m)
    ),

    'K': lambda i, j: (
        (i == m and j < m) or
        j == 0 or
        (i == j and i >= m) or
        (i + j == n - 1 and j >= m)
    ),

    'L': lambda i, j: (i == n - 1 or j == 0),

    'M': lambda i, j: (
        (i == j and j <= m) or
        j == 0 or
        j == n - 1 or
        (i + j == n - 1 and j > m)
    ),

    'N': lambda i, j: (i == j or j == 0 or j == n - 1),

    'O': lambda i, j: (i == 0 or i == n - 1 or j == 0 or j == n - 1),

    'P': lambda i, j: (
        i == 0 or
        j == 0 or
        (j == n - 1 and i <= m) or
        i == m
    ),

    'Q': lambda i, j: (
        i == 0 or
        i == n - 1 or
        j == 0 or
        j == n - 1 or
        (i == j and i > 2)
    ),

    'R': lambda i, j: (
        i == 0 or
        j == 0 or
        (j == n - 1 and i <= m) or
        i == m or
        (i == j and j >= m)
    ),

    'S': lambda i, j: (
        i == 0 or
        (j == 0 and i < m) or
        (j == n - 1 and i > m) or
        i == m or
        i == n - 1
    ),

    'T': lambda i, j: (j == m or i == 0),

    'U': lambda i, j: (i == n - 1 or j == 0 or j == n - 1),

    'V': lambda i, j: (
        (j == 0 and i <= m) or
        (j == n - 1 and i <= m) or
        (i > m and j == i - m) or
        (i > m and j == (n - 1) - (i - m))
    ),

    'W': lambda i, j: (
        j == 0 or
        j == n - 1 or
        (i == j and j >= m) or
        (i + j == n - 1 and j <= m)
    ),

    'X': lambda i, j: (i == j or i + j == n - 1),

    'Y': lambda i, j: (
        (i == j and j <= m) or
        (i + j == n - 1 and j >= m) or
        (j == m and i >= m)
    ),

    'Z': lambda i, j: (i == 0 or i + j == n - 1 or i == n - 1)
}


# for i in range(n):
#     for j in range(n):
#         print('*' if alphabets[alpha](i, j) else ' ', end=' ')  List comparsion
#     print()


for i in range(n):
    for a in list_alpha:
        for j in range(n):
            if alphabets[a](i, j):
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print('  ',end='') 
    print() 

# Output:
# Enter a alphabets: ak
# ['A', 'K']
# Enter the size of the alphabets: 7
# * * * * * * *   * * * * * * *   * * * * * * *   *           *   
# *           *         *         *           *     *       *     
# *           *         *         *           *       *   *       
# * * * * * * *         *         * * * * * * *         *         
# *           *   *     *         *           *         *         
# *           *   *     *         *           *         *         
# *           *   * * * *         *           *         *   