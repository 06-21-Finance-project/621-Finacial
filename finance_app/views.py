import environ
from django.shortcuts import render
import requests

env = environ.Env()
environ.Env.read_env()

API_KEY = env('API_TOKEN')

def index(request):
    context = fetch_news(request)
    return render(request, 'index.html', context)































def fetch_news(request):
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


