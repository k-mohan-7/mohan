def matches(n,m):
    count=0
    l1=[]
    l2=[]
    for i in n:
        l1.append(i)
    for j in m:
        l2.append(j)
    length=len(n)
    if length>len(m):
        length=len(m)
    for i in range(length):
        if l1[i]==l2[i]:
            count+=1
    return count
n1=input("Enter the string:")
m1=input("Enter the string:")
print(matches(n1,m1))  
    
