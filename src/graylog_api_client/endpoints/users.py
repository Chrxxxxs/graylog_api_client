from ..data_structures import GraylogApiResult
from ..rest_adapter import RestAdapter
from warnings import deprecated


class Endpoint_USER:
    # Graylog Endpoint for /users
    def __init__(self, rest_adapter: RestAdapter):
        self._rest_adapter = rest_adapter

    def create_user(self, username: str, first_name: str, last_name: str, email: str, password: str, permissions: list[str], data: dict | None = None) -> GraylogApiResult:
        """Graylog API Route: POST /users"""
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

    @deprecated("This method is marked as deprecated by Graylog and will not work with future Graylog versions. Use the 'get_users_paginated' method instead.")
    def get_users(self, parameters: dict | None = None) -> GraylogApiResult:
        """Graylog API Route: GET /users"""
        result = self._rest_adapter.get("users", parameters)
        return result

    def get_users_paginated(self, parameters: dict | None = None) -> GraylogApiResult:
        """Graylog API Route: GET /users/paginated"""
        result = self._rest_adapter.get("users/paginated", parameters)
        return result

    def get_user_by_id(self, user_id: str) -> GraylogApiResult:
        """Graylog API Route: GET /users/id/{user_id}"""
        result = self._rest_adapter.get(f"users/id/{user_id}")
        return result

    def get_user_by_username(self, username: str) -> GraylogApiResult:
        """Graylog API Route: GET /users/{username}"""
        result = self._rest_adapter.get(f"users/{username}")
        return result

    def get_user_tokens_by_id(self, user_id: str) -> GraylogApiResult:
        """Graylog API Route: GET /users/{user_id}/tokens"""
        result = self._rest_adapter.get(f"users/{user_id}/tokens")
        return result

    def delete_user_by_id(self, user_id: str) -> GraylogApiResult:
        """Graylog API Route: DELETE /users/id/{user_id}"""
        result = self._rest_adapter.delete(f"users/id/{user_id}")
        return result

    def delete_user_by_username(self, username: str) -> GraylogApiResult:
        """Graylog API Route: DELETE /users/{username}"""
        result = self._rest_adapter.delete(f"users/{username}")
        return result

    def change_user_status(self, user_id: str, status: str) -> GraylogApiResult:
        """Graylog API Route: PUT /users/{user_id}/status/{status}"""
        if status not in ["enabled", "disabled", "deleted"]:
            raise ValueError(f"Status must be either 'enabled', 'disabled' or 'deleted' but was: {status}")
        result = self._rest_adapter.put(f"users/{user_id}/status/{status}")
        return result
