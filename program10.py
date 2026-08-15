#reverse numbers
x= int(input("enter the number:"))
reverse = 0
while x!=0:
    a=x%10
    reverse=reverse*10+a
    x=x//10
print(reverse)


#palindrome number
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

