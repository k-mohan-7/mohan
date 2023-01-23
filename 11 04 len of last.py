n=int(input('enter the digit'))
l=[]
for i in range(n):
    a=input('enter the sentences ')
    l.append(a)
s=0
for i in l:
    a=i.split()
    if s<len(a):
        s=len(a)
print(s)
