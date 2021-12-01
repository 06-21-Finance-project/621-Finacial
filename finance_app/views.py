from django.http import HttpResponse
from time import sleep
from datetime import datetime
from django.shortcuts import render
import requests
import environ

env = environ.Env()
environ.Env.read_env()

API_KEY = env('API_TOKEN')


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
    crypto_response = requests.get(f'https://newsapi.org/v2/everything?q=bitcoin&{today}&sortBy=publishedAt&'
                                 'apiKey=a292184125094d328398eaa6c0a624b1').json
    stock_response = requests.get(f'https://newsapi.org/v2/everything?q=stock&{today}&sortBy=publishedAt&'
                              'apiKey=a292184125094d328398eaa6c0a624b1').json
    business_response = requests.get(f'https://newsapi.org/v2/everything?q=business&{today}&sortBy=publishedAt&'
                                 'apiKey=a292184125094d328398eaa6c0a624b1').json
    # for i in range(10):
    #     crypto_news = crypto_news + crypto_response['data']
    # for i in range(10):
    #     stocks_news = stocks_news + stock_response['data']
    # for i in range(10):
    #     business_news = business_news + business_response['data']

    return {'bit_coin_news': crypto_response, 'stocks_news': stock_response, 'business_news': business_response, 'today': today}


def fetch_stocks(request):
    url = 'https://api.stockdata.org/v1/data/quote'
    stocks_symbol = ["IQV,ENB,FB", "AMZN,BKNG,TSLA", "AAPL,GOOGL,MSFT", "MA"]
    stock_details = []
    for i in range(4):
        querystring = {"api_token": API_KEY, "symbols": stocks_symbol[i]}
        response = requests.request("GET", url, params=querystring)
        response = response.json()
        stock_details = stock_details + response["data"]
    return {"stock_data": stock_details}


def fetch_crypto(request):
    input = datetime.now()
    time = input.strftime('%H:%M')
    crypto = []
    response = requests.get('https://api.coincap.io/v2/assets')
    response = response.json()
    for i in range(10):
        crypto = crypto + response["data"]
    return {'allCrypto': crypto, 'time': time}
