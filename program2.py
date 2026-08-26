# swapping a variable with temp variable 
x=1
y=2
temp=x
x=y
y=temp
print(x,y)

#swap without temp variable
x=1
y=2
x=x+y
print(x,y)
y=x-y
print(x,y)
x=x-y
print(x,y)
