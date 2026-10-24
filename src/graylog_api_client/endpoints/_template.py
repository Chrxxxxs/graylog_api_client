from ..data_structures import GraylogApiResult
from ..rest_adapter import RestAdapter


class Endpoint_TEMPLATE:
    # Graylog Endpoint for /template
    def __init__(self, rest_adapter: RestAdapter):
        self._rest_adapter = rest_adapter


# New Endpoints should be created using this template. The class name should be changed to the name of the endpoint, and the methods should be added as needed.
_ = GraylogApiResult  # This is a placeholder to avoid linter errors for unused imports.
