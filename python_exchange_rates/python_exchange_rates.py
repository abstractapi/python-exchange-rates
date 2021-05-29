from python_core import HttpEndpoint
from collections import namedtuple

class AbstractExchangeRates:
    api_key = None
    endpoint_subdomain = 'exchange-rates'
    global_req_params = {
        'lang' : 'python'
    }

    @staticmethod
    def configure(api_key):
        AbstractExchangeRates.api_key = api_key

    @staticmethod
    def live(base, target=""):

        http_endpoint = HttpEndpoint(
            endpoint_subdomain=AbstractExchangeRates.endpoint_subdomain,
            global_req_params=AbstractExchangeRates.global_req_params,
            path='live/'
        )

        if AbstractExchangeRates.api_key is None:
            exception_type = "APINotConfiguredException"
            exception_msg = "Can't use the endpoint unless it's configured, use configure(api_key)"
            raise Exception(
                "[{}] : {}".format(exception_type, exception_msg)
            )

        try:
            req_params = {
                "api_key" : AbstractExchangeRates.api_key,
                "base" : base
            }

            if target != "":
                req_params['target'] = target

            response = http_endpoint.get(
                req_params=req_params
            )
            # Convert the dict to an object
            for key in response:
                if (type(response[key]) == dict):
                    EmbeddedObject = namedtuple('EmbeddedObject', response[key])
                    embedded_obj = EmbeddedObject(**response[key])
                    response[key] = embedded_obj
            ResponseObject = namedtuple('ResponseObject', response.keys())
            response_obj = ResponseObject(**response)
            return response_obj

        except Exception as e:
            # HttpEndpoint has expressive exceptions
            raise SystemExit(e)

    @staticmethod
    def historical(base, date, target=""):

        http_endpoint = HttpEndpoint(
            endpoint_subdomain=AbstractExchangeRates.endpoint_subdomain,
            global_req_params=AbstractExchangeRates.global_req_params,
            path='historical/'
        )

        if AbstractExchangeRates.api_key is None:
            exception_type = "APINotConfiguredException"
            exception_msg = "Can't use the endpoint unless it's configured, use configure(api_key)"
            raise Exception(
                "[{}] : {}".format(exception_type, exception_msg)
            )

        try:
            req_params = {
                "api_key" : AbstractExchangeRates.api_key,
                "base" : base,
                "date" : date
            }

            if target != "":
                req_params['target'] = target

            response = http_endpoint.get(
                req_params=req_params
            )
            # Convert the dict to an object
            for key in response:
                if (type(response[key]) == dict):
                    EmbeddedObject = namedtuple('EmbeddedObject', response[key])
                    embedded_obj = EmbeddedObject(**response[key])
                    response[key] = embedded_obj
            ResponseObject = namedtuple('ResponseObject', response.keys())
            response_obj = ResponseObject(**response)
            return response_obj

        except Exception as e:
            # HttpEndpoint has expressive exceptions
            raise SystemExit(e)

    @staticmethod
    def convert(base, target, date="", base_amount=""):

        http_endpoint = HttpEndpoint(
            endpoint_subdomain=AbstractExchangeRates.endpoint_subdomain,
            global_req_params=AbstractExchangeRates.global_req_params,
            path='convert/'
        )

        if AbstractExchangeRates.api_key is None:
            exception_type = "APINotConfiguredException"
            exception_msg = "Can't use the endpoint unless it's configured, use configure(api_key)"
            raise Exception(
                "[{}] : {}".format(exception_type, exception_msg)
            )

        try:
            req_params = {
                "api_key" : AbstractExchangeRates.api_key,
                "base" : base,
                "target" : target
            }

            if date != "":
                req_params['date'] = date

            if base_amount != "":
                req_params['base_amount'] = base_amount

            response = http_endpoint.get(
                req_params=req_params
            )
            # Convert the dict to an object
            for key in response:
                if (type(response[key]) == dict):
                    EmbeddedObject = namedtuple('EmbeddedObject', response[key])
                    embedded_obj = EmbeddedObject(**response[key])
                    response[key] = embedded_obj
            ResponseObject = namedtuple('ResponseObject', response.keys())
            response_obj = ResponseObject(**response)
            return response_obj

        except Exception as e:
            # HttpEndpoint has expressive exceptions
            raise SystemExit(e)
