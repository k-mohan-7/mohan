c={2:["a","b","c"],3:["d","e","f"],4:["g","h","i"],5:["j","k","l"],6:["m","n","o"],7:["p","q","r","s"],8:["t","u","v"],9:["w","x","y","z"]}
n=input("enter n value:")
l=[]
if n=="":
    print(l)
else:
    n1=int(n)
    digit2=n1%10
    n2=n1//10
    digit1=n2%10
    for i in c[digit1]:
        for j in c[digit2]:
            l.append(i+j)
print(l)
