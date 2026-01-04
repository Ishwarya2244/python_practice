a=int(input("enter a:"))
b=int(input("enter b:"))
print(a+b)
print(a-b)
print(a*b)


x="10"
y=5
print(x*y)


a=input("enter a:")
b=input("enter b:")
print(a+b)

print(bool(0)) #false
print(bool("0")) #true
print(bool(""))#false
print(bool(" "))#true
print(bool("false"))#true
print(bool("1"))#true

a=int(input("enter a :"))
b=int(input("enter b:"))
c=int(input("enter c:"))
if a>=b and a>=c:
    print("Largest number:",a)
elif b>=a and b>=c:
    print("largest number:",b)
else:
    print("largest number:",c)
