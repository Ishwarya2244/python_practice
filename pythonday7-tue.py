#Topic: Conditions (if, else, elif)

age=int(input("Enter your age:"))
if age>=18:
    print("You are eligible to vote")

else:
    print("Your are not eligible to vote")



marks=int(input("Enter marks:"))
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=50:
    print("Grade C")
else:
    print("Fail")



num=int(input("Enter your number:"))
if num>0:
    print("positive")
elif num<0:
    print("Negative")
elif num==0:
    print("Zero")
else:
    print("not valid")
