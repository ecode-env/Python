import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class InstaFollower:
    def __init__(self):
        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_option)

    def login(self, email, password):
        self.driver.get(url='https://www.instagram.com/accounts/login/')
        time.sleep(5)

        #email_input = self.driver.find_element(By.XPATH, '//input[@name="email"]')
        email_input = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        email_input.send_keys(email)
        time.sleep(1)

        #password_input = self.driver.find_element(By.XPATH, '//input[@type="password"]')
        password_input = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        password_input.send_keys(password)
        time.sleep(1)

        #sign_in = self.driver.find_element(By.XPATH, '//div[@role="none" and @data-visualcompletion="ignore"]')
        sign_in = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[3]/button')
        sign_in.click()
        time.sleep(5)

    def find_followers(self):
        time.sleep(5)
        # noinspection PyBroadException
        try:
            close_button = self.driver.find_element(By.XPATH, '//div[@aria-label="Close"]')
            close_button.click()
        except Exception:
            pass
        time.sleep(3)
        self.driver.get(url='https://www.instagram.com/codemyjourney/')
        time.sleep(3)
        followers = self.driver.find_element(By.XPATH, value='//a[@href="/codemyjourney/followers/"]')
        time.sleep(3)
        followers.click()
        time.sleep(5)

    def follow(self):
        # Find all "Follow" and "Requested" buttons
        follow_buttons = self.driver.find_elements(By.XPATH,
                                                   '//button[div/div[contains(text(), "Follow") or contains(text(), "Requested")]]')
        print(f"Found {len(follow_buttons)} follow buttons.")

        # Loop through all the follow buttons
        while True:
            # Scroll the page down to load more followers
            self.driver.execute_script("window.scrollBy(0, 100);")
            time.sleep(2)

            # Check for "Unfollow" dialog and skip (pass) if it appears
            # noinspection PyBroadException
            try:
                unfollow_button = self.driver.find_element(By.XPATH, '//button[text()="Unfollow"]')
                print("Found 'Unfollow' button, skipping.")
            except Exception as e:
                pass

            # Find all "Follow" buttons again after scrolling (elements might be dynamically added)
            follow_buttons = self.driver.find_elements(By.XPATH,
                                                       '//button[div/div[contains(text(), "Follow") or contains(text(), "Requested")]]')

            # Click all found "Follow" or "Requested" buttons
            for button in follow_buttons:
                try:
                    # Check the text of the button
                    button_text = button.text
                    if button_text == "Follow" or button_text == "Requested":
                        # Scroll the button into view and click it
                        self.driver.execute_script("arguments[0].scrollIntoView();", button)
                        time.sleep(1)
                        button.click()
                        print(f"Clicked '{button_text}' button.")
                        time.sleep(2)
                    else:
                        print(f"Skipped '{button_text}' button.")
                except Exception as e:
                    print(f"Error clicking follow button: {e}")

            # Exit the loop if there are no more follow buttons to click (prevent infinite loop)
            if len(follow_buttons) == 0:
                break

