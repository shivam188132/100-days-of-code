import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://news.ycombinator.com/")
web_page = response.text
print(web_page)
soup = BeautifulSoup(web_page, "html.parser")
article_titles = []
links = []


for article in soup.find_all(name="a", rel="noreferrer"):
    text = article.string
    article_titles.append(text)
    link = article.get("href")
    links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
largest_vote = max(article_upvotes)
article_index = article_upvotes.index(largest_vote)
# print(article_index)
print(article_titles[article_index])
print(links[article_index])

# print(article_titles)
#
# print(links)
# print(article_upvotes)
# print(largest_vote)
