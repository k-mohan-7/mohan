def gcd1(a,b):
    a1=[]
    b1=[]
    gcd=[]
    if a>b:
        g=a
    else:
        g=b
    for i in range(1,a+1):
        if a%i==0:
            a1.append(i)
    for i in range(1,a+1):
        if b%i==0:
            b1.append(i)
    for i in range(1,g+1):
        if i in a1 and i in b1:
            gcd.append(i)
    gcd.sort()
    return(max(gcd))
def lcm(a,b):
    lcm=(a*b)//gcd1(a,b)
    return lcm
    
n1=int(input("Enter a "))
n2=int(input("Enter b"))
print("gcd:",gcd1(n1,n2))
print("lcm:",lcm(n1,n2))
