import logging
from typing import List, Union, Dict

from .rest_adapter import RestAdapter
from .data_structures import GraylogApiResult


class GraylogAPI:
    def __init__(self, host: str, api_key: str, ssl_verify: Union[str, bool] = True, logger: logging.Logger = None):
        """GraylogAPI client

        :param host: The hostname of the Graylog API endpoint plus the protocol. Example: https://graylog.com/api
        :param api_key: An API Key to authenticate with Graylog
        :param ssl_verify: Enables or Disables TLS Certificate verification. For a custom certificate, this value must a path pointing to the certificate, defaults to True
        :param logger: The logger being used by the Adapter, will use a new one if none is given, defaults to None
        """
        self._rest_adapter = RestAdapter(host=host, api_key=api_key, ssl_verify=ssl_verify, logger=logger)

    # The endpoints grouped like they are in the api-browser
    # /authz Authorization
    def get_auth_grants_overview(self) -> GraylogApiResult:
        overview = self._rest_adapter.get("authz/grants-overview")
        return overview

    def get_auth_roles(self, parameters: Dict = None) -> GraylogApiResult:
        roles = self._rest_adapter.get("authz/roles", parameters)
        return roles

    def get_auth_roles_of_user(self, username: str, parameters: Dict = None) -> GraylogApiResult:
        roles = self._rest_adapter.get(f"authz/roles/user/{username}", parameters)
        return roles

    def get_auth_role_by_id(self, role_id: str) -> GraylogApiResult:
        roles = self._rest_adapter.get(f"authz/roles/{role_id}")
        return roles

    def get_auth_assignees_of_role(self, role_id: str, parameters: Dict = None) -> GraylogApiResult:
        assignees = self._rest_adapter.get(f"authz/roles/{role_id}/assignees", parameters)
        return assignees

    # /ca
    def get_ca(self) -> GraylogApiResult:
        result = self._rest_adapter.get("ca")
        return result

    # /certificates
    def get_certificates(self) -> GraylogApiResult:
        result = self._rest_adapter.get("certificates")
        return result

    # /cluster
    def get_cluster(self) -> GraylogApiResult:
        result = self._rest_adapter.get("cluster")
        return result

    def get_processbufferdump(self, node_id: str = "") -> GraylogApiResult:
        result = self._rest_adapter.get(f"cluster/{node_id}/processbufferdump".replace("//", "/"))
        return result

    def get_jvminfo(self, node_id: str) -> GraylogApiResult:
        result = self._rest_adapter.get(f"cluster/{node_id}/jvm")
        return result

    # /contentstream
    # /dashboards
    # /datanodes
    # /datanode
    # /api-docs API-Documentation
    # /enterprise
    # /entitylists
    # /entity_scopes
    # /entity_suggestions
    # /events
    # /system/inputs/{inputId}/extractors Extractors
    # /favorites
    # /views/fields FieldTypes
    # /system/indexer Indexer
    # /search/universal/absolute Legacy Message Search
    # /messages
    # /migration
    # /system/pipelines Pipelines
    # /plugins
    # /remote-reindex-migration
    # /roles
    # /views/search Search
    # /search Search Options (Decorators, Export, Functions etc.)
    # /views/searchjobs Searchjobs
    # /sidecars
    # /sidecar
    # /startpage
    # /system/inputs/{inputId}/staticfields Staticfields
    # /streams
    def get_streams(self) -> GraylogApiResult:
        result = self._rest_adapter.get("streams")
        return result

    # /system Main System endpoints
    # /telemetry
    # /token_usage
    # /users
    def create_user(self, username: str, first_name: str, last_name: str, email: str, password: str, permissions: List[str], data: Dict = None) -> GraylogApiResult:
        user_data = {
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
        }
        if permissions:
            user_data["permissions"] = permissions
        if data:
            user_data.update(data)
        result = self._rest_adapter.post("users", data=user_data)
        return result

    def get_users(self, parameters: Dict = None) -> GraylogApiResult:
        result = self._rest_adapter.get("users", parameters)
        return result

    def get_users_paginated(self, parameters: Dict = None) -> GraylogApiResult:
        result = self._rest_adapter.get("users/paginated", parameters)
        return result

    def get_user_by_id(self, user_id: str) -> GraylogApiResult:
        result = self._rest_adapter.get(f"users/id/{user_id}")
        return result

    def get_user_by_username(self, username: str) -> GraylogApiResult:
        result = self._rest_adapter.get(f"users/{username}")
        return result

    def get_user_tokens_by_id(self, user_id: str) -> GraylogApiResult:
        result = self._rest_adapter.get(f"users/{user_id}/tokens")
        return result

    def delete_user_by_id(self, user_id: str) -> GraylogApiResult:
        result = self._rest_adapter.delete(f"users/id/{user_id}")
        return result

    def delete_user_by_username(self, username: str) -> GraylogApiResult:
        result = self._rest_adapter.delete(f"users/{username}")
        return result

    def change_user_status(self, user_id: str, status: str) -> GraylogApiResult:
        if status not in ["enabled", "disabled", "deleted"]:
            raise ValueError(f"Status must be either 'enabled', 'disabled' or 'deleted' but was: {status}")
        result = self._rest_adapter.put(f"users/{user_id}/status/{status}")
        return result

    # /views Main Views Endpoints
    def get_views(self, parameters: Dict = None) -> GraylogApiResult:
        result = self._rest_adapter.get("views", parameters)
        return result

    def get_view_by_id(self, view_id: str) -> GraylogApiResult:
        result = self._rest_adapter.get(f"views/{view_id}")
        return result
