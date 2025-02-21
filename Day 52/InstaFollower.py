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
        time.sleep(10)

        email_input = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        email_input.send_keys(email)
        time.sleep(2)

        password_input = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        password_input.send_keys(password)
        time.sleep(2)

        sign_in = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[3]/button')
        sign_in.click()
        time.sleep(5)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(url='https://www.instagram.com/codemyjourney/')
        followers = self.driver.find_element(By.XPATH, value='//*[@id="mount_0_0_DT"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a')
        time.sleep(3)
        followers.click()

    def follow(self):
        x_path='/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div'
        scr1 = self.driver.find_element(By.XPATH, value=x_path)
        print(scr1)
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
