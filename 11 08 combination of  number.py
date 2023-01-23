a=int(input('enter number'))
b=len(a)
for i in range(b):
    for j in range(b):
        for k in range(b):
            if (i!=j and j!=k and i!=k):
                print(a[i],a[j],a[k])
