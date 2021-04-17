import requests
from bs4 import BeautifulSoup as bs

# getting the company
def get_symbol(cmp_name):
    try:
        url = "https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch" # use placeholders where MSFT is, to fetch price from yahoo finance

        response = requests.get(url)

        soup = bs(response.content, 'html.parser')
        print(soup.div['D(ib) Mend(20px)'])
    except NameError as error:
        print("Error while trying to get data")


"""
def get_price(cmp_symbol):
    try:
        url = ("https://eodhistoricaldata.com/api/eod/{}?api_token=60754dbc9be494.79866025&fmt=json").format(cmp_symbol)

        response = requests.get(url).json()

        print(response)
    except requests.HTTPError as error:
        print("Error while trying to get the price")
    


get_price("MSFT")"""

get_symbol("Microsoft")