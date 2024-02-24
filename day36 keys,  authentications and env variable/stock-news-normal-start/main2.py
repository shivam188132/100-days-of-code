import requests
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "xxxxxxxxxx"
account_sid = 'xxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxx'

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_api_key = "xxxxxxxxxxxxxxxxxx"

stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": API_KEY

}
response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_data = response.json()["Time Series (Daily)"]

stock_data_list = [value for (key, value) in stock_data.items()]
# print(stock_data_list)

yesterday_data = float(stock_data_list[0]["4. close"])
# print(yesterday_data)
day_before_yesterday_data = float(stock_data_list[1]["4. close"])
# print(day_before_yesterday_data)
difference = day_before_yesterday_data - yesterday_data
percent_difference = (difference*day_before_yesterday_data)/100
# print(percent_difference)
up_down = None
if percent_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if abs(percent_difference) > 5:
    news_params = {
        "apiKey": news_api_key,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data_articles = news_response.json()["articles"]
    three_articles = news_data_articles[:3]
    formatted_articles = [f"{STOCK_NAME}: {up_down}{percent_difference}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)
    client = Client(account_sid, auth_token)
    for article in formatted_articles:

        message = client.messages.create(
            body=article,
            from_='+14177945054',
            to='+919835568198'
        )
        print(message.status)

