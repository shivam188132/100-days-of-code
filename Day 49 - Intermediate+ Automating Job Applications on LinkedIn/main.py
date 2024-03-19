from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import ElementNotInteractableException
import time

driver = webdriver.Chrome()
driver.get(url="https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&fromSignIn=true&trk=cold_join_sign_in")
account_pass = "xxxxxxxxxx4"

def open_promt():

    user_id = driver.find_element(By.XPATH, '//*[@id="username"]')
    user_id.send_keys("shivamkumar188132@gmail.com")


    user_pass = driver.find_element(By.XPATH, '//*[@id="password"]')
    user_pass.send_keys(account_pass)

    press_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
    press_button.click()

    time.sleep(4)
    try:
     search_button = driver.find_element(By.XPATH, '//*[@id="global-nav-search"]/div/button')
    except ElementNotInteractableException:
        search_button = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')

    search_button.click()
    input_search = driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
    input_search.send_keys("data analyst")
    input_search.send_keys(Keys.ENTER)

    time.sleep(4)

    job_button = driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[1]/button')
    job_button.click()
    time.sleep(4)


    apply = driver.find_element(By.CSS_SELECTOR, 'a.job-card-container__link')
    apply.click()


    save_button = driver.find_element(By.CSS_SELECTOR, 'button.jobs-save-button.artdeco-button.artdeco-button--3.artdeco-button--secondary')
    save_button.click()



open_promt()

time.sleep(30)
