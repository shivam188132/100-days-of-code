import re
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
ask = input("for how much time(in minutes) u want to run ? \n example press press 1 for 1 min:   ")

drive = webdriver.Chrome()
URL = "http://orteil.dashnet.org/experiments/cookie/"
drive.get(url=URL)


# get the cookie and click on it
def click_cookie():
    cookie = drive.find_element(By.XPATH, '//*[@id="cookie"]')
    cookie.click()



# checks the number of cookies available, returns integer of number of cookies available

def get_cookie_count():
    cookie_counter = drive.find_element(By.XPATH, '//*[@id="money"]').text
    if ',' in cookie_counter:
        cookie_counter.replace(',', '')

    return int(cookie_counter)


# buy the most expensive upgrade available, takes cookie count as input

def buy_cookie_upgrade(cookie_count):
    # get the list of current upgrades
    upgrades_building = drive.find_elements(By.CSS_SELECTOR, "#store b")
    upgrade_list = []
    for _ in range(len(upgrades_building)):
        building_upgrade = upgrades_building[_].text
        if building_upgrade != "":
            upgrade_list.append(building_upgrade)

    # get the integer prices of all upgrades
    building_price_in_numeric = []
    for _ in upgrades_building:
        building_price_in_numeric.extend(re.findall(r'\d[\d,]*', _.text))

    # Process the numeric values to remove commas and convert to integers
    building_price_in_numeric = [int(value.replace(',', '')) for value in building_price_in_numeric]

    # Determine the most expensive affordable upgrade based on cookie count passed into function
    affordable_items = []
    for prices in building_price_in_numeric:
        if prices < cookie_count:
            affordable_items.append(prices)



    if len(affordable_items) > 0:
                most_expensive_affordable_item = max(affordable_items)
                index_item_to_buy = building_price_in_numeric.index(most_expensive_affordable_item)
                item_to_buy = building_price_in_numeric[index_item_to_buy]

                try:
                    # Click to buy the most affordable item
                    buy_item = drive.find_element(By.ID, f"buy{item_to_buy}")
                    buy_item.click()
                except NoSuchElementException:
                    # Handle the case when the element is not found
                    print("Element not found. Skipping purchase.")

    else:
        pass


# Checks for available upgrades every 20 secs
t_end = time.time() + 20

# game ends after x mins
game_end = time.time() + (60*int(ask) )
game_on = True

while game_on:
    click_cookie()
    if time.time() > t_end:
        cookie_count = get_cookie_count()
        item_being_brought  = buy_cookie_upgrade(cookie_count)
        t_end = time.time() + 20

    if time.time() > game_end:
        game_on = False
        cookies_per_second = drive.find_element(By.XPATH, '//*[@id="cps"]').text
        print(f"Time Up!!, your {cookies_per_second}. Congratulations")



