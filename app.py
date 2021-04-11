import requests

def get_price(company):
    try:
        url = ("https://finnhub.io/api/v1/quote?symbol={}&token=c1phgr2ad3id1hoq14pg").format(company)

        response = requests.get(url)

        print(response.text)
    except requests.HTTPError as error:
        print("Error while trying to get the price")


get_price("AAPL")