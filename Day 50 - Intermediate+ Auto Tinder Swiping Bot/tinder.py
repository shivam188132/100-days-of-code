import random
import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# Maximize the Chrome window
driver.maximize_window()
driver.get(url="https://tinder.com/")

time.sleep(4)
login_button = driver.find_element(By.CSS_SELECTOR, 'button[data-size="large"]')
login_button.click()
time.sleep(3)
login_with_fb = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Log in with Facebook"]')
login_with_fb.click()
time.sleep(3)

# Switch to Facebook login window

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

login_id = driver.find_element(By.XPATH, '//*[@id="email"]')
login_id.send_keys("xxxxxxxxx")

login_pass = driver.find_element(By.XPATH, '//*[@id="pass"]')
login_pass.send_keys("ixxxxxxxxx")

# login_bt = driver.find_element(By.XPATH, '//*[@id="u_0_0_lC"]')
time.sleep(2)
login_pass.send_keys(Keys.ENTER)

# Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)

# Delay by 5 seconds to allow page to load.
time.sleep(10)

# Allow location
allow_location_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Allow"]')
allow_location_button.click()
time.sleep(12)

# Disallow notifications
notifications_button = driver.find_element(By.XPATH, '//button[@aria-label="Not interested"]')
notifications_button.click()
time.sleep(5)
# Allow cookies
cookies = driver.find_element(By.XPATH, '//div[text()="I accept"]/ancestor::button')
cookies.click()
time.sleep(6)
# Tinder free tier only allows 100 "Likes" per day. looping in  while loop
for n in range(100):
    choice = random.randint(0, 3)
    # Add a 1 second delay between likes.
    time.sleep(2)
    try:
        if choice == 0:
            print("yes")
            like_button = driver.find_element(By.XPATH,
                                              '//button[contains(@class, "button") and contains(@class, "Bgi($g-ds-background-like)") and contains(@class, "Expand") and contains(@class, "Cur(p)") and contains(@class, "Scale(1.1):h") and contains(@class, "Scale(.9):a")]')
            like_button.click()

        else:
            print("no babe ")
            dislike_button = driver.find_element(By.XPATH,
                                                 '//button[contains(@class, "button") and contains(@class, "Bgi($g-ds-background-nope)") and contains(@class, "Expand") and contains(@class, "Cur(p)") and contains(@class, "Scale(1.1):h") and contains(@class, "Scale(.9):a")]')
            dislike_button.click()

    except ElementClickInterceptedException:
        time.sleep(6)

    except NoSuchElementException:
        print("error countered unable to find the button")

driver.quit()
