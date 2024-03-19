from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")


# nu_data = driver.find_element(By.ID, 'articlecount').find_element(By.TAG_NAME, "a")
# print(nu_data.text)
# nu_data.click()
# continue_link = driver.find_element(By.LINK_TEXT, 'Operation Overlord')
# continue_link.click()
search = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/div/div/div/form/div/div/div[1]/input')
print(search.text)
search.send_keys("python")
search.send_keys(Keys.ENTER)
