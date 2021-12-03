# test to print movies.json data
import json

filename = 'movies.json'
try:
    my_movies = json.load(open(filename))
except Exception as e:
    print("Could not read {}".format(filename))
    print(e)
    exit(1)

for m in my_movies:
  print("here  " + str(m))
  
