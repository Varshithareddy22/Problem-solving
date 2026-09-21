#even 
arr=[2,7,8,5,16,9,10]
count=0
for num in arr:
    if num%2==0:
        count+=1
        print(num)        
print("Total count is", count)

#odd
arr=[2,7,8,5,16,9,10]
count=0
for num in arr:
    if num%2!=0:
        count+=1
        print(num)        
print("Total count is" ,count)
