#divisible by 3 or 7
x= int(input("enter the variable"))
if x%3==0 :
    print(x,"is divisible by 3")
elif x%7==0 :
    print(x,"is divisible by 7")
else:
    print(x,"is not divible 3 or 7")     

#divisible by 5 and 11
x= int(input("enter the variable"))
if x%5==0 and x%11==0:
    print(x,"is divisible by 5 and 11")
else:
    print(x,"is not divible 5 and 11") 

#number lies between 10 and 50
x= int(input("enter the variable"))
if x>=10 and x<=50 :
    print(x,"lies between 10 and 50")
else :    
    print(x,"doesn't lie between 10 and 50")