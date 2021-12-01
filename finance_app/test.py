from datetime import datetime

import requests

if __name__ == '__main__':
    crypto_response = requests.get(f'https://newsapi.org/v2/everything?q=bitcoin&2021-12-01&sortBy=publishedAt&'
                                   'apiKey=a292184125094d328398eaa6c0a624b1').json()

    time_c = 1
    crypto_news = []


    for i in crypto_response["articles"]:
        if time_c <= 10:
            time_c += 1
            t_in = i["publishedAt"]
            print("t in: " + t_in)
            t_out = datetime.strptime(t_in[0:19], "%Y-%m-%dT%H:%M:%S")
            print("t out: " + str(t_out))
            i["publishedAt"] = t_out
            crypto_news.append(i)