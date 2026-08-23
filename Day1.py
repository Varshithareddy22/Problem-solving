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

#changing movies
movies = ["Dear Comrade", "Arjun Reddy", "RRR"]
movies[2]="Geetha Govindam"
for movie in movies:
    print(movie)

#removing movie
movies = ["Dear Comrade", "Arjun Reddy", "RRR"]
movies.remove("RRR")
for movie in movies:
    print(movie)

#All changes at once
movies = ["Dear Comrade", "Arjun Reddy", "RRR"]
movies.append("Kingdom")
movies.remove("RRR")
movies[2]="Geetha Govindam"
for movie in movies:
    print(movie)

    
