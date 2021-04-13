import requests


# getting company symbol
def get_symbol(cmp_name):

    try:
        url = ('https://finnhub.io/api/v1/search?q={}&token=c1phgr2ad3id1hoq14pg').format(cmp_name)

        response = requests.get(url)

    except requests.HTTPError as error:
        print("there was an error while trying to get company symbol")


    # returning symbol for func get_price
    return response.json()['result'][0]['symbol']


def get_price(company):
    try:

        cmp_symbol = get_symbol(company)
        print(cmp_symbol)

        """
        url = ("https://finnhub.io/api/v1/quote?symbol={}&token=c1phgr2ad3id1hoq14pg").format(cmp_symbol)

        response = requests.get(url)

        print(response)"""
    except requests.HTTPError as error:
        print("Error while trying to get the price")
    


get_price("microsoft")