from unittest import TestCase

from currency import get_currency


class GetCurrencyTestCase(TestCase):
    def test_one_dollar_rate(self):
        one_dollar_rate = get_currency(1)
        self.assertEqual(one_dollar_rate, 73.48)

    def test_ten_dollar_rate(self):
        one_dollar_rate = get_currency(10)
        self.assertEqual(one_dollar_rate, 734.8)


