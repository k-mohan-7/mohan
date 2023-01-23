import statistics
n=int(input("Enter the number of elements in list1:"))
l1=[]
for i in range(n):
    n1=int(input("Enter the element:"))
    l1.append(n1)
print("Mean of list is ",statistics.mean(l1))
print("Median of list is ",statistics.median(l1))
print("Mode of list is",statistics.mode(l1))
