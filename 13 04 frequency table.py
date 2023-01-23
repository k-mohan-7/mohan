n=int(input("Enter the number of elements in list1:"))
l1=[]
for i in range(n):
    n1=int(input("Enter the element:"))
    l1.append(n1)
count=0
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print("Element | Frequency")
print("--------------------")
for i in l2:
    print(i," "*4,"|",l1.count(i))
