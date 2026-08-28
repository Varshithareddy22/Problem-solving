#finding 2nd largest number 
x = int(input("enter the value:"))
y = int(input("enter the value:"))
z = int(input("enter the value:"))
if (x > y and x < z) or (x < y and x > z):
    print("x is the second largest number")
elif (y > x and y < z) or (y < x and y > z):
    print("y is the second largest number")
else:
    print("z is the second largest number")


#find greatest and 2nd greatest value
x = int(input("enter the value of x:"))
y = int(input("enter the value of y:"))
z = int(input("enter the value of z:"))
if x > y and x > z:
    print("x is greater")
    if y > z:
        print("y is 2nd greatest value")
    else:
        print("z is 2nd greatest value")
elif y > x and y > z:
    print("y is greater")
    if x > z:
        print("x is 2nd greatest value")
    else:
        print("z is 2nd greatest value")
else:
    print("z is greater")
    if x > y:
        print("x is 2nd greatest value")
    else:
        print("y is 2nd greatest value")
