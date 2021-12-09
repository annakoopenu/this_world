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
    print_line = str('\n -- ') + str(n_movies) + str('-- ' )
    n_movies = n_movies - 1
    print_line = print_line + str(each_movie['name']) + str('(') + str(each_movie['year']) + str(') ') 
    each_movie.pop('name')
    each_movie.pop('year')
    print(print_line)
    print(each_movie)
    for key, value in each_movie.items():
        print_line = print_line + str(key) + str(': ') + str(value)

    print(print_line)
