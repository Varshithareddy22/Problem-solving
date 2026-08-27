# movie list manager
movies = ["Dear Comrade", "Arjun Reddy", "RRR"]
print(movies)

# print list in sequence
movies = ["Dear Comrade", "Arjun Reddy", "RRR"]
for movie in movies:
    print(movie)

# adding movies
movies = ["Dear Comrade", "Arjun Reddy", "RRR"]
movies.append("Kingdom")
for movie in movies:
    print(movie)

# changing movies
movies = ["Dear Comrade", "Arjun Reddy", "RRR"]
movies[2]="Geetha Govindam"
for movie in movies:
    print(movie)

# removing movie from list
movies = ["Dear Comrade", "Arjun Reddy", "RRR"]
movies.remove("RRR")
for movie in movies:
    print(movie)

# All changes at once
movies = ["Dear Comrade", "Arjun Reddy", "RRR"]
movies.append("Kingdom")
movies.remove("RRR")
movies[2]="Geetha Govindam"
for movie in movies:
    print(movie)

# lists
list = input("Enter 7 fruits names :")
print(list.split(","))
list = [1,5,2,66,9,8,10,100]
list.sort()
list.reverse()
list.insert(5,50)
list.pop(5)
list.append(500)
list.remove(100)
print(list)


# tuples 
tuple =(1,"am",5,7 )
print(tuple)
print(type(tuple))
t=tuple.count("am")
print(t)
print(tuple.count("am"))
fruits =[]
f1 = input("Enter  fruits names :")
fruits.append(f1)
f2 = input("Enter  fruits names :")
fruits.append(f2)
f3 = input("Enter  fruits names :")
fruits.append(f3)
f4 = input("Enter  fruits names :")
fruits.append(f4)
f5 = input("Enter  fruits names :")
fruits.append(f5)
print(fruits)


marks = []
m1 = int(input("Enter marks for student 1: "))
marks.append(m1)
m2 = int(input("Enter marks for student 2: "))
marks.append(m2)
m3 = int(input("Enter marks for student 3: "))
marks.append(m3)
m4 = int(input("Enter marks for student 4: "))
marks.append(m4)
m5 = int(input("Enter marks for student 5: "))
marks.append(m5)
marks.sort()
print(marks)

