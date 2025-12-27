n=int(input("enter a number:"))
total=0
for i in range(1,n+1):
    total=total+i

print(total)

name=input("enter your name:")
age=int(input("enter your age:"))
height=float(input("enter your height:"))
print(f"Hello {name}! You are {age} years old and {height} feet tall.")

print(type(name))
print(type(age))
print(type(height))

age=int(input("enter ur age:"))
print(f"After birthday,you are {age} years old!")
