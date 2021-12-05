# test to print movies.json data
import json

filename = 'movies.json'

try:
    my_movies = json.load(open(filename))
except Exception as e:
    print("Could not read {}".format(filename))
    print(e)
    exit(1)

n_movies = (len(my_movies))

for each_movie in my_movies:
    print('\n --- Movie --- ' + str(n_movies) )
    n_movies = n_movies - 1
    for key, value in each_movie.items():
        print(str(key) + ': ' + str(value))

