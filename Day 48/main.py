from selenium import webdriver
from selenium.webdriver.common.by import By

# keep chrome browser open after program finish
chrom_option = webdriver.ChromeOptions()
chrom_option.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrom_option)
driver.get(url='https://www.python.org/')

#amazon = 'https://www.amazon.com/Apple-MacBook-Laptop-10%E2%80%91core-16%E2%80%91core/dp/B0BSHDT7F5/ref=sr_1_3?crid=2FS45T2YPJ96S&dib=eyJ2IjoiMSJ9.FlNeYUBHREaWx49hRy3_PPjEpyAP7FfFf5z9Z0nWTRB7zJGQV5pbm0lC5scUKxehCMBPUBz4OooP2gpzN8b3O123Tu2f-rKzG4tYAs5xx-nVEEUFL-Mym39zSydFzUTzWwQLEo4bUXFxy5iexkWMQogPa-QAyhgbmruq6M8d-VZkPh1XWgN1HMDFwqOmzGEzbsJlfBhlrqUHRaCU-X01q8aMLYsyLL7Z2qp1gx7T7e0.crGRqwWXr2ZvvGZa5h7Kh2kTTRPg-6gSieDm3TKIWcg&dib_tag=se&keywords=macbook%2Bpro%2B14-inch%2B(m2%2Bpro)&qid=1739704214&refinements=p_n_size_browse-bin%3A2423840011&rnid=2242797011&sprefix=macbook%2Bpro%2B14-inch%2Bm2%2Bpro%2B%2Caps%2C244&sr=8-3&th=1'

# select using tag ID and we can class
#prise_dollar = driver.find_element(By.CLASS_NAME, value='here class name')

#prise_dollar = driver.find_element(By.ID, value='_price')

#To find witch css selector
#prise_dollar = driver.find_element(By.CSS_SELECTOR, value='here name')

# we can get more information

# we use prise_dollar.get_attribute('ex. placeholder')
#print(prise_dollar.text)

# get with XPATH

# xpath = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[1]/div[1]/h2')
# print(xpath.text)

##  First Task for  selenium

event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
event_name = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')

events = {n: {"name": name.text, "time": time.text} for n, (name, time) in enumerate(zip(event_name, event_times))}


print(events)
driver.close()