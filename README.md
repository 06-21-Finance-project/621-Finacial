# 621-Financial

## Project Overview

   In this modern-day, people have more interested in cryptocurrency and stock when compared to the past. The fact that they have a significant impact on the way people spend their money due to the risk of an investment that depends on people's decisions and data is terrifying. Moreover, we seek out a few websites that can effectively show the relation between news and the status of cryptocurrencies and stock. So, we came with a solution to solve this issue. Our web page will establish the relationship between the current events and the status of the stock market and cryptocurrencies, including the current investor trend(primary data), to guide the beginner investor on the right track.

<div align="right"> <b><a href="#top">↥ back to top</a></b> </div>

<br>

## Features

* Display the market price of stocks and cryptocurrencies only the attractive ones.
* Display the news of various categories in the same page as the price of stocks and cryptocurrencies.
* The information is paired by the time.
* Users are able to see the relations between the income, age, the money spend on stocks and cryptocurrencies, and their interests on stocks and cryptocurrencies.


<div align="right"> <b><a href="#top">↥ back to top</a></b> </div>

<br>

## Required Libraries and tools
* Django
    * Python 3.9
    * Django
    * django-environ
    * django_heroku
    * requests
*  Swagger
    * connexion[swagger-ui]
    * werkzeug
    * swagger-ui-bundle
    * python_dateutil
    * setuptools
    * Flask

<div align="right"> <b><a href="#top">↥ back to top</a></b> </div>

<br>


## Getting Started (Project Django)

In the project directory, you can run:

    $ pip install -r requirements.txt

For downloading all of the requirement you required for the web page.

    $ python manage.py runserver

Runs the app in the development mode.\
Open [http://localhost:8000](http://localhost:8000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.


<div align="right"> <b><a href="#top">↥ back to top</a></b> </div>

<br>

## Getting Started (Project Swagger)


In the project directory, you can run:

    $ java -jar openapi/openapi-generator-cli-5.3.0.jar generate -i openapi/621-financial-api.yaml -o autogen -g python-flask

To start the autogen (Requirement: openapi-generator-cli-5.3.0.jar), then you can run

    $ pip install -r requirements.txt

For downloading all of the requirement you required for the web page. After that you can run

    $ python app.py

To runs the app in the development mode.\
Open [http://localhost:8080/finance-api/v1/ui/#/](http://localhost:8080/finance-api/v1/ui/#/) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.


<div align="right"> <b><a href="#top">↥ back to top</a></b> </div>

<br>


## Team Members
| Name                     |                  GitHub ID                  |     Role      |    Faculty   |   University   |
| ------------------------ | :-----------------------------------------: | :-----------: |    :-----------:   |   :-----------:   |
| Teeranut Sawanyawat      |     [LevNut](https://github.com/LevNut)     |     Developer |   Software and Knowledge Engineer   |   Kasetsart University   |
| Metaras Charoenseang     |    [metaras](https://github.com/metaras)    |   Developer   |   Software and Knowledge Engineer   |   Kasetsart University   |
| Pattarin Wongwaipanich   |  [pattarinn](https://github.com/pattarinn)  |   Developer   |   Software and Knowledge Engineer   |   Kasetsart University   |

<div align="right"> <b><a href="#top">↥ back to top</a></b> </div>

<br>


## References
* [Primary Data](https://docs.google.com/spreadsheets/d/1yl4KlxzFLZDi_MFgiNc-iB2PT6uAG_pMEYbzb9aimOc/edit?usp=sharing)
* [Presentation Slide](https://docs.google.com/presentation/d/1bsEGp61wrR63aAOHyj-sWKr4lLTLm0frO6JYfUrbu8w/edit?usp=sharing)

<div align="right"> <b><a href="#top">↥ back to top</a></b> </div>

<br>

## License

Distributed under the MIT License. See `license.txt` for more information.

<div align="right"> <b><a href="#top">↥ back to top</a></b> </div>

<br>
