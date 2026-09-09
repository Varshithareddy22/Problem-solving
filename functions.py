#function1
def greet():
    print("Hello Varshitha")
greet()
greet()

#function2
def greet(name):
    print("Hello",name)
greet("Varshitha")
greet("Smriti")
greet("Jemi")    

#function with multiple inputs
def add(a,b):
    print(a+b)
add(2,3)
add(5,18)    

#return function
def add(a,b):
    return a+b
result1 = add(5,18)
result2 = add(18,23)
print(result1)
print(result2)
