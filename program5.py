#1
x= int(input("enter the voter age: "))
if x>=18 :
    print("Eligible to vote")
else:
    print("Not eligible to vote")


#2 finding greatest od three numbers
x= int(input("enter the value of x:"))
y= int(input("enter the value of y:"))
z= int(input("enter the value of z:"))
if (x>y) and (x>z):
    print("x is greater")
elif (y>x) and (y>z):
    print("y is greater") 
else:
    print("z is greater")

#3
x= int(input("enter the value of x:"))
y= int(input("enter the value of y:"))
if (x>0) and (y>0) :
    print(x,y,"numbers are positive")
else :
    print(x,y,"numbers are not positive")    
