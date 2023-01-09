n=int(input('enter the digits'))
l1=[ ]
odd=[ ]
even=[ ]
for i in range(n) :
 n1=int(input('enter the  number'))
 l1.append(n1)
for j in(l1):
    if j%2==0:
       even.append(j)
    else:
        odd.append(j)
l2=[ ]
odd1=0
even1=0
for i in odd:
     odd1=odd1+i**2
l2.append(odd1)
for j in even:
    even1 =even1+j**2
l2.append(even1)
print(l2)


