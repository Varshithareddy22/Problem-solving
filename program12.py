# finding vowel and constants using conditional statement
x=(input("Enter the letter:"))
x=x.lower()            
if x in "aeiou":
    print(x,"is a vowel")
else:  
    print(x,"is a constant")

