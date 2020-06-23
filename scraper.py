import json
import requests
from bs4 import BeautifulSoup
import time
import lxml
import os
import json

def url(year):
    page = "https://www.rottentomatoes.com/top/bestofrt/?year=" + str(year)
    return page


movies = {}
for year in range(1950,1980):
    movie_list = []
    html = requests.get(url(year)).text
    soup = BeautifulSoup(html, "lxml")
    table = soup.find('table', attrs={'class' : 'table'})
    names = table.findAll('a', attrs = {'class' : 'unstyled articleLink'})
    for name in names:
        m_name = name.text[2:]
        m_name = m_name.strip()
        movie_list.append(m_name)
    movies[year] = movie_list
    print(str(year) + " done")
    
with open("50_to_80.json", "w") as f:
    json.dump(movies, f)
print("Saved")


movies = {}
for year in range(1980,2000):
    movie_list = []
    html = requests.get(url(year)).text
    soup = BeautifulSoup(html, "lxml")
    table = soup.find('table', attrs={'class' : 'table'})
    names = table.findAll('a', attrs = {'class' : 'unstyled articleLink'})
    for name in names:
        m_name = name.text[2:]
        m_name = m_name.strip()
        movie_list.append(m_name)
    movies[year] = movie_list
    print(str(year) + " done")

with open("80_to_00.json", "w") as f:
    json.dump(movies, f)
print("Saved")


movies = {}
for year in range(2000,2021):
    movie_list = []
    html = requests.get(url(year)).text
    soup = BeautifulSoup(html, "lxml")
    table = soup.find('table', attrs={'class' : 'table'})
    names = table.findAll('a', attrs = {'class' : 'unstyled articleLink'})
    for name in names:
        m_name = name.text[2:]
        m_name = m_name.strip()
        movie_list.append(m_name)
    movies[year] = movie_list
    print(str(year) + " done")


with open("00_to_20.json", "w") as f:
    json.dump(movies, f)
print("Saved")