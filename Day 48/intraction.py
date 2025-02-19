from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up Chrome options to keep the browser open after the script ends
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

# Initialize the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_option)
window_handles = driver.window_handles

# Switch to the pop-up window (the last handle in the list is usually the new window)
driver.switch_to.window(window_handles[-1])

# Maximize the pop-up window
driver.maximize_window()

# Navigate to the Wikipedia main page
driver.get(url="https://secure-retreat-92358.herokuapp.com/")

# Example: Find the article count link using CSS_SELECTOR
# wiki = driver.find_elements(By.CSS_SELECTOR, value='#articlecount a')
# print(wiki[1].text)

# Example: Click on a link by its text
# all_portals = driver.find_element(By.LINK_TEXT, value='Content portals')
# all_portals.click()

# Find the search input element by its name attribute
# search = driver.find_element(By.NAME, value="search")
#
# # Type 'Python' into the search box
# search.send_keys('Python')
#
# # Press Enter to perform the search
# search.send_keys(Keys.ENTER)

## CHALLENGE 2

fName = driver.find_element(By.NAME, value='fName')
lName = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')
button = driver.find_element(By.CLASS_NAME, value='btn')
print(fName.text)

fName.send_keys("Eyob", Keys.ENTER)
lName.send_keys("Mulugeta", Keys.ENTER)
email.send_keys("eyobbmulugeta@gmail.com", Keys.ENTER)
button.click()


# Optionally, close the browser after the search
# driver.close()