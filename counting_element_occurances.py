#checking how many times a mul element is repeated 
arr=[5,8,5,9,5,9,1]
target1=5
target2=9
count1=0
count2=0
for num in arr:
    if num==target1:
        count1+=1
    if num==target2:
        count2+=1
print("count of 5 is",count1)    
print("count of 9 is",count2)

#checking how many times a 1 element is repeated 
arr=[5,8,5,9,5,1]
target=5
count=0
for num in arr:
    if num==target:
        count+=1
print("count of 5 is",count)    