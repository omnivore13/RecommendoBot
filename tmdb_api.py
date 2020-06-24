from credentials import key #API Key for The Movie Database
#https://www.themoviedb.org/documentation/api
import json
import pickle
import requests
from bs4 import BeautifulSoup
import re
from unidecode import unidecode



def search(query, key = key):
    URL = "https://api.themoviedb.org/3/search/movie?api_key="+ key + "&language=en-US&query=" + query + "&page=1&include_adult=true"
    html = requests.get(URL)
    if html.status_code == 200:
        result = html.json()['results'][0]
        id = result['id']
        return search_id(id)
        
def search_id(id, key = key):
    data = {}
    URL = "https://api.themoviedb.org/3/movie/" + str(id) + "?api_key="+ key + "&language=en-US"
    html = requests.get(URL)
    if html.status_code == 200:
        movie_data = html.json()
        data['id'] = movie_data['id']
        data['title'] = movie_data['title']
        data['budget'] = movie_data['budget']
        data['genres'] = [genre['name'] for genre in movie_data['genres']]
        data['overview'] = movie_data['overview']
    return data

tokeepoverall = ['budget', 'genres[name]', 'prodcomp[name], runtime. tagline']
to_keep = ['original_title', 'genre_ids', 'overview', 'vote_average', 'year(release_date)', 'id']
fp = open('movies.pickle', 'rb')
movies = pickle.load(fp)
fp.close()

