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
from tqdm import tqdm

def search(query, key = key):
    URL = "https://api.themoviedb.org/3/search/movie?api_key="+ key + "&language=en-US&query=" + query + "&page=1&include_adult=true"
    html = requests.get(URL)
    if html.status_code == 200:
        out = html.json()
        if out['total_results'] == 0:
            pass
        else:
            result = out['results'][0]
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
    details_URL = "https://api.themoviedb.org/3/movie/" + str(id) + "?api_key="+ key + "&language=en-US"
    credits_url = "https://api.themoviedb.org/3/movie/" + str(id) + "/credits?api_key=" + key
    html = requests.get(details_URL)
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
        data['overview'] = unidecode(movie_data['overview'])
        data['language'] = movie_data['original_language']
        data['votes'] = movie_data['vote_count']
        data['status'] = movie_data['status']
    html = requests.get(credits_url)
    if html.status_code == 200:
        credits = html.json()
        try:
            data['cast'] = [cast['name'] for cast in credits['cast']][:3]
        except:
            data['cast'] = None
        try:
            director = [crew['name'] for crew in credits['crew'] if crew['job'] == 'Director']
            data['director'] = director[0]
        except:
            data['director'] = None
        try:
            producer = [crew['name'] for crew in credits['crew'] if crew['job'] == 'Producer']
            data['producer'] = producer[0]
        except:
            data['producer'] = None
        
    return data

# fp = open('movies.pickle', 'rb')
# movies = pickle.load(fp)
# fp.close()

# all_movies = {}
# for movie in tqdm(movies):
#     all_movies[movie] =  search(movie)


# fp = open('all_movies.json', "w")
# json.dump(all_movies, fp)
# fp.close()

new_movies = {}
new_titles = []
fp = open('movies.txt', 'r')
for i in fp:
    new_titles.append(i.strip())
fp.close()


for movie in tqdm(new_titles[:3000]):
    new_movies[movie] = search(movie)
fp = open('movies_3k.json', 'w')
json.dump(new_movies, fp)
fp.close()
for movie in tqdm(new_titles[3000:6000]):
    new_movies[movie] = search(movie)
fp = open('movies_6k.json', 'w')
json.dump(new_movies, fp)
fp.close()

for movie in tqdm(new_titles[6000:]):
    new_movies[movie] = search(movie)
fp = open('movies_9k.json', 'w')
json.dump(new_movies, fp)
fp.close()