x=5
y=8
print(x>y)

# 1️⃣ What is a for loop?

#A for loop is used to repeat a block of code a fixed number of times.


#Q1️⃣

#Print numbers from 1 to 5 using for loop.

for i in range(1,6):
    print(i)


#Q2️⃣

#Print all numbers from 1 to 10 but skip 5

for i in range(1,11):
    if i == 5:
        continue
    print(i)

#3.


arr=[3,6,9]
for x in arr:
    print(x)

#4.Print numbers from 10 to 1 using a for loop.

for i in range(10,0,-1):
    print(i)



#5.Print only even numbers from 1 to 10.

for i in range(0,11,2):
    print(i)


#6.Print numbers from 1 to 10.👉 Stop the loop when number is 7

for i in range(1,11):
    if i == 7:
        break
    print(i)


#7.print only numbers greater than 5:

arr=[2,6,1,9,4,8]
for i in arr:
    if i >5:
        print(i)






    
