import logging
from typing import Union, Dict
from src.graylog_api_client.rest_adapter import RestAdapter
from src.graylog_api_client.data_structures import GraylogApiResult


class GraylogAPI:
    def __init__(self, host: str, api_key: str, ssl_verify: Union[str, bool] = True, logger: logging.Logger = None):
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

    # /views Main Views Endpoints
    def get_views(self, parameters: Dict = None) -> GraylogApiResult:
        result = self._rest_adapter.get("views", parameters)
        return result

    def get_view_by_id(self, view_id: str) -> GraylogApiResult:
        result = self._rest_adapter.get(f"views/{view_id}")
        return result
