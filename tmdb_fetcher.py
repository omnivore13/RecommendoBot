from credentials import key #API Key for The Movie Database
#https://www.themoviedb.org/documentation/api
import json
import requests
import re
from unidecode import unidecode
from bs4 import BeautifulSoup

def search(query, key = key):
    URL = "https://api.themoviedb.org/3/search/company?api_key=" + key + "&query=" + query + "&page=1"

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
