import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

movies = [movie.getText() for movie in soup.find_all('h3', class_='title')][::-1]

with open('movies.txt', 'w') as file:
    file.write("\n".join(movies))
