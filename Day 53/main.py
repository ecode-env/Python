import requests
from bs4 import BeautifulSoup


response = requests.get(url='https://appbrewery.github.io/Zillow-Clone/').text

soup = BeautifulSoup(response, "html.parser")

#STEP 1

list_of_links = [ link.get('href') for link in soup.find_all(name='a', class_='property-card-link') ]

#STEP 2

list_of_prices = [price.text.split('+')[0].split('/')[0]
                  for price in soup.find_all(name='span', class_='PropertyCardWrapper__StyledPriceLine')]

