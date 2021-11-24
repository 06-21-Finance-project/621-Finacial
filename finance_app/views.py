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
    # context.update(fetch_stocks(request))
    context.update(fetch_crypto(request))
    return render(request, 'index.html', context)


def fetch_news(request):
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
    crypto = []
    temp = []
    response = requests.get('https://api.coincap.io/v2/assets')
    response = response.json()
    temp = temp + response["data"]

    for i in range(10):
        crypto.append(temp[i])
    return {'allCrypto': crypto}
