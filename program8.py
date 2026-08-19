#print 1 to 10

for i in range (1,11):
    print(i)

#print 10 to 1
for i in range (10,0,-1):
    print(i)

#print even numbers 2 to 20
for i in range (2,21,+2):
    print(i)

#print odd numbers 1 to 19
for i in range(1,20,+2):
    print(i)

#print *****
i = 1
while i<=5:
    print("*")
    i=i+1

# pattern
i = 5
while i >= 1:
    j = 1
    while j <= i:
        print("*", end="")
        j = j + 1
    print()
    i = i - 1
