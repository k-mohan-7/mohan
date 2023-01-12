def shippingcost(n):
    sum1=750
    for i in range(n):
        sum1=sum1+200
    return sum1
n1=int(input("Enter the number of items:"))
print(shippingcost(n1))
