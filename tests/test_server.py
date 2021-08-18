import json
from unittest import TestCase

import requests


class TestServerTestCase(TestCase):
    def setUp(self):
        self.url = 'http://localhost:8000'

    def test_get(self):
        status_code = requests.get(self.url).status_code
        self.assertEqual(status_code, 200)
        response = requests.get(self.url).content.decode('utf8')
        json_data = response.replace("\r", "") .split('\n')[-1]
        dict_data = json.loads(json_data)
        self.assertEqual(dict_data["amount"], 1)
        self.assertEqual(dict_data["rubles"], 73.48)
        self.assertEqual(dict_data["currency"], 'USD')


