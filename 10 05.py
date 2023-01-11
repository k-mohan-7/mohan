n=0
l=[]
lower=0
upper=0
digi=0
while n!="*":
    n=input("Enter any character:")
    l.append(n)
for i in l:
  if i.isupper()==True:
    upper+=1
  elif i.islower()==True:
    lower+=1
  elif i.isdigit()==True:
    digi+=1  
print(lower)
print(upper)
print(digi)
