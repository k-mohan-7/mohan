n=int(input('enter the digit'))
l=[]
for i in range(n):
    a=int(input('enter the numbers'))
    l.append(a)
b=sorted(l)
b.insert(3,100)
print(b)
  
