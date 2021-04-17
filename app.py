import requests
from bs4 import BeautifulSoup as bs

# getting the company
def get_symbol(cmp_name):
    try:
        url = ("https://finance.yahoo.com/quote/{}?p={}&.tsrc=fin-srch").format(cmp_name, cmp_name) # use placeholders where MSFT is, to fetch price from yahoo finance

        response = requests.get(url)

        soup = bs(response.content, 'html.parser')
        # getting current price
        current_price = soup.find_all("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")[0].text
        print("Current price for ", cmp_name + " is ", current_price + "€")
    except Exception:
        print("That company doesnt exist")


# Input Company Symbol that is registered in the stock market
get_symbol("EDPR.LS")