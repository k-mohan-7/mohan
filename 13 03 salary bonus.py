g=input("Enter the grade:")
s=int(input("Enter the salary:"))
print("Salary:",s)
b=0
if s<=10000:
    print('bonus'(0.2)*s)
elif g=="a" or g=="A":
    b=(5/100)*s
    print("Bonus:",b)
elif g=="b" or g=="B":
    b=(10/100)*s
    print("Bonus:",b)
else:
    print("Wrong grade")
print("Total to be paid:",b+s)
