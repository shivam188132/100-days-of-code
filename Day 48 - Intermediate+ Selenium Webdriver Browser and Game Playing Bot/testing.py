from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# clicks = int(input("How many clicks do you want? : "))

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie_click = driver.find_element(By.XPATH, '//*[@id="cookie"]')
money = driver.find_element(By.XPATH, '//*[@id="money"]')

cursor = driver.find_element(By.XPATH, '//*[@id="buyCursor"]')
grandma = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]')
factory = driver.find_element(By.XPATH, '//*[@id="buyFactory"]')
mine = driver.find_element(By.XPATH, '//*[@id="buyMine"]')
shipment = driver.find_element(By.XPATH, '//*[@id="buyShipment"]')
alchemy_lab = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]')
portal = driver.find_element(By.XPATH, '//*[@id="buyPortal"]')

upgrades = driver.find_elements(By.CSS_SELECTOR, "#store b")
print(type(upgrades))
for _ in upgrades:
    print(_.text)


# print(upgrades)
import re

upgrades = driver.find_elements(By.CSS_SELECTOR, "#store b")

# Use regular expression to find all numeric values in each upgrade text
numeric_values = []
for upgrade in upgrades:
    numeric_values.extend(re.findall(r'\d[\d,]*', upgrade.text))

# Process the numeric values to remove commas and convert to integers
numeric_values = [int(value.replace(',', '')) for value in numeric_values]

print(numeric_values)







driver.close()


