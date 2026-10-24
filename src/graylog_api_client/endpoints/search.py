from ..data_structures import GraylogApiResult
from ..rest_adapter import RestAdapter
from typing import Literal


class Endpoint_SEARCH:
    # Graylog Endpoint for /search
    def __init__(self, rest_adapter: RestAdapter):
        self._rest_adapter = rest_adapter

    def post_search_query(self, query: str, start: int, timerange: dict, streams: list[str], stream_categories: list[str] | None = None,
                          sort: str | None = None, sort_order: Literal["Ascending", "Descending"] | None = None,
                          fields: list[str] | None = None, size: int = 50) -> GraylogApiResult:
        """Graylog API Route: POST /search/messages \n
        start replaces the "from" parameter in the API."""
        data = {
            "query": query,
            "from": str(start),
            "timerange": timerange,
            "streams": streams,
            "stream_categories": stream_categories,
            "sort": sort,
            "sort_order": sort_order,
            "fields": fields,
            "size": str(size),
        }
        result = self._rest_adapter.post("search/messages", data=data)
        return result
