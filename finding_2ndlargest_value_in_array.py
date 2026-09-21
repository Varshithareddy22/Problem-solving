arr=[10,5,18,23,9]
largest=arr[0]
second_largest=arr[1]
for num in arr:
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest and num!=largest:
        second_largest=num
print(f"The largest number is {largest} and The second largest number is {second_largest}")