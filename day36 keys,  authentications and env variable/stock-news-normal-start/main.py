import requests
from twilio.rest import Client

account_sid = 'xxxxx'
auth_token = 'xxxxxx'
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

API_KEY = "xxxxxx"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_api_key = "7a995ac7d18a41e295c78e248bda45ba"

parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data1 = response.json()["Time Series (Daily)"]
data1_list = [value for (key, value) in data1.items()]
# print(data1_list)
yesterday_closing_price = float(data1_list[0]['4. close'])

day_before_yesterday_closing_price = float(data1_list[1]['4. close'])

difference = day_before_yesterday_closing_price - yesterday_closing_price
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percentage_difference = (difference / day_before_yesterday_closing_price) * 100
print(percentage_difference)

if percentage_difference >= 0:
    # print("Get News")
    news_params = {
        "apiKey": news_api_key,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{percentage_difference}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
        for article in three_articles]
    print(formatted_articles)
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+14177945054',
            to='+919835568198'
        )
        print(message.status)
