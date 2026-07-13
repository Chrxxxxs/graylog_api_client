from typing import List, Dict


class GraylogApiResult:
    def __init__(self, status_code: int, message: str = "", data: List[Dict] = None):
        """Result returned from low-level RestAdapter

        :param status_code: Standard HTTP Status code
        :param message: Human readable result
        :param data: Python List of Dictionaries (or maybe just a single Dictionary on error)
        """
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data if data else []


# TODO make this a proper class
class GraylogTimerange:
    # Example relative:
    # { "type": "relative", "range": 300 }
    # Example absolute:
    # { "type": "absolute", "from": "2023-01-01T00:00:00.000Z", "to": "2023-01-02T00:00:00.000Z" }
    def relative(range: int):
        ...
    def absolute(from_time: str, to_time: str):
        ...