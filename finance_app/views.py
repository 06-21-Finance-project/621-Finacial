from django.http import HttpResponse
from django.shortcuts import render
from time import sleep
from datetime import datetime
import requests


def index(request):
    input = datetime.now()
    today = input.strftime('%Y-%m-%d')
    # while True:
    bit_coin_news = requests.get(f'https://newsapi.org/v2/everything?q=bitcoin&from={today}&sortBy=publishedAt&'
                                 'apiKey=e4a078da3fc844f9a8cd5690e7c4a0f2').json
    stock_news = requests.get(f'https://newsapi.org/v2/everything?q=stock&from={today}&sortBy=publishedAt&'
                              'apiKey=e4a078da3fc844f9a8cd5690e7c4a0f2').json
    business_news = requests.get('https://newsapi.org/v2/everything?q=business&'
                                 f'from={today}&sortBy=publishedAt&apiKey=e4a078da3fc844f9a8cd5690e7c4a0f2').json

    return render(request, 'index.html', {'bit_coin_news': bit_coin_news, 'stock_news': stock_news,
                                             'business_news': business_news, 'today': today})
    # sleep()
