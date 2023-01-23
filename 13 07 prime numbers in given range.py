n1=int(input('enter the starting value'))
n2=int(input('enter the ending value'))
for i in range (n1,n2+1):
    c=0
    for j in range(2,n2+1):
        if i%j==0:
            c=c+1
    if c==1:
        print(i)
