def intrest(p,t,s):
    if s=='y':
        r=12
        intr=((p*t*r)/100)
        return(intr)
    elif s=='n':
        r=10
        intr=((p*t*r)/100)
        return(intr)

    
p=int(input('enter the principal amount'))
t=int(input('enter the time'))
s=input('enter y if senior citizen n if no')
print(intrest(p,t,s))    
