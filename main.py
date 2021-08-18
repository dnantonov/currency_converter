import logging
import sys
import requests
from bs4 import BeautifulSoup

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def get_currency():
    logging.info('Scrape rate data started')
    url = 'https://www.vbr.ru/banki/kurs-valut/prodaja-usd/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    rate = soup.find(id='value_0').text
    logging.info(f'Dollar rate: {rate}$')
    logging.info('Data has been scraped')


if __name__ == '__main__':
    get_currency()
