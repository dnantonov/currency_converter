import logging
import re
import sys
import urllib.request

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def get_currency(dollars):
    logging.info(f'Converting {dollars}$ in rubles...')
    response = urllib.request.urlopen('https://www.banki.ru/products/currency/usd/').read()
    rate = re.findall(b'<div class="currency-table__large-text">(\d+(?:\,\d+)?)</div>', response)[0]
    formatted_rate = rate.decode('utf8').replace(',', '.')
    logging.info(f'Dollar rate in rubles: {formatted_rate}$')
    result_in_rubles = round(float(formatted_rate) * dollars, 2)
    logging.info(f'{dollars}$ will be {result_in_rubles}₽ in rubles')
    return result_in_rubles
