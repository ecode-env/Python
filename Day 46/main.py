import requests
from bs4 import BeautifulSoup



user_date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD ')

URL = f'https://www.billboard.com/charts/hot-100/{user_date}'

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url=URL, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')


top_music = [music.getText().strip() for music in soup.select(selector='li ul li h3')]
