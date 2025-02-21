import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class FillOut:
    def __init__(self):
        self.optional_chrome = webdriver.Chrome()
        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=self.chrome_option)

    def fill_out_a_form(self, get_addresses, get_prices, get_links):
        form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSewDHZCYIoFQZx5KIB9DEmUbVjOxibxhRHurJc9mz6qRJveYg/viewform?usp=dialog'

        for i in range(len(get_addresses)):
            self.driver.get(form_url)
            time.sleep(2)


            input_fields = self.driver.find_elements(By.CSS_SELECTOR, value='.o3Dpx input')
            submit_button = self.driver.find_element(By.CSS_SELECTOR, value='span span')

            if len(input_fields) >= 3:
                input_fields[0].send_keys(get_addresses[i])
                time.sleep(1)
                input_fields[1].send_keys(get_prices[i])
                time.sleep(1)
                input_fields[2].send_keys(get_links[i])
                time.sleep(1)
                submit_button.click()
                time.sleep(2)
            else:
                print(f"Error: Not enough input fields found on form for entry {i + 1}")