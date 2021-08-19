import re
import urllib.request
from unittest import TestCase

from currency import get_currency


class GetCurrencyTestCase(TestCase):
    def setUp(self):
        response =urllib.request.urlopen('http://www.finmarket.ru/currency/rates/').read()
        rate = re.findall(b'<div class="value">(\d+(?:\,\d+)?)</div>', response)[0]
        self.formatted_rate = round(float(rate.decode('utf8').replace(',', '.')), 2)

    def test_one_dollar_rate(self):
        one_dollar_function_rate = round(get_currency(1), 2)
        self.assertEqual(one_dollar_function_rate, self.formatted_rate)

    def test_ten_dollar_rate(self):
        ten_dollar_function_rate = get_currency(10)
        checking_rate = round(10*self.formatted_rate, 2)
        self.assertEqual(ten_dollar_function_rate, checking_rate)


