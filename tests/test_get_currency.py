import re
from unittest import TestCase

import requests

from currency import get_currency


class GetCurrencyTestCase(TestCase):
    def setUp(self):
        response = requests.get('http://www.finmarket.ru/currency/rates/')
        rate = re.findall(b'<div class="value">(\d+(?:\,\d+)?)</div>', response.content)[0]
        self.formatted_rate = round(float(rate.decode('utf8').replace(',', '.')), 2)

    def test_one_dollar_rate(self):
        one_dollar_function_rate = round(get_currency(1), 2)
        self.assertEqual(one_dollar_function_rate, self.formatted_rate)

    def test_ten_dollar_rate(self):
        ten_dollar_function_rate = get_currency(10)
        checking_rate = round(10*self.formatted_rate, 2)
        self.assertEqual(ten_dollar_function_rate, checking_rate)


