n=int(input('enter the value'))
su=0
while (su>=1):
    d=n%10
    su=su+d**2
    n=n//10
print(su)
if su==1:
    print('true')
else:
    print('false')
