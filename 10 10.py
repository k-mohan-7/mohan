yr=int(input("Enter the year to check:"))
if yr%400==0 or yr%4==0:
    print("It is leap year")
else:
    print("Not a leap year")
