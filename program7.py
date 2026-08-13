#finding 2nd largest number 
x = int(input("enter the value"))
y = int(input("enter the value"))
z = int(input("enter the value"))

if (x > y and x < z) or (x < y and x > z):
    print("x is the second largest number")
elif (y > x and y < z) or (y < x and y > z):
    print("y is the second largest number")
else:
    print("z is the second largest number")