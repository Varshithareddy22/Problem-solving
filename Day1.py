# movie list manager
 #print list
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

