import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

# Extract titles
titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]

# Reverse the order
# titles.reverse()
movie = titles[::-1]

# Write the reversed list to the file
with open("file.txt", "w", encoding="utf-8") as data_file:
    for title in movie:
        data_file.write(title + "\n")

