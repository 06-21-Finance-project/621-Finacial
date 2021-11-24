from django.shortcuts import render
import requests


def index(request):
    return


def all_crypto(request):
    crypto = []

    response = requests.get('https://api.coincap.io/v2/assets')
    for i in range(10):
        crypto = crypto + response.json()["data"]

    return render(request, 'index.html', {'allCrypto': crypto})