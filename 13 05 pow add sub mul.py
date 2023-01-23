def pow1(x,n):
    print(x**n)
def add(x,n):
    print(x+n)
def sub(x,n):
    print(x-n)
def mul(x,n):
    print(x*n)
def div(x,n):
    print(x//n)
X=int(input("X="))
N=int(input("N="))
choice=int(input("Enter 1-pow,2-add,3-sub,4-mul,5-div"))
if choice==1:
    pow1(X,N)
elif choice==2:
    add(X,N)
elif choice==3:
    sub(X,N)
elif choice==4:
    mul(X,N)
elif choice==5:
    div(X,N)
