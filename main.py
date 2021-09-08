#Amr Mualla 
#Stock News Notifier
import requests 
from twilio.rest import Client

STOCK = "AMC"
COMPANY_NAME = "AMC Entertainment"

STOCK2 = "MSFT"
COMPANY_NAME2 = "Microsoft"

STOCK3 = "AAPL"
COMPANY_NAME3 = "Apple"

alphavantage_apikey = "BYX6MFMR3CE83EU9"
news_apikey = "2370768ac0844fc2a9e2b2d5c7a537ee"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_SID = "ACf074087ba6676a8ab1d109904715205c"
TWILIO_AUTH_TOKEN = "d87bf3247af9f6e5db610feb35587132"

MY_NUMBER = "+13476317359"
TWILIO_NUMBER = "+16147050143"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params1 = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alphavantage_apikey,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params1)
data = response.json()["Time Series (Daily)"]
lst = [value for (key,value) in data.items()]
previous_day_data = lst[0]
previous_day_closingprice = previous_day_data["4. close"]


stock_params2 = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alphavantage_apikey,
}
response2 = requests.get(STOCK_ENDPOINT, params=stock_params2)
data2 = response.json()["Time Series (Daily)"]
lst2 = [value for (key,value) in data2.items()]
previous_day_data2 = lst2[0]
previous_day_closingprice2 = previous_day_data2["4. close"]


stock_params3 = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alphavantage_apikey,
}
response3 = requests.get(STOCK_ENDPOINT, params=stock_params3)
data3 = response.json()["Time Series (Daily)"]
lst3 = [value for (key,value) in data3.items()]
previous_day_data3 = lst3[0]
previous_day_closingprice3 = previous_day_data3["4. close"]

day_before_previous_day = lst[1]
day_before_previous_day_close = day_before_previous_day["4. close"]
day_before_previous_day2 = lst2[1]
day_before_previous_day_close2 = day_before_previous_day2["4. close"]
day_before_previous_day3 = lst3[1]
day_before_previous_day_close3 = day_before_previous_day3["4. close"]

stock_difference = abs(float(previous_day_closingprice) - float(day_before_previous_day_close))
stock_change = None
if stock_difference > 0:
    stock_change = "🔺"
else:
    stock_change = "🔻"

stock2_difference = abs(float(previous_day_closingprice2) - float(day_before_previous_day_close2))
stock2_change = None
if stock2_difference > 0:
    stock2_change = "🔺"
else:
    stock2_change = "🔻"

stock3_difference = abs(float(previous_day_closingprice3) - float(day_before_previous_day_close3))
stock3_change = None
if stock3_difference > 0:
    stock3_change = "🔺"
else:
    stock3_change = "🔻"

stock_delta = round(stock_difference / float(previous_day_closingprice) * 100)
stock2_delta  = round(stock2_difference / float(previous_day_closingprice2) * 100)
stock3_delta = round(stock3_difference / float(previous_day_closingprice3) * 100)

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

if abs(stock_delta) >= 1:
    news_params = {
        "apiKey": news_apikey,
        "qInTitle": STOCK,
    }
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = response.json()["articles"]
    main_articles = articles[:3]
    articles_message = [f"{STOCK}: {stock_change}{stock_delta}%Headline: {article['title']}. \nBrief: {article['description']}" for article in main_articles]
    for article in articles_message:
        message = client.messages.create(
            body=article,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER,
        )
        print(message.status)

if abs(stock2_delta) >= 1:
    news_params = {
        "apiKey": news_apikey,
        "qInTitle": STOCK2,
    }
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = response.json()["articles"]
    main_articles = articles[:3]
    articles_message = [f"{STOCK2}: {msft_change}{msft_delta}%Headline: {article['title']}. \nBrief: {article['description']}" for article in main_articles]
    for article in articles_message:
        message = client.messages.create(
            body=article,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER,
        )
        print(message.status)

if abs(stock2_delta) >= 1:
    news_params = {
        "apiKey": news_apikey,
        "qInTitle": STOCK3,
    }
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = response.json()["articles"]
    main_articles = articles[:3]
    articles_message = [f"{STOCK3}: {stock3_change}{stock3_delta}%Headline: {article['title']}. \nBrief: {article['description']}" for article in main_articles]
    for article in articles_message:
        message = client.messages.create(
            body=article,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER,
        )
        print(message.status)
-