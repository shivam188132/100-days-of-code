from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

# Find the specific div containing the events
events_div = driver.find_element(By.CLASS_NAME, "medium-widget.event-widget.last")

# Get all the event items in the div
event_items = events_div.find_elements(By.TAG_NAME, "li")

# Initialize an empty dictionary to store the data
events_dict = {}

# Iterate through the event items and populate the dictionary
for event in event_items:
    date_element = event.find_element(By.TAG_NAME, "time")
    event_name = event.find_element(By.TAG_NAME, "a")

    date_text = date_element.text
    event_name_text = event_name.text

    # Check if the date already exists in the dictionary, if not, create an empty list for that date
    if date_text not in events_dict:
        events_dict[date_text] = []

    # Append the event as a dictionary to the list of events for that date
    events_dict[date_text].append({'event_name': event_name_text})
    # print(events_dict)

# Loop through the events dictionary and print the events
for date, events in events_dict.items():
    print(f"{date}:")
    for event in events:
        print(f"  - {event['event_name']}")
