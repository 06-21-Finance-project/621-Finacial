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
    try:
        input = datetime.now()
        today = input.strftime('%Y-%m-%d')
        # while True:
        bit_coin_news = requests.get(f'https://newsapi.org/v2/everything?q=bitcoin&from={today}&sortBy=publishedAt&'
                                     'apiKey=e4a078da3fc844f9a8cd5690e7c4a0f2').json
        stock_news = requests.get(f'https://newsapi.org/v2/everything?q=stock&from={today}&sortBy=publishedAt&'
                                  'apiKey=e4a078da3fc844f9a8cd5690e7c4a0f2').json
        business_news = requests.get('https://newsapi.org/v2/everything?q=business&'
                                     f'from={today}&sortBy=publishedAt&apiKey=e4a078da3fc844f9a8cd5690e7c4a0f2').json
        return {'bit_coin_news': bit_coin_news, 'stock_news': stock_news, 'business_news': business_news}
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
            querystring = {"api_token": stock_api_key, "symbols": stocks_symbol[i]}
            response = requests.request("GET", url, params=querystring)
            response = response.json()
            stock_details = stock_details + response["data"]
        return {"stock_data": stock_details}
    except:
        return {"stock_data": "Some problems happen during the data fetching: stocks data"}


def fetch_crypto(request):
    try:
        crypto = []
        response = requests.get('https://api.coincap.io/v2/assets')
        response = response.json()
        for i in range(10):
            crypto = crypto + response["data"]
        return {'allCrypto': crypto}
    except:
        return {'allCrypto': "Some problems happen during the data fetching: crypto data"}


def fetch_primary_data(request):
        return render(request, 'primary_data.html')

