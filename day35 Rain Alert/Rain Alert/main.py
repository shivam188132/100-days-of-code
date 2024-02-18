from twilio.rest import Client
api_key = "xxxxxxxxxxxxxxxxxxxxxxx"
import requests
code = 0
account_sid = 'xxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxx'



weather_params = {
    "lon": 85.1167,
     "lat": 25.6,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

"""weather_data = response.json()["weather"][0]["id"]
# for _ in weather_data:
#
#      code = (_["id"])
# if code <= 700:
#      print("bring an Umbrella")
if weather_data <= 700:
     client = Client(account_sid, auth_token)"""





