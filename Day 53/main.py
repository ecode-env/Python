from BeautifulSoup import ListOFHouse
from Selenium import FillOut

house = ListOFHouse()
fillOut = FillOut()

address = house.get_addresses()
prices = house.get_prices()
links =  house.get_links()

fillOut.fill_out_a_form(address, prices, links)
