n=int(input("Enter the number of elements:"))
l=[]
for i in range(n):
    n1=int(input("Enter the number of elements:"))
    l.append(n1)
lst=[]
count=0
for i in l:
    count=0
    for j in l:
        if j<i:
            count+=1            
    lst.append(count)
print(l)
print('count of list',lst)
