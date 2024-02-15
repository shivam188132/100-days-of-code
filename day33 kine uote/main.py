import requests
responce = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(responce)
# print(responce.status_code)
responce.raise_for_status()
data = responce.json()
print(data)
latitude = responce.json()["iss_position"]["latitude"]
longitude = responce.json()["iss_position"]["longitude"]
iss_position = (latitude, longitude)
print(iss_position)