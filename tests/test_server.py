import json
import urllib
import urllib.request
from unittest import TestCase
from currency import get_currency


class TestServerTestCase(TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:8000'

    def test_get(self):
        status_code = urllib.request.urlopen(self.url).getcode()
        self.assertEqual(status_code, 200)
        response = urllib.request.urlopen(self.url).read().decode('utf8')
        json_data = response.split('\n')[-1]
        dict_data = json.loads(json_data)
        current_usd_rate = get_currency(1)
        self.assertEqual(dict_data["amount"], 1)
        self.assertEqual(dict_data["rubles"], current_usd_rate)
        self.assertEqual(dict_data["currency"], 'USD')

    def test_post(self):
        request = urllib.request.Request(self.url)
        request.add_header('Content-Type', 'application/json; charset=utf-8')
        jsondata = json.dumps({"amount": 20})
        json_data_as_bytes = jsondata.encode('utf-8')  # needs to be bytes
        request.add_header('Content-Length', len(json_data_as_bytes))
        response = urllib.request.urlopen(request, json_data_as_bytes)
        self.assertEqual(response.getcode(), 200)
        dict_json_data = response.read().decode('utf8').split('\n')[-1]
        dict_data = json.loads(dict_json_data)
        twenty_dollars = get_currency(20)
        self.assertEqual(dict_data["amount"], 20)
        self.assertEqual(dict_data["rubles"], twenty_dollars)
        self.assertEqual(dict_data["currency"], 'USD')


