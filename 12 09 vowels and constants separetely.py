n= input('enter the string')
v=['a','e','i','o','u','a','E','I','O','U']
v1=[]
c=[]
for i in n:
    if i in v:
        v1.append(i)
for j in n:
    if j not in v:
        c.append(j)
print(' '.join(v1))
print(' '.join(c))
