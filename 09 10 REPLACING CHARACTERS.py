a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
st=input("Enter a string:")
st1=list(st)
c=0
for i in st:
    fre=st.count(i)
    n=(a.index(i)+fre)
    r=a[n]
    st1[c]=r
    c+=1
for i in st1:
    print(i,end="")
