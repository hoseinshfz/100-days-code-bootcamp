import requests
from bs4 import BeautifulSoup

OLD_URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=OLD_URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

titles = [movie.getText() for movie in all_movies]

movies = titles[::-1]

with open("old_movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        #print(movie)
        file.write(f"{movie}\n")

"""
With New Website, it is done using parsing the Json output 
"""

import json


NEW_URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=NEW_URL)
web_page = response.content

soup = BeautifulSoup(web_page, "html.parser")

data = json.loads(soup.select_one("#__NEXT_DATA__").contents[0])

movies_list = data['props']['pageProps']['data']['getArticleByFurl']['_layout'][3]['content']['images']
movies = []
titles = []
titles = [item['image']['name'] for item in movies_list]
movies = titles[::-1]

with open("new_movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        #print(movie)
        file.write(f"{movie}\n")

