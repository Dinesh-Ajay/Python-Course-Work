# def dis(s,indx):
#     if indx==len(s):
#         return
#     print(s[:indx+1])
#     dis(s,indx+1)

# dis('Python',0)

# def dis(s,indx,x):
#     if indx==len(s):
#         return
#     print(s[x:indx])
#     dis(s,indx+1,x+1)

# dis('Pythonfytfiu',2,0)

# def dis(s,indx,x):
#     if indx==len(s)-x+1:
#         return
#     print(s[indx:indx+x])
#     dis(s,indx+1,x)

# dis('Pythonfytfiu',0,2)

# def dis(l, indx):
#     if indx == len(l):
#         return 0
    
#     return l[indx]+dis(l,indx+1)

# l=[1,2,3,4,5,6,7,8]
# print(dis(l,0))

def dis(l, indx):
    if indx == len(l):
        return 0
    if l[indx] in "aeiouAEIOU":
        return 1+dis(l,indx+1)
    else:
        return dis(l,indx+1)

l="pythonarilwtrhoreu"
print(dis(l,0))

