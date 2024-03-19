from bs4 import BeautifulSoup



with open("testing.html",encoding="utf8") as datafile:
    my_data = datafile.read()

soup = BeautifulSoup(my_data, "html.parser")
# print(soup.select("li a"))
# print(soup.find_all("a li"))

# print(soup.find(name="form"))
# from_tag = soup.find(name="form")
# print(from_tag.maxlength)
# print(soup.from_tag.maxlength)
# print(soup.select("input"))
from_tag = soup.find("input")
print(from_tag.get("maxlength"))