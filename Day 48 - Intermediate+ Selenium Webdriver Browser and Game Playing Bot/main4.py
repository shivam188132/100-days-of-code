from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Locate the search input element
search_input = driver.find_element(By.NAME, "search")

# Type the search query into the input
search_input.send_keys("Python")

# Simulate pressing the Enter key to submit the form or trigger an action
search_input.send_keys(Keys.ENTER)

# Wait for a few seconds to see the results or perform further actions
# ...

# Remember to close the webdriver when you are done
driver.quit()
