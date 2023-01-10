n=int(input('enter no of digits'))
l=[]
sum=0
for i in range(n):
    n1=int(input('enter the value'))
    l.append(n1)
for i in l:
    sum=sum+i**2
print('the sum of square is',sum)
    
