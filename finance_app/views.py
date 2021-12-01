from datetime import datetime
from django.shortcuts import render
import requests
import environ

env = environ.Env()
environ.Env.read_env()

stock_api_key = env('STOCK_API_KEY')


def index(request):
    context = {}
    context.update(fetch_news(request))
    context.update(fetch_stocks(request))
    context.update(fetch_crypto(request))
    return render(request, 'index.html', context)


def fetch_news(request):
    input = datetime.now()
    today = input.strftime('%Y-%m-%d')
    # while True:
    crypto_news = []
    stocks_news = []
    business_news = []
    try:
        crypto_response = requests.get(f'https://newsapi.org/v2/everything?q=bitcoin&{today}&sortBy=publishedAt&'
                                       'apiKey=a292184125094d328398eaa6c0a624b1').json()
        stock_response = requests.get(f'https://newsapi.org/v2/everything?q=stock&{today}&sortBy=publishedAt&'
                                      'apiKey=a292184125094d328398eaa6c0a624b1').json()
        business_response = requests.get(f'https://newsapi.org/v2/everything?q=business&{today}&sortBy=publishedAt&'
                                         'apiKey=a292184125094d328398eaa6c0a624b1').json()

        time_c = 1
        for i in crypto_response["articles"]:
            if time_c <= 10:
                time_c += 1
                t_in = i["publishedAt"]
                t_out = datetime.strptime(t_in[0:19], "%Y-%m-%dT%H:%M:%S")
                i["publishedAt"] = t_out
                crypto_news.append(i)

        time_s = 1
        for j in stock_response["articles"]:
            if time_s <= 10:
                time_s += 1
                t_in = j["publishedAt"]
                t_out = datetime.strptime(t_in[0:19], "%Y-%m-%dT%H:%M:%S")
                j["publishedAt"] = t_out
                stocks_news.append(j)

        time_b = 1
        for k in business_response["articles"]:
            if time_b <= 10:
                time_b += 1
                t_in = k["publishedAt"]
                t_out = datetime.strptime(t_in[0:19], "%Y-%m-%dT%H:%M:%S")
                k["publishedAt"] = t_out
                business_news.append(k)

        return {'crypto_news': crypto_news, 'stocks_news': stocks_news, 'business_news': business_news}
    except:
        return {'bit_coin_news': "Some problems happen during the data fetching: bit_coin_news",
                'stock_news': "Some problems happen during the data fetching: stock_news",
                'business_news': "Some problems happen during the data fetching: business_news"}


def fetch_stocks(request):
    try:
        url = 'https://api.stockdata.org/v1/data/quote'
        stocks_symbol = ["IQV,ENB,FB", "AMZN,BKNG,TSLA", "AAPL,GOOGL,MSFT", "MA"]
        stock_details = []
        for i in range(4):
            querystring = {"api_token": API_KEY, "symbols": stocks_symbol[i]}
            response = requests.request("GET", url, params=querystring)
            response = response.json()
            for s in response["data"]:
                t_in = s["last_trade_time"]
                t_out = datetime.strptime(t_in[0:19], "%Y-%m-%dT%H:%M:%S")
                s["last_trade_time"] = t_out
                print("t_out: " + str(t_out))
            stock_details = stock_details + response["data"]
        return {"stock_data": stock_details}
    except:
        return {"stock_data": "Some problems happen during the data fetching: stocks data"}


def fetch_crypto(request):
    try:
        crypto_rank = ["1", "2", "3", "4", "5",
                       "6", "7", "8", "9", "10"]
        input = datetime.now()
        time = input.strftime("%Y-%M-%d %H:%M")
        print(time)
        crypto = []
        response = requests.get('https://api.coincap.io/v2/assets')
        response = response.json()
        for i in response["data"]:
            if i["rank"] in crypto_rank:
                crypto.append(i)

        return {'allCrypto': crypto, 'time': time}
    except:
        return {'allCrypto': "Some problems happen during the data fetching: crypto data"}


def fetch_primary_data(request):
    return render(request, 'primary_data.html')
