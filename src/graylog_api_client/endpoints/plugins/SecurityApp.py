from ...data_structures import GraylogApiResult
from ...rest_adapter import RestAdapter
from typing import Union, Dict
from datetime import datetime

class SecurityApp:
    def __init__(self, rest_adapter: RestAdapter):
        self._rest_adapter = rest_adapter
        self.Assets = Assets(rest_adapter)

class Assets:
    def __init__(self, rest_adapter: RestAdapter):
        self._rest_adapter = rest_adapter
    
    def get_assets(self, *, sort: str = "name", page: int = 1, per_page: int = 15, query: str = "",\
                               filters: str = "", direction: str = "asc") -> GraylogApiResult:
        parameters = {
            "sort": sort,
            "page": page,
            "per_page": per_page,
            "query": query,
            "filters": filters,
            "direction": direction,
        }
        result = self._rest_adapter.get("plugins/org.graylog.plugins.securityapp.asset/assets", parameters)
        return result
    
    # The API Browser is very confusing/wrong for creating assets
    def create_user_asset(
        self, *, name: str, usernames: list[str], user_ids: list[str] = [], email_addresses: list[str] = [], first_name: str = "", last_name: str = "", category: list[str] = [], priority: int = 1
    ) -> GraylogApiResult:
        """Create a user asset."""
        data = {
            "category": category,
            "details": {
                "type": "user",
                "usernames": usernames,
                "user_ids": user_ids,
                "email_addresses": email_addresses,
                "first_name": first_name,
                "last_name": last_name,
            },
            "name": name,
            "priority": priority,
        }
        result = self._rest_adapter.post("plugins/org.graylog.plugins.securityapp.asset/assets", data=data)
        return result
    
    def create_machine_asset(
        self, *, name: str, hostnames: list[str], ip_addresses: list[str] = [], mac_addresses: list[str] = [], category: list[str] = [], custom_fields: dict[str, str] = {},
        description: str = "", geo_info: dict[str, int|str] = {}, owner: str = "", priority: int = 1
    ) -> GraylogApiResult:
        """Create a machine asset."""
        data = {
            "category": category,
            "details": {
                "type": "machine",
                "hostnames": hostnames,
                "ip_addresses": ip_addresses,
                "mac_addresses": mac_addresses,
                "custom_fields": custom_fields,
                "description": description,
                "geo_info": geo_info,
                "owner": owner,
            },
            "name": name,
            "priority": priority,
        }
        result = self._rest_adapter.post("plugins/org.graylog.plugins.securityapp.asset/assets", data=data)
        return result
    
    def add_categories_to_multiple_assets(self, *, asset_ids: list[str], categories: list[str]) -> GraylogApiResult:
        # Untested
        data = {
            "asset_ids": asset_ids,
            "categories": categories,
        }
        result = self._rest_adapter.put("plugins/org.graylog.plugins.securityapp.asset/assets/bulk/categories_add", data=data)
        return result

    def get_asset_by_id_detailed(self, asset_id: str) -> GraylogApiResult:
        result = self._rest_adapter.get(
            f"plugins/org.graylog.plugins.securityapp.asset/assets/{asset_id}"
        )
        return result
    
    def edit_asset_by_id(self, asset_id: str, **updates) -> GraylogApiResult:
        """Edit the asset with the given ID by passing the updates as keyword arguments."""
        current_state = self.get_asset_by_id_detailed(asset_id)
        payload = current_state.data
        payload.update(updates)
        result = self._rest_adapter.put(
            f"plugins/org.graylog.plugins.securityapp.asset/assets/{asset_id}", data=payload
        )
        return result
    
    def delete_asset_by_id(self, asset_id: str) -> GraylogApiResult:
        result = self._rest_adapter.delete(
            f"plugins/org.graylog.plugins.securityapp.asset/assets/{asset_id}"
        )
        return result