s=input('enter the string')
t=input('enter the string')
if(len(s) != len(t)):
    print('it is not isomorphic')
else:
    c={}
for i in range (len(s)):
    e=s[i]
    f=t[i]
    if(e not in c):
        c[e]=f
        print('it is isomorphic')
    else:
        if e in c:
            if c[e]!=f:
                print('not isomorphic')
                break
            else:
                print("isomorphic")
                break
    
