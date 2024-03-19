
import requests
response = requests.get(url="https://www.linkedin.com/jobs/search/?currentJobId=3672047688&keywords=data%20analyst")
html_content = response.text
# print(html_content)



from bs4 import BeautifulSoup

soup = BeautifulSoup(html_content, "html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))

