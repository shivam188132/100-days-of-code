from selenium import webdriver
# Import the By class
from selenium.webdriver.common.by import By
import time

# chrome_driver_path = "C:\\Users\shiva\devlopment\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome()
# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
# # time.sleep(5)
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(price.text)

driver.get("https://www.python.org/")
logo = driver.find_element(By.CLASS_NAME, "python-logo")
print(logo.size)

# xpath
button = driver.find_element(By.XPATH, '//*[@id="top"]/nav/ul/li[6]/a')
print(button.text)

driver.close()