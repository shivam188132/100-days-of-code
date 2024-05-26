import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By


class InternetSpeedTwitterBot:
    def __init__(self):
        self.Promise_up = 30
        self.Promise_down = 30

        self.Twitter_user_id = "xxxx"
        self.Twitter_pass = "xxxxx"

        self.driver = webdriver.Chrome()

    def get_internet_speed(self):
        self.driver.maximize_window()
        self.driver.get(url="https://www.speedtest.net/")
        time.sleep(3)
        accept_cookies = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        accept_cookies.click()
        time.sleep(1)
        click_run = self.driver.find_element(By.XPATH,
                                             '//a[@aria-label="start speed test - connection type multi" and contains(@class, "js-start-test")]/span[@class="start-text"]')
        click_run.click()
        time.sleep(60)
        self.down_speed = self.driver.find_element(By.XPATH,
                                                   '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print(f"DOWN SPEED : {self.down_speed}")
        self.up_speed = self.driver.find_element(By.XPATH,
                                                 '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"UP SPEED : {self.up_speed}")

    def Twitter_bot(self):
        self.driver.maximize_window()
        self.driver.get(url="https://twitter.com/i/flow/login")
        time.sleep(5)
        username_prompt = self.driver.find_element(By.XPATH, '//input[@name="text" and @autocomplete="username"]')
        username_prompt.send_keys(f"{self.Twitter_user_id}")
        time.sleep(1)
        next_button = self.driver.find_element(By.XPATH,
                                               '//div[@role="button" and @tabindex="0" and contains(@class, "css-18t94o4") and contains(@class, "css-1dbjc4n") and contains(@class, "r-sdzlij") and contains(@class, "r-1phboty") and contains(@class, "r-rs99b7") and contains(@class, "r-ywje51") and contains(@class, "r-usiww2") and contains(@class, "r-2yi16") and contains(@class, "r-1qi8awa") and contains(@class, "r-1ny4l3l") and contains(@class, "r-ymttw5") and contains(@class, "r-o7ynqc") and contains(@class, "r-6416eg") and contains(@class, "r-lrvibr") and contains(@class, "r-13qz1uu")]/div[@dir="ltr" and contains(@class, "css-901oao")]/span[contains(@class, "css-901oao") and contains(@class, "css-16my406") and contains(@class, "r-poiln3") and contains(@class, "r-bcqeeo") and contains(@class, "r-qvutc0")]/span[contains(@class, "css-901oao") and contains(@class, "css-16my406") and contains(@class, "r-poiln3") and contains(@class, "r-bcqeeo") and contains(@class, "r-qvutc0") and contains(text(), "Next")]')
        next_button.click()
        time.sleep(2)
        password = self.driver.find_element(By.XPATH, '//input[@type="password" and @name="password"]')
        password.send_keys(f"{self.Twitter_pass}")
        click_login = self.driver.find_element(By.XPATH, '//div[@data-testid="LoginForm_Login_Button"]')
        click_login.click()
        self.tweet = f"@JioCare i am getting my down_speed as {self.down_speed} \n and upload speed as {self.up_speed} \n as what you promised."
        time.sleep(5)
        try:
            type_column = self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetTextarea_0"]')
        except ElementClickInterceptedException:
            time.sleep(5)

        type_column.send_keys(self.tweet)
        time.sleep(2)
        send_tweet = self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetButtonInline"]')

        send_tweet.click()
        time.sleep(6)
