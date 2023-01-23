n=int(input('enter the number'))
l=[]
for i in range(n):
    n1=input('sentence')
    l.append(n1)
i=input('a for assending d for desending')
if i=='a':
    sorted(l)
    print(' '.join(l),end=' ')
elif i=='d':
    sorted(l,reverse=True)
    print(' '.join(l),end=' ')
print()
