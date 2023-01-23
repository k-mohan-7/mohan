age=int(input("Enter your age:"))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible")
    print("You are allowed to vote after",18-age,"years")
