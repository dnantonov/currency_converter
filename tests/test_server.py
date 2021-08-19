import json
import requests
from unittest import TestCase
from currency import get_currency


class TestServerTestCase(TestCase):
    def setUp(self):
        self.url = 'http://localhost:8000'

    def test_get(self):
        status_code = requests.get(self.url).status_code
        self.assertEqual(status_code, 200)
        response = requests.get(self.url).content.decode('utf8')
        json_data = response.split('\n')[-1]
        dict_data = json.loads(json_data)
        current_usd_rate = get_currency(1)
        self.assertEqual(dict_data["amount"], 1)
        self.assertEqual(dict_data["rubles"], current_usd_rate)
        self.assertEqual(dict_data["currency"], 'USD')

    def test_post(self):
        status_code = requests.post(self.url, json={"amount": 20}).status_code
        self.assertEqual(status_code, 200)
        response = requests.post(self.url, json={"amount": 20}).content.decode('utf8')
        json_data = response.split('\n')[-1]
        dict_data = json.loads(json_data)
        twenty_dollars = get_currency(20)
        self.assertEqual(dict_data["amount"], 20)
        self.assertEqual(dict_data["rubles"], twenty_dollars)
        self.assertEqual(dict_data["currency"], 'USD')


