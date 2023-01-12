import math
n=int(input("Enter a number:"))
l=[]
for i in range(1,n+1):
    root =math.sqrt(i)
    intr = int(root)
    if intr**2==i:
        l.append(i)
    else:
        continue
print(len(l))
