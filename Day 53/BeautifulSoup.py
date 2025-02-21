import requests
from bs4 import BeautifulSoup

class ListOFHouse:
    def __init__(self):
        self.response = requests.get(url='https://appbrewery.github.io/Zillow-Clone/').text
        self.soup = BeautifulSoup(self.response, "html.parser")
        self.links = [ link.get('href') for link in self.soup.find_all(name='a', class_='property-card-link') ]
        self.addresses = [ address.text.strip().replace('|', '').strip()
                           for address  in self.soup.find_all(name='address') ]
        self.prices = [price.text.split('+')[0].split('/')[0]
                  for price in self.soup.find_all(name='span', class_='PropertyCardWrapper__StyledPriceLine')]

    def get_links(self):
        return self.links
    def get_prices(self):
        return self.prices
    def get_addresses(self):
        return self.addresses