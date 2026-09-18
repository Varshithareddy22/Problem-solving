#postive numbers
arr=[-5,3,-2,8,0,7,-1]
count=0
for num in arr:
    if num>0:
        count+=1
        print(num,"no. is +ive")
    elif num==0:
        print(num,"is 0")
print(count)

#negative numbers
arr=[-5,3,-2,8,0,7,-1]
count=0
for num in arr:
    if num<0:
        count+=1
        print(num,"no. is -ive")
    elif num==0:
        print(num,"is 0")
print(count)