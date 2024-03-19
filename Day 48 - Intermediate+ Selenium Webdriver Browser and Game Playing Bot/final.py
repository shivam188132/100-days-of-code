import time

from selenium import webdriver
from selenium.webdriver.common.by import By

ask = input("for how much time(in minutes) u want to run ? \n example press press 1 for 1 min:   ")


chrome_driver_path = "Users\jojo\OneDrive\Documents\Coding\chromedriver_win32\chromedriver.exe"
# service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome()

URL = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url=URL)


# gets cookie and clicks on it to click
def click_cookie():
    cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')
    cookie.click()


# checks the number of cookies available, returns integer of number of cookies available
def get_cookie_count():
    cookie_counter = driver.find_element(By.XPATH, '//*[@id="money"]').text

    if "," in cookie_counter:
        cookie_counter = cookie_counter.replace(",", "")

    return int(cookie_counter)


# buy the most expensive upgrade available, takes cookie count as input
def buy_upgrade(cookie_count):
    # get the current list of all upgrades
    upgrades = driver.find_elements(By.CSS_SELECTOR, "#store b")
    upgrades_list = []
    for _ in range(len(upgrades)):
        upgrade = upgrades[_].text
        if upgrade != "":
            upgrades_list.append(upgrade)

    # get the integer prices for all upgrades
    list_upgrade_prices = []
    for upgrade_price in upgrades_list:
        upgrade_price = upgrade_price.split('-')[1].strip()
        if "," in upgrade_price:
            upgrade_price = upgrade_price.replace(",", "")
        list_upgrade_prices.append(int(upgrade_price))

    # Determine the most expensive affordable upgrade based on cookie count passed into function
    affordable_items = []
    for item in list_upgrade_prices:
        if item < cookie_count:
            affordable_items.append(item)
    if len(affordable_items) > 0:
        most_expensive_affordable_item = max(affordable_items)

        index_item_to_buy = list_upgrade_prices.index(most_expensive_affordable_item)
        item_to_buy = upgrades_list[index_item_to_buy]
        item_to_buy_in_string = str(item_to_buy.split("-")[0].strip())

        # Click to buy the most expensive affordable upgrade
        buy_item = driver.find_element(By.ID, f"buy{item_to_buy_in_string}")
        buy_item.click()

    else:
        pass


# Checks for available upgrades every 5 secs
t_end = time.time() + 5

# game ends after x mins
game_end = time.time() + (60 * int(ask))
game_on = True

while game_on:
    click_cookie()
    if time.time() > t_end:
        cookie_count = get_cookie_count()
        item_to_buy = buy_upgrade(cookie_count)
        t_end = time.time() + 20

    if time.time() > game_end:
        game_on = False
        cookies_per_second = driver.find_element(By.XPATH, '//*[@id="cps"]').text
        print(f"Time Up!!, your {cookies_per_second}. Congratulations")
