from ..data_structures import GraylogApiResult
from ..rest_adapter import RestAdapter


class Endpoint_VIEWS:
    # Graylog Endpoint for /views
    def __init__(self, rest_adapter: RestAdapter):
        self._rest_adapter = rest_adapter

    def get_views(self, parameters: dict | None = None) -> GraylogApiResult:
        """Graylog API Route: GET /views"""
        result = self._rest_adapter.get("views", parameters)
        return result

    def get_view_by_id(self, view_id: str) -> GraylogApiResult:
        """Graylog API Route: GET /views/{view_id}"""
        result = self._rest_adapter.get(f"views/{view_id}")
        return result
