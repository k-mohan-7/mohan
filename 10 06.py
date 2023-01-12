n=0
l=[]
c=0
d=0
e=0
f=0
while n!=-1:
    n=int(input('enter the number'))
    l.append(n)
b=len(l)
for i in l:
    if i>0:
        c=c+i
        e=e+1
    if i<0:
        d=d+i
        f=f+1
print('the average of positive num is' ,c/e)
print('the average of negitive num is' ,d/f)

        
