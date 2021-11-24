import environ
from django.shortcuts import render
import requests

env = environ.Env()
environ.Env.read_env()

API_KEY = env('API_TOKEN')

def index(request):
    context = fetch_stocks(request)
    return render(request, 'index.html', context)

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
