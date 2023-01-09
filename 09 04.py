a=input('enter the digit ')
l=[ ]
for i in a:
    l.append(i)
if (l)==(l[::-1]):
 print('it is palindrome')
else:
    print('it is not p')
