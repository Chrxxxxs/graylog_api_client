from ...rest_adapter import RestAdapter
from .SecurityApp import SecurityApp

class Plugins:
    def __init__(self, rest_adapter: RestAdapter):
        self._rest_adapter = rest_adapter
        self.SecurityApp = SecurityApp(rest_adapter)