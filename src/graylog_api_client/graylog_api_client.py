import logging
from typing import Literal
from warnings import deprecated

from .rest_adapter import RestAdapter
from .data_structures import GraylogApiResult
from .endpoints import Plugins, Endpoint_AUTH, Endpoint_SEARCH, Endpoint_USER, Endpoint_VIEWS


class GraylogAPI:
    def __init__(self, host: str, api_key: str, ssl_verify: str | bool = True, logger: logging.Logger | None = None):
        """GraylogAPI client

        :param host: The hostname of the Graylog API endpoint plus the protocol. Example: https://graylog.com/api
        :param api_key: An API Key to authenticate with Graylog
        :param ssl_verify: Enables or Disables TLS Certificate verification. For a custom certificate, this value must a path pointing to the certificate, defaults to True
        :param logger: The logger being used by the Adapter, will use a new one if none is given, defaults to None
        """
        self._rest_adapter = RestAdapter(host=host, api_key=api_key, ssl_verify=ssl_verify, logger=logger)
        self.plugins = Plugins(rest_adapter=self._rest_adapter)
        self.authz = Endpoint_AUTH(rest_adapter=self._rest_adapter)
        self.users = Endpoint_USER(rest_adapter=self._rest_adapter)
        self.views = Endpoint_VIEWS(rest_adapter=self._rest_adapter)
        self.search = Endpoint_SEARCH(rest_adapter=self._rest_adapter)

    # The endpoints grouped like they are in the api-browser
    # /authz Authorization
    @deprecated("This method is deprecated and will be removed in a future version. Use the 'authz' attribute instead.")
    def get_auth_grants_overview(self) -> GraylogApiResult:
        overview = self.authz.get_grants_overview()
        return overview

    @deprecated("This method is deprecated and will be removed in a future version. Use the 'authz' attribute instead.")
    def get_auth_roles(self, parameters: dict | None = None) -> GraylogApiResult:
        roles = self.authz.get_roles(parameters)
        return roles

    @deprecated("This method is deprecated and will be removed in a future version. Use the 'authz' attribute instead.")
    def get_auth_roles_of_user(self, username: str, parameters: dict | None = None) -> GraylogApiResult:
        roles = self.authz.get_roles_of_user(username, parameters)
        return roles

    @deprecated("This method is deprecated and will be removed in a future version. Use the 'authz' attribute instead.")
    def get_auth_role_by_id(self, role_id: str) -> GraylogApiResult:
        roles = self.authz.get_role_by_id(role_id)
        return roles

    @deprecated("This method is deprecated and will be removed in a future version. Use the 'authz' attribute instead.")
    def get_auth_assignees_of_role(self, role_id: str, parameters: dict | None = None) -> GraylogApiResult:
        assignees = self.authz.get_assignees_of_role(role_id, parameters)
        return assignees

    # /search Search Options (Decorators, Export, Functions etc.)
    @deprecated("This method is deprecated and will be removed in a future version. Use the 'search' attribute instead.")
    def post_search_query(self, query: str, start: int, timerange: dict, streams: list[str], stream_categories: list[str] | None = None,
                          sort: str | None = None, sort_order: Literal["Ascending", "Descending"] | None = None,
                          fields: list[str] | None = None, size: int = 50) -> GraylogApiResult:
        """start replaces the "from" parameter in the API"""
        result = self.search.post_search_query(query, start, timerange, streams, stream_categories, sort, sort_order, fields, size)
        return result

    # /streams
    @deprecated("This method is deprecated by Graylog and will not work with future Graylog versions")
    def get_streams(self) -> GraylogApiResult:
        result = self._rest_adapter.get("streams")
        return result

    # /users
    @deprecated("This method is deprecated and will be removed in a future version. Use the 'users' attribute instead.")
    def create_user(self, username: str, first_name: str, last_name: str, email: str, password: str, permissions: list[str], data: dict | None = None) -> GraylogApiResult:
        result = self.users.create_user(username, first_name, last_name, email, password, permissions, data)
        return result

    @deprecated("This method is deprecated and will be removed in a future version. Use the 'users' attribute instead.")
    def get_users(self, parameters: dict | None = None) -> GraylogApiResult:
        result = self.users.get_users(parameters)
        return result

    @deprecated("This method is deprecated and will be removed in a future version. Use the 'users' attribute instead.")
    def get_users_paginated(self, parameters: dict | None = None) -> GraylogApiResult:
        result = self.users.get_users_paginated(parameters)
        return result

    @deprecated("This method is deprecated and will be removed in a future version. Use the 'users' attribute instead.")
    def get_user_by_id(self, user_id: str) -> GraylogApiResult:
        result = self.users.get_user_by_id(user_id)
        return result

    @deprecated("This method is deprecated and will be removed in a future version. Use the 'users' attribute instead.")
    def get_user_by_username(self, username: str) -> GraylogApiResult:
        result = self.users.get_user_by_username(username)
        return result

    @deprecated("This method is deprecated and will be removed in a future version. Use the 'users' attribute instead.")
    def get_user_tokens_by_id(self, user_id: str) -> GraylogApiResult:
        result = self.users.get_user_tokens_by_id(user_id)
        return result

    @deprecated("This method is deprecated and will be removed in a future version. Use the 'users' attribute instead.")
    def delete_user_by_id(self, user_id: str) -> GraylogApiResult:
        result = self.users.delete_user_by_id(user_id)
        return result

    @deprecated("This method is deprecated and will be removed in a future version. Use the 'users' attribute instead.")
    def delete_user_by_username(self, username: str) -> GraylogApiResult:
        result = self.users.delete_user_by_username(username)
        return result

    @deprecated("This method is deprecated and will be removed in a future version. Use the 'users' attribute instead.")
    def change_user_status(self, user_id: str, status: str) -> GraylogApiResult:
        result = self.users.change_user_status(user_id, status)
        return result

    # /views Main Views Endpoints
    @deprecated("This method is deprecated and will be removed in a future version. Use the 'views' attribute instead.")
    def get_views(self, parameters: dict | None = None) -> GraylogApiResult:
        result = self.views.get_views(parameters)
        return result

    @deprecated("This method is deprecated and will be removed in a future version. Use the 'views' attribute instead.")
    def get_view_by_id(self, view_id: str) -> GraylogApiResult:
        result = self.views.get_view_by_id(view_id)
        return result
