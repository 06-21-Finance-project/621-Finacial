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
    context = fetch_stocks(request)
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

    return render(request, {'bit_coin_news': bit_coin_news, 'stock_news': stock_news, 'business_news': business_news})


def fetch_stocks(request):
    url = 'https://api.stockdata.org/v1/data/quote'
    stocks_symbol = ["IQV,ENB,FB", "AMZN,BKNG,TSLA", "AAPL,GOOGL,MSFT", "MA"]
    context = {}
    stock_details = []
    for i in range(4):
        querystring = {"api_token": API_KEY, "symbols": stocks_symbol[i]}
        response = requests.request("GET", url, params=querystring)
        response = response.json()
        stock_details = stock_details + response["data"]
    context["stock_data"] = stock_details
    return context


def all_crypto(request):
    crypto = []

    response = requests.get('https://api.coincap.io/v2/assets')
    for i in range(10):
        crypto = crypto + response.json()["data"]

    return render(request, 'index.html', {'allCrypto': crypto})
