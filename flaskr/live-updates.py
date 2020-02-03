from bs4 import BeautifulSoup
import requests
import csv
import time

url_ftse = 'https://uk.finance.yahoo.com/quote/%5EFTSE?p=^FTSE'
url_bitcoin = 'https://uk.finance.yahoo.com/quote/BTC-GBP?p=BTC-GBP'
url_gspc = 'https://uk.finance.yahoo.com/quote/%5EGSPC?p=%5EGSPC'
url_ixic = 'https://uk.finance.yahoo.com/quote/%5EIXIC?p=%5EIXIC'
live_ftse = None
f = None


# retrieving price of the FTSE 100 from the Yahoo finance website
def ftse_price(url):
    global f
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    price_ftse = soup.find("span", {"class": "Trsdu(0.3s)"}).text
    price_ftse = price_ftse.replace(",", "")
    f = csv.writer(open('live-ftse.txt', 'w'))
    f.writerow(['Price'])
    return float(price_ftse), f


# This continuously runs te ftse_price function to give a live price
def live_ftse_price():
    global live_ftse
    while True:
        live_ftse = ftse_price(url_ftse)
        return live_ftse


def bitcoin_price(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    price_bitcoin = soup.find("span", {"class": "Trsdu(0.3s)"}).text
    price_bitcoin = price_bitcoin.replace(",", "")
    return float(price_bitcoin)


def live_bitcoin_price():
    while True:
        live_bitcoin = bitcoin_price(url_bitcoin)
        print("bitcoin price:", live_bitcoin)


def GSPC_price(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    price_gspc = soup.find("span", {"class": "Trsdu(0.3s)"}).text
    price_gspc = price_gspc.replace(",", "")
    return float(price_gspc)


def live_GSPC_price():
    while True:
        live_gspc = GSPC_price(url_gspc)
        print(" S&P 500 price:", live_gspc)


def ixic_price(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    price_IXIC = soup.find("span", {"class": "Trsdu(0.3s)"}).text
    price_IXIC = price_IXIC.replace(",", "")
    return float(price_IXIC)


def live_ixic_price():
    while True:
        live_ixic = ixic_price(url_ixic)
        print(" NASDAQ price:", live_ixic)


# main code


# print(live_bitcoin_price())
# print(live_GSPC_price())
# print(live_ixic_price())

live_ftse_price()
f.writerow([live_ftse])



