# AbstractAPI python-exchange-rates library

Integrate the powerful [Exchange Rates API from Abstract](https://www.abstractapi.com/exchange-rate-api) in your Python project in a few lines of code.

The Exchange Rate API is an REST API that allows you to:

- look up the latest exchange rates for 80+ currencies via the *live* endpoint
- get historical exchange rates using the *historical* endpoint
- convert an arbitrary amount from one currency to another using the *convert* endpoint

It's very simple to use: you only need to submit your API key and a currency symbol (such as "USD"), and the API will respond with current exchange rate, historical data, or convertion rates.


# Documentation

## Supported Python Versions

This library supports the **Python version 3.6** and higher.

## Installation

You can install **python-exchange-rates** via PyPi or by downloading the source.

### Via PyPi:

**python-exchange-rates** is available on PyPi as the
[`abstract-python-exchange-rates`](https://pypi.org/project/abstract-python-exchange-rates/) package:

```bash
pip install abstract-python-exchange-rates
```

## API key

Get your API key for free and without hassle from the [Abstact website](https://app.abstractapi.com/users/signup?target=/api/exchange-rates/pricing/select).

## Quickstart

### Get exchange rates

```python
import pprint
from python_exchange_rates import AbstractExchangeRates

EXCHANGE_RATES_API_KEY =  "YYYYYY"; # Get your API Key from https://app.abstractapi.com/api/exchange-rates/documentation

AbstractExchangeRates.configure(EXCHANGE_RATES_API_KEY)

# Get live exchange rates using Abstract's Exchange Rates API and Python
response = AbstractExchangeRates.live("EUR")
pprint(response)

# Get historical exchange rates using Abstract's Exchange Rates API and Python
response = AbstractExchangeRates.historical('EUR', '2021-05-01');
pprint(response)

# Convert currency using Abstract's Exchange Rates API and Python
response = AbstractExchangeRates.convert('EUR', 'USD');
pprint(response)
```

## API response

The API response contains the following fields:

### `live` response parameters
| Parameter| Type| Details |
| - | - | - |
| base | String | The base currency used to get the exchange rates. |
| last_updated | String | The Unix timestamp of when the returned data was last updated. |
| exchange_rates | Object | A JSON Object containing each of the target currency as the key and its exchange rate versus the base currency as that key's value. |

### `historical` response parameters

| Parameter | Type | Details |
| - | - | - |
| base | String | The base currency used to get the exchange rates. |
| date | String | The date the currencies were pulled from, per the successful request. |
| exchange_rates | Object | A JSON Object containing each of the target currency as the key and its exchange rate versus the base currency as that key's value. |

### `convert` response parameters

| Parameter | Type | Details |
| - | - | - |
| base | String | The base currency used to get the exchange rates. |
| target | String | The target currency that the base_amount was converted into. |
| date | String | The date the currencies were pulled from, per the successful request. |
| base_amount | Float | The amount of the base currency from the request. |
| converted_amount | Float | The amount of the target currency that the base_amount has been converted into |
| exchange_rate | Float | The exchange rate used to convert the base_amount from the base currency to the target currency |

## Detailed documentation

You will find additional information and request examples in the [Abstract help page](https://app.abstractapi.com/api/exchange-rates/documentation).

## Getting help

If you need help installing or using the library, please contact [Abstract's Support](https://app.abstractapi.com/api/exchange-rates/support).

For bug report and feature suggestion, please use [this repository issues page](https://github.com/abstractapi/python-exchange-rates/issues).

# Contribution

Contributions are always welcome, as they improve the quality of the libraries we provide to the community.

Please provide your changes covered by the appropriate unit tests, and post them in the [pull requests page](https://github.com/abstractapi/python-exchange-rates/pulls).

## Setup

To install the requirements, run:

```bash
python3 setup.py install --user
```

Once you implementer all your changes and the unit tests, run the following command to run the tests:

```bash
EXCHANGE_RATES_API_KEY=YYYYYY python3 tests/test_python_exchange_rates.py
```
