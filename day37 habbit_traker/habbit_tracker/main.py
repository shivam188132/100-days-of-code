import requests
from datetime import datetime

USERNAME = "xxxxxx"
TOKEN = "xxxxxxxx"
GRAPH_ID = "graph7"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# creating user

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph7",
    "name": "Raja Billa Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url= graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


pixel_endpoint = f"{graph_endpoint}/graph7"
date = datetime(year=2023, month=7, day=10).strftime("%Y%m%d")

pixel_config = {
    "date": date,
    "quantity": "15.56",


}
# todays_date = datetime.now().strftime("%Y%m%d")
# response = requests.put(url=put_endpoint, json=put_config, headers=headers)
# print(response.text)


put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230710"

put_config = {
    "quantity": "4",

}

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230710"
reaponse = requests.delete(url = delete_endpoint, headers=headers)
print(reaponse.text)




