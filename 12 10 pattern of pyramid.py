n=int(input('enter the number'))
for i in range (1,n):
    for j in range(n-i,0,-1):
        print(' ',end=' ')
    for j in range(0,i):
        print(i,end=' ')
    for j in range(0,i):
        print(i,end=' ')
    print()
