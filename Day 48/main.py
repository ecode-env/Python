from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)




driver = webdriver.Chrome()
driver.get(url='https://www.python.org/')

# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
#
# print(f'The price is {price_dollar.text}.{price_cents.text}')


# search_bar = driver.find_element(By.NAME, value='q')
# print(search_bar.get_attribute('placeholder'))
#
# button = driver.find_element(By.ID, value='submit')
# print(button.size)
#
# documentation_link = driver.find_element(By.CLASS_NAME, value='.documentation-widget a')
# print(documentation_link.text)
#
#
# # XPATH
#
# bug_link = driver.find_element(By.XPATH, value='')
# print(bug_link.text)

# Challenge 1

events = {}

# Find the event times and names
event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')

for i in range(len(event_times)):
    events[i] = {
        'name': event_names[i].text,
        'time': event_times[i].text,
    }


print(events)
# driver.close() # close single
driver.quit() # close entire tap