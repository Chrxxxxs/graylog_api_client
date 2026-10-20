from ..data_structures import GraylogApiResult
from ..rest_adapter import RestAdapter
from typing import Dict

class Endpoint_AUTH:
    def __init__(self, rest_adapter: RestAdapter):
        self._rest_adapter = rest_adapter

    def get_grants_overview(self) -> GraylogApiResult:
        overview = self._rest_adapter.get("authz/grants-overview")
        return overview

    def get_roles(self, parameters: Dict = None) -> GraylogApiResult:
        roles = self._rest_adapter.get("authz/roles", parameters)
        return roles

    def get_roles_of_user(self, username: str, parameters: Dict = None) -> GraylogApiResult:
        roles = self._rest_adapter.get(f"authz/roles/user/{username}", parameters)
        return roles

    def get_role_by_id(self, role_id: str) -> GraylogApiResult:
        roles = self._rest_adapter.get(f"authz/roles/{role_id}")
        return roles

    def get_assignees_of_role(self, role_id: str, parameters: Dict = None) -> GraylogApiResult:
        assignees = self._rest_adapter.get(f"authz/roles/{role_id}/assignees", parameters)
        return assignees