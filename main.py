import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Browser:
    browser, service = None, None

    # Initialise the webdriver with the path to chromedriver.exe SA 12/14/22
    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    def open_page(self, url: str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()

        # Function to find open input field and enter text SA 12/14/22

    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(1)

        # Function to find and click button to log in SA 12/14/22

    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)

    def login_aem(self, username: str, password: str):
        self.add_input(by=By.ID, value='username', text=username)
        self.add_input(by=By.ID, value='password', text=password)
        self.click_button(by=By.ID, value='submit-button')

    def click_sites(self, ):
        self.click_button(by=By.XPATH, value='//div[@class="globalnav-homecard-title" and text()="Sites"]')

    def click_newswire(self, ):
        self.click_button(by=By.ID, value='coral-id-42')

    def quick_publish(self, ):
        self.click_button(by=By.XPATH, value='//button[@trackingelement="Quick Publish"]')


if __name__ == '__main__':
    # When Chrome is updated the chromedriver.exe needs to be updated as well SA 12/14/22
    # 'https://chromedriver.chromium.org/downloads'
    browser = Browser('Drivers/chromedriver.exe')

    browser.open_page('https://devaem.caes.uga.edu:8443/')
    time.sleep(3)

    browser.login_aem(username='sa69508', password='Willsjack1212@')
    browser.click_sites()
    browser.click_newswire()
    time.sleep(4000)

    # browser.open_page('https://www.google.com')
    # time.sleep(3)
    #
    # browser.open_page('https://uga.edu/')
    # time.sleep(3)
    #
    # browser.close_browser()
