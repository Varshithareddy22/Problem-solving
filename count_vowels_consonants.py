#vowels
s="smriti"
count=0
for char in s:
    if char in "aeiou":
        count+=1
        print(char)
print("vowels in s is", count)        

#consonants
s="jemimah"
count=0
for char in s:
    if char not in "aeiou":
        count+=1
        print(char)
print("cconsonants in s is", count)        
