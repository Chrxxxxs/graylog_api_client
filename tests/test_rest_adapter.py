from unittest import TestCase, mock

import requests

from src.graylog_api_client.data_structures import GraylogApiResult
from src.graylog_api_client.exceptions import GraylogApiException
from src.graylog_api_client.rest_adapter import RestAdapter


class TestRestAdapter(TestCase):
    def setUp(self):
        self.rest_adapter = RestAdapter("", "")
        self.response = requests.Response()

    def test__do_good_request_returns_result(self):
        self.response.status_code = 200
        self.response._content = "{}".encode()
        with mock.patch("requests.Session.request", return_value=self.response):
            result = self.rest_adapter._do(method="GET", endpoint="/")
        self.assertIsInstance(result, GraylogApiResult)

    def test__do_bad_json_raises_GraylogApiException(self):
        invalid_json = b'{"invalid_json": '
        logger = mock.Mock()
        self.rest_adapter._logger = logger
        self.response._content = invalid_json
        with mock.patch("requests.Session.request", return_value=self.response):
            with self.assertRaises(GraylogApiException):
                self.rest_adapter._do(method="GET", endpoint="/")

    def test_get(self):
        self.rest_adapter._do = mock.Mock(spec=["method", "endpoint", "parameters"])
        self.rest_adapter.get(endpoint="/get", parameters={"foo": "bar"})
        assert self.rest_adapter._do.call_count == 1
        assert self.rest_adapter._do.call_args == mock.call(method="GET", endpoint="/get",
                                                            parameters={"foo": "bar"})

    def test_post(self):
        self.rest_adapter._do = mock.Mock(spec=["method", "endpoint", "parameters"])
        self.rest_adapter.post(endpoint="/post", parameters={"foo": "bar"}, data={"foo": "baz"})
        assert self.rest_adapter._do.call_count == 1
        assert self.rest_adapter._do.call_args == mock.call(method="POST", endpoint="/post",
                                                            parameters={"foo": "bar"}, data={"foo": "baz"})

    def test_delete(self):
        self.rest_adapter._do = mock.Mock(spec=["method", "endpoint", "parameters"])
        self.rest_adapter.delete(endpoint="/delete", parameters={"foo": "bar"}, data={"foo": "baz"})
        assert self.rest_adapter._do.call_count == 1
        assert self.rest_adapter._do.call_args == mock.call(method="DELETE", endpoint="/delete",
                                                            parameters={"foo": "bar"}, data={"foo": "baz"})

    def test_put(self):
        self.rest_adapter._do = mock.Mock(spec=["method", "endpoint", "parameters"])
        self.rest_adapter.put(endpoint="/put", parameters={"foo": "bar"}, data={"foo": "baz"})
        assert self.rest_adapter._do.call_count == 1
        assert self.rest_adapter._do.call_args == mock.call(method="PUT", endpoint="/put",
                                                            parameters={"foo": "bar"}, data={"foo": "baz"})
