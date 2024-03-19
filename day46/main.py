import requests
from bs4 import BeautifulSoup


# date = input("what year you would like to travel to in YYY-MM-DD format: ")
response = requests.get(url="https://www.billboard.com/charts/hot-100/2000-08-12/")
web_data = response.text

soup = BeautifulSoup(web_data, "html.parser")
# name = soup.find(name="h3", class_="c-title").getText()
# print(name)

song_name = [title.getText().strip() for title in soup.find_all(name="h3", class_="a-no-trucate")]
# incomplete_song = song_name[1]
# song_names_spans = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_names_spans]
# print(song_name)
with open("song.txt", "w") as datafile:
    for song in song_name:
        # print(type(song))
        datafile.write(f"{song}\n")