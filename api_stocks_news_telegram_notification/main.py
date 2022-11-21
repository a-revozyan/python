import requests
from datetime import date, timedelta
import sys, os
from io import StringIO

CURRENT_DATETIME = str(date.today() - timedelta(days=1))
STOCK = ["TSLA", "AMZN"]
MY_NEWS_API_KEY = os.environ["NEWS_API_KEY"]
STOCK_INFO_ARTIFACT = {
    "TESLA_STOCK": {},
    "AMAZON_STOCK": {},
}
NEWS_INFO_ARTIFACT = {
    "TESLA_NEWS": {
        "1": [],
        "2": [],
        "3": [],
    },
    "AMAZON_NEWS": {
        "1": [],
        "2": [],
        "3": [],
    },
}

def get_stocks_info(STOCK):

    MY_STOCK_API_KEY = os.environ["STOCK_API_KEY"]
    for x in STOCK:
        parameters_stock = {
            "apikey": MY_STOCK_API_KEY,
            "symbol": x,
            "outputsize": "full",
            "function": "TIME_SERIES_DAILY_ADJUSTED",
        }
        url_stock = "https://www.alphavantage.co/query"
        response_stock = requests.get(url_stock, params=parameters_stock)
        response_stock.raise_for_status()
        data_stock = response_stock.json()
        opened_with = data_stock["Time Series (Daily)"][CURRENT_DATETIME]["1. open"]
        closed_with = data_stock["Time Series (Daily)"][CURRENT_DATETIME]["4. close"]
        opened = f"{CURRENT_DATETIME}, Opened {x}, {opened_with}"
        closed = f"{CURRENT_DATETIME}, Closed {x}, {closed_with}"
        if x == "TSLA":
            STOCK_INFO_ARTIFACT["TESLA_STOCK"]["open_date"] = opened
            STOCK_INFO_ARTIFACT["TESLA_STOCK"]["close_date"] = closed
        elif x == "AMZN":
            STOCK_INFO_ARTIFACT["AMAZON_STOCK"]["open_date"] = opened
            STOCK_INFO_ARTIFACT["AMAZON_STOCK"]["close_date"] = closed

    get_news_info(STOCK)

def get_news_info(STOCK):

    STOCK[0] = "TESLA"
    STOCK[1] = "AMAZON"

    for x in STOCK:
        parameters_news = {
            "q": x,
            "from": CURRENT_DATETIME,
            "sortBy": "popularity&",
            "apiKey": "e9e365be3ffb42818945f74ece01a931",
        }

        url_news = "https://newsapi.org/v2/everything?"
        response_news = requests.get(url_news, params=parameters_news)
        response_news.raise_for_status()
        data_news = response_news.json()

        if x == "TESLA":
            count = 0
            for x in data_news["articles"][:3]:
                count += 1
                source = x.get("source")["name"]
                NEWS_INFO_ARTIFACT["TESLA_NEWS"][f"{count}"].append(source)
                title = x.get("title")
                NEWS_INFO_ARTIFACT["TESLA_NEWS"][f"{count}"].append(title)
                description = x.get("description")
                NEWS_INFO_ARTIFACT["TESLA_NEWS"][f"{count}"].append(description)
        elif x == "AMAZON":
            count = 0
            for x in data_news["articles"][:3]:
                count += 1
                source = x.get("source")["name"]
                NEWS_INFO_ARTIFACT["AMAZON_NEWS"][f"{count}"].append(source)
                title = x.get("title")
                NEWS_INFO_ARTIFACT["AMAZON_NEWS"][f"{count}"].append(title)
                description = x.get("description")
                NEWS_INFO_ARTIFACT["AMAZON_NEWS"][f"{count}"].append(description)

get_stocks_info(STOCK)

def send_to_telegram():

    TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
    TELEGRAM_CHAT_ID = "-863117164"
    apiURL = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'

    try:
        stock_info = "\n###############TESLA###############\n"
        for key, value in STOCK_INFO_ARTIFACT["TESLA_STOCK"].items():
            stock_info += str(f"{value}\n")
        stock_info += "\n##############AMAZON##############\n"
        for key, value in STOCK_INFO_ARTIFACT["AMAZON_STOCK"].items():
            stock_info += str(f"{value}\n")


        news_info = "\n #############TESLA_NEWS#############\n"
        for x in NEWS_INFO_ARTIFACT["TESLA_NEWS"].items():
            buffer = StringIO()
            sys.stdout = buffer
            print(*x[1], sep=", " "\n")
            news_info += buffer.getvalue()
        news_info += "\n #############AMAZON_NEWS#############\n"
        for x in NEWS_INFO_ARTIFACT["AMAZON_NEWS"].items():
            buffer = StringIO()
            sys.stdout = buffer
            print(*x[1], sep=", " "\n")
            news_info += buffer.getvalue()

        requests.post(apiURL, json={'chat_id': TELEGRAM_CHAT_ID, 'text': stock_info})
        requests.post(apiURL, json={'chat_id': TELEGRAM_CHAT_ID, 'text': news_info})
    except Exception as e:
        print(e)

send_to_telegram()
