"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://secure-retreat-92358.herokuapp.com/")
input_list = ["Shivam", "kumar", "shivamkumar819991@gmail.com"]
input_arg = ["fName", "lName", "email"]
is_on = True
while is_on:
    for _ in input_arg:
        search_input = driver.find_element(By.NAME, _)
        for _ in input_list:
            search_input.send_keys(input_list, _)
            search_input.send_keys(Keys.ENTER)

    is_on = False
time.sleep(5)"""


# method 2



"""rom selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://secure-retreat-92358.herokuapp.com/")

input_list = ["Shivam", "kumar", "shivamkumar819991@gmail.com"]
input_arg = ["fName", "lName", "email"]

# Iterate through the input_arg and input_list simultaneously
for arg, value in zip(input_arg, input_list):
    search_input = driver.find_element(By.NAME, arg)
    search_input.send_keys(value)

# Submit the form (assuming there is a submit button)
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()

time.sleep(5)

# Remember to close the webdriver when you are done
driver.quit()"""

# or

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://secure-retreat-92358.herokuapp.com/")

input_list = ["Shivam", "kumar", "shivamkumar819991@gmail.com"]
input_arg = ["fName", "lName", "email"]

# Get the length of input_arg (or input_list, assuming both lists have the same length)
num_inputs = len(input_arg)

# Iterate through the lists simultaneously using the range function
for i in range(num_inputs):
    arg = input_arg[i]
    value = input_list[i]

    search_input = driver.find_element(By.NAME, arg)
    search_input.send_keys(value)

# Submit the form (assuming there is a submit button)
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()

time.sleep(5)

# Remember to close the webdriver when you are done
driver.quit()
