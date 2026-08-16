#leap year 
'''
x=int(input("Enter the year:"))
if (x%400==0) or (x%100!=0 and x%4==0):
    print(x,"is a leap year")       
else: 
    print(x,"is not a leap year")    
'''

#vowles and constants
x=(input("Enter the letter:"))
x=x.lower()
if x in "aeiou":
    print(x,"is a vowle")
else:
    print(x,"is a constant")    
   