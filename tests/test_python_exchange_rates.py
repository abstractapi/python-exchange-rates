import unittest
import os, sys
import time

from python_exchange_rates import AbstractExchangeRates
from dotenv import load_dotenv

load_dotenv()

EXCHANGE_RATES_API_KEY = os.getenv('EXCHANGE_RATES_API_KEY')


class TestAbstractExchangeRates(unittest.TestCase):
    def __init__(self, *args, **kwargs):

        super(TestAbstractExchangeRates, self).__init__(*args, **kwargs)
        self.api = AbstractExchangeRates()

    def test_no_config(self):

        with self.assertRaises(Exception):
            # tests aren't always run in order, so make sure to
            # clear api_key
            AbstractExchangeRates.api_key = None
            AbstractExchangeRates.live("EUR")

    def test_live_response(self):

        AbstractExchangeRates.configure(EXCHANGE_RATES_API_KEY)
        response = AbstractExchangeRates.live("EUR")
        self.assertEqual(response.base, 'EUR')
        time.sleep(1)

    def test_historical_response(self):

        AbstractExchangeRates.configure(EXCHANGE_RATES_API_KEY)
        response = AbstractExchangeRates.historical("EUR", "2021-05-01")
        self.assertEqual(response.base, 'EUR')
        self.assertEqual(response.date, '2021-05-01')
        time.sleep(1)

    def test_convert_response(self):

        AbstractExchangeRates.configure(EXCHANGE_RATES_API_KEY)
        response = AbstractExchangeRates.convert("EUR", "USD")
        self.assertEqual(response.base, 'EUR')
        self.assertEqual(response.target, 'USD')
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()