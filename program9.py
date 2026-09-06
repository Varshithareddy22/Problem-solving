#sum of first n numbers
x= int(input("enter the number"))
sum=0
i=1
while i<=x:
    sum=sum+i 
    i=i+1
print(sum)

#multiplication table
x= int(input("enter the table:"))
i=1
while i<=10:
    print(x*i)
    i=i+1 

#multiplication table using for loop
x=int(input("enter the number:"))
for i in range (1,11,+1):
    print(x*i)
    i=i+1

#count digits
x= int(input("enter the number:"))
i=0
while x>0:
    x=x//10
    i=i+1
print(i)

#sum of digits
x= int(input("enter the number:"))
i=0
while x>0:
    a=x%10
    i=a+i
    x=x//10
print(i)
