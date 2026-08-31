# reverse a number
x= int(input("enter the number:"))
reverse = 0
while x!=0:
    a=x%10
    reverse=reverse*10+a
    x=x//10
print(reverse)
 

# palindrome 
x= int(input("enter the number:"))
original=x
reverse = 0
while x!=0:
    a=x%10
    reverse=reverse*10+a
    x=x//10
if (original==reverse):
    print(reverse,"is palindrome")
else:
    print(reverse,"is not palindrome")


# factorial
x= int(input("Enter the number"))
factorial=1
i=1
while i<=x:
    factorial=factorial*i
    i=i+1
print("factorial of ",x,"is",factorial)

# break statement
for i in range(1,50,2):
    if i ==25:
        break
    print(i)

# continue statement
for i in range(1,50):
    if i ==25:
        continue
    print(i)

# print list using for loop
l1 =(1,2,"manas","varshitha","rohit","virat","rohit",8,9)
for item in l1:
    print(item)
