n=int(input("enter n value:"))
l=[]
vowel=["a","e","i","o","u"]
for i in vowel:
    for j in vowel:
        a=i+j
        l.append(a)
for x in range(0,n-1):
    for i in l:
        if ord(i[x])>ord(i[x+1]):
            l.remove(i)
print(l)
print(len(l))
