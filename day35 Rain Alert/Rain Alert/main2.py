import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "xxxxxxxxxxx"
account_sid = 'xxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxx'

weather_params = {
    "lon": 84.986954,
     "lat": 19.351210,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
x = 0
will_rain = False
while x != 12:
    weather_data = response.json()["hourly"][:12][x]["weather"][0]["id"]
    print(weather_data)
    if weather_data <= 700:
        will_rain = True
    x += 1

if will_rain:
    # print("Bring the Umbrella")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="IT is going to rain 🌧️ today rain shivam babu , kripya chata ☂️ le k nikle wrna gile chuha🐭 jaise dikhogei",
        from_='+14177945054',
        to='+919835568198'
    )
    print(message.status)