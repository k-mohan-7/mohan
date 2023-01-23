n1=int(input("Enter number1:"))
n2=int(input("Enter number1:"))
grt=0
if n1>n2:
    grt=n1
elif n2>n1:
    grt=n2
l=[]
for i in range(1,grt+1):
    if (n1%i==0) and (n2%i==0):
        l.append(i)
    else:
        continue
print(len(l))
