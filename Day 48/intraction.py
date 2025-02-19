from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_option)
driver.get(url='https://en.m.wikipedia.org/wiki/Main_Page')

# wiki = driver.find_elements(By.CSS_SELECTOR, value='#articlecount a')
# print(wiki[1].text)

# Click

# Find element by link name

#Content portals



driver.close()