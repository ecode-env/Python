import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_option)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(url='https://www.speedtest.net/')
        time.sleep(10)  # Wait for page to load

        # Click the "Go" button
        click = self.driver.find_element(By.CSS_SELECTOR, ".start-button .start-text")
        click.click()

        time.sleep(45)  # Wait longer for test to complete

        # Get download and upload speeds
        down_speed = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        up_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

        self.down = down_speed
        self.up = up_speed

        return self.down, self.up

    def tweet_at_provider(self, email, password, internet_provider, down, up):
        self.driver.get(url='https://x.com/i/flow/login')
        time.sleep(10)  # Wait for page to load

        # 1️⃣ Enter email/username
        email_input = self.driver.find_element(By.NAME, 'text')
        email_input.send_keys(email)
        time.sleep(2)
        email_input.send_keys(Keys.ENTER)

        # 2️⃣ If extra username confirmation appears, enter it
        time.sleep(5)
        try:
            username_input = self.driver.find_element(By.NAME, 'text')
            username_input.send_keys("CodeTesten85949")
            time.sleep(2)
            username_input.send_keys(Keys.ENTER)
        except:
            pass

        # 3️⃣ Enter password
        time.sleep(5)
        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys(password)
        time.sleep(2)
        password_input.send_keys(Keys.ENTER)

        # 4️⃣ Wait and type tweet
        time.sleep(5)
        post = self.driver.find_element(By.CSS_SELECTOR, "div[role='textbox']")

        tweet_text = (
            f"Hello, {internet_provider}, why is my internet speed {self.down} Mbps down "
            f"and {self.up} Mbps up, when I pay for {down} Mbps down and {up} Mbps up? "
            f"Please fix this! #InternetSpeed #SlowInternet"
        )
        post.send_keys(tweet_text)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, '//div[@data-testid="tweetButtonInline"]')
        tweet_button.click()
        time.sleep(10)
        self.driver.quit()
