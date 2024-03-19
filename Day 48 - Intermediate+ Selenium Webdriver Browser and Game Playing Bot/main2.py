from selenium import webdriver
# Import the By class
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")
data =driver.find_elements(By.CSS_SELECTOR, "span.say-no-more")

for element in data:
    print(element.text)