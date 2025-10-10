import requests
import logging
from typing import Dict, Union

from src.graylog_api_client.exceptions import GraylogApiException
from src.graylog_api_client.data_structures import GraylogApiResult


class RestAdapter:
    def __init__(self, host: str, api_key: str, ssl_verify: Union[str, bool] = True, logger: logging.Logger = None):
        """Constructor for RestAdapter

        :param host: The hostname of the Graylog API endpoint plus the protocol. Example: https://graylog.com/api
        :param api_key: An API Key to authenticate with Graylog
        :param ssl_verify: Enables or Disables TLS Certificate verification. For a custom certificate, this value must a path pointing to the certificate, defaults to True
        :param logger: The logger being used by the Adapter, will use a new one if none is given, defaults to None
        """
        self._logger = logger or logging.getLogger(__name__)
        self.host = host + "/"
        self._api_key = api_key
        self._ssl_verify = ssl_verify
        self._session = requests.Session()
        self._session.headers.update({"Accept": "application/json"})
        self._session.auth = (self._api_key, "token")  # Graylog uses the format Basic Auth: "<API-token>:token"
        if not ssl_verify:
            requests.packages.urllib3.disable_warnings()

    def _do(self, method: str, endpoint: str, parameters: Dict = None, data: Dict = None) -> GraylogApiResult:
        """Run the HTTP Requests.

        :param method: The HTTP Method that this request will use.
        :param endpoint: The API endpoint that this request goes to. Example: /streams.
        :param parameters: Dictionary to be sent in the query string of the Request.
        :param data: Dictionary to be sent in the body of the Request.
        :raises GraylogApiException: Generic Exception for Errors caused within the Adapter.
        :return: An object containing the Result of the API request.
        """
        url = self.host + endpoint
        log_line_pre = f"method={method}, url={url}, parameters={parameters}"
        log_line_post = ', '.join((log_line_pre, "success={}, status_code={}, message={}"))
        try:
            self._logger.debug(msg=log_line_pre)
            response = self._session.request(method=method, url=url, verify=self._ssl_verify, params=parameters, json=data)
        except requests.exceptions.RequestException as e:
            self._logger.error(msg=str(e))
            raise GraylogApiException("Invalid API Response") from e
        try:
            data = response.json()
        except (ValueError, requests.exceptions.JSONDecodeError) as e:
            self._logger.error(msg=log_line_post.format(False, None, e))
            raise GraylogApiException("Bad JSON in response") from e
        is_success = 299 >= response.status_code >= 200  # OK
        log_line = log_line_post.format(is_success, response.status_code, response.reason)
        if is_success:
            self._logger.debug(msg=log_line)
            return GraylogApiResult(status_code=response.status_code, message=response.reason, data=data)
        self._logger.error(msg=log_line)
        raise GraylogApiException(f"{response.status_code}: {response.reason}")

    def get(self, endpoint: str, parameters: Dict = None) -> GraylogApiResult:
        """Send a GET request to the API.

        :param endpoint: The API endpoint that this request goes to. Example: /streams.
        :param parameters: Dictionary to be sent in the query string of the Request.
        :return: An object containing the Result of the API request.
        """
        return self._do(method="GET", endpoint=endpoint, parameters=parameters)

    def post(self, endpoint: str, parameters: Dict = None, data: Dict = None) -> GraylogApiResult:
        """Send a POST request to the API.

        :param endpoint: The API endpoint that this request goes to. Example: /streams.
        :param parameters: Dictionary to be sent in the query string of the Request.
        :param data: Dictionary to be sent in the body of the Request.
        :return: An object containing the Result of the API request.
        """
        return self._do(method="POST", endpoint=endpoint, parameters=parameters, data=data)

    def delete(self, endpoint: str, parameters: Dict = None, data: Dict = None) -> GraylogApiResult:
        """Send a DELETE request to the API.

        :param endpoint: The API endpoint that this request goes to. Example: /streams.
        :param parameters: Dictionary to be sent in the query string of the Request.
        :param data: Dictionary to be sent in the body of the Request.
        :return: An object containing the Result of the API request.
        """
        return self._do(method="DELETE", endpoint=endpoint, parameters=parameters, data=data)

    def put(self, endpoint: str, parameters: Dict = None, data: Dict = None) -> GraylogApiResult:
        """Send a PUT request to the API.

        :param endpoint: The API endpoint that this request goes to. Example: /streams.
        :param parameters: Dictionary to be sent in the query string of the Request.
        :param data: Dictionary to be sent in the body of the Request.
        :return: An object containing the Result of the API request.
        """
        return self._do(method="PUT", endpoint=endpoint, parameters=parameters, data=data)
