num=int(input("Enter the number of elements to be in the list:"))
l=[]
for i in range(num):
    n1=int(input("Enter the element:"))
    l.append(n1)
m=int(input('enter max number'))
n=int(input('entee the minimum number you need'))
maxm=sorted(l)
minm=sorted(l,reverse=True)
m1=maxm[m-1]
n1=minm[n-1]
print('sum of numbers is ;',m1+n1)
print('difference of number is ;',m1-n1)
print(m1,'max number')
print(n1,'minimum number')
