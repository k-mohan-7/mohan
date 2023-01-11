for i in range(1000,10000):
    n=str(i)
    r=len(n)
    t=r//2
    y=(n[:t])
    u=(n[t:r]) 
    y1=int(y) 
    u1=int(u)
    k=(y1+u1)**2
    if k==i:
        print(i)

