#without using flag
'''
arr=[10,5,18,23,9]
target=18
for num in arr:
    if num==target:
        print("found",num)
'''
#with flag
arr=[10,5,18,23,9]
target=18
found=False
for num in arr:
    if num==target:
        found=True
        break
if found:
        print(num,"found")
else:
        print("not found")    