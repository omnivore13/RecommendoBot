import json
import requests
import re
from unidecode import unidecode
from bs4 import BeautifulSoup
import pickle


def filter_func(string):
    string = re.sub(r' \(\d\d\d\d\)', '', string)
    string = re.sub(r' \(\D+\)', '', string)
    return string

dict_1 = json.load(open('50_to_80.json'))
dict_2 = json.load(open('80_to_00.json'))
dict_3 = json.load(open('00_to_20.json'))
movies = list(dict_1.values()) + list(dict_2.values())+ list(dict_3.values())
movie_titles = []
for movie_list in movies:
    movie_titles.extend(movie_list)
movie_titles = list(map(filter_func, movie_titles))
movie_titles = list(map(unidecode, movie_titles))

fp = open('movies.pickle', 'wb')
pickle.dump(movie_titles, fp)
fp.close()