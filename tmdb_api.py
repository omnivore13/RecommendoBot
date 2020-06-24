from credentials import key #API Key for The Movie Database
#https://www.themoviedb.org/documentation/api
import json
import pickle
import requests
from bs4 import BeautifulSoup
import re
from unidecode import unidecode
from datetime import *
import numpy as np

def search(query, key = key):
    URL = "https://api.themoviedb.org/3/search/movie?api_key="+ key + "&language=en-US&query=" + query + "&page=1&include_adult=true"
    html = requests.get(URL)
    if html.status_code == 200:
        result = html.json()['results'][0]
        id = result['id']
        return search_id(id)

def user_search(query, key = key):
    URL = "https://api.themoviedb.org/3/search/movie?api_key="+ key + "&language=en-US&query=" + query + "&page=1&include_adult=true"
    html = requests.get(URL)
    if html.status_code == 200:
        out = html.json()
        if out['total_results'] == 1:
            result = html.json()['results'][0]
            id = result['id']
            return search_id(id)
        else:
            print("Did you mean: ")
            for idx, movie in enumerate(out['results']):
                print(str(idx) + " " + movie['title'])
            choice = int(input("Your choice? "))
            movie_id = out['results'][choice]['id']
            return search_id(movie_id)
    else:
        return "Please check query. Movie not found"
        
def search_id(id, key = key):
    data = {}
    URL = "https://api.themoviedb.org/3/movie/" + str(id) + "?api_key="+ key + "&language=en-US"
    html = requests.get(URL)
    if html.status_code == 200:
        movie_data = html.json()
        data['title'] = movie_data['title']
        try:
            data['release'] = datetime.strptime(movie_data['release_date'], '%Y-%m-%d').year
        except:
            data['release'] = np.nan
        data['popularity'] = movie_data['popularity']
        data['budget'] = movie_data['budget']
        data['genres'] = [genre['name'] for genre in movie_data['genres']]
        data['overview'] = movie_data['overview']
        data['language'] = movie_data['original_language']
    return data

fp = open('movies.pickle', 'rb')
movies = pickle.load(fp)
fp.close()



all_movies = {}
for movie in movies:
    all_movies[movie] =  search(movie)


fp = open('all_movies.json', "w")
json.dump(all_movies, fp)
fp.close()