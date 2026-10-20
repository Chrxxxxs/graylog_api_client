from unittest import TestCase, mock

from src.graylog_api_client.data_structures import GraylogApiResult
from src.graylog_api_client.graylog_api_client import GraylogAPI


class TestGraylogApiClient(TestCase):
    def setUp(self):
        self.graylog_api = GraylogAPI("", "")
        self.graylog_api._rest_adapter.get = mock.Mock(spec=["endpoint", "parameters"], return_value=GraylogApiResult(200))
        self.graylog_api._rest_adapter.post = mock.Mock(spec=["endpoint", "parameters", "data"], return_value=GraylogApiResult(200))
        self.graylog_api._rest_adapter.delete = mock.Mock(spec=["endpoint", "parameters", "data"], return_value=GraylogApiResult(200))
        self.graylog_api._rest_adapter.put = mock.Mock(spec=["endpoint", "parameters", "data"], return_value=GraylogApiResult(200))

    # The endpoints grouped like they are in the api-browser
    # /authz Authorization
    def test_get_auth_roles(self):
        roles = self.graylog_api.get_auth_roles()
        self.assertIsInstance(roles, GraylogApiResult)
        self.graylog_api._rest_adapter.get.assert_called_once_with("authz/roles", None)

    def test_get_auth_grants_overview(self):
        overview = self.graylog_api.get_auth_grants_overview()
        self.assertIsInstance(overview, GraylogApiResult)
        self.graylog_api._rest_adapter.get.assert_called_once_with("authz/grants-overview")

    def test_get_auth_roles_of_user(self):
        dummy_user = "foo"
        roles = self.graylog_api.get_auth_roles_of_user(dummy_user)
        self.assertIsInstance(roles, GraylogApiResult)
        self.graylog_api._rest_adapter.get.assert_called_once_with(f"authz/roles/user/{dummy_user}", None)

    def test_get_auth_role_by_id(self):
        dummy_id = "foo"
        role = self.graylog_api.get_auth_role_by_id(dummy_id)
        self.assertIsInstance(role, GraylogApiResult)
        self.graylog_api._rest_adapter.get.assert_called_once_with(f"authz/roles/{dummy_id}")

    def test_get_auth_assignees_of_role(self):
        dummy_id = "foo"
        assignees = self.graylog_api.get_auth_assignees_of_role(dummy_id)
        self.assertIsInstance(assignees, GraylogApiResult)
        self.graylog_api._rest_adapter.get.assert_called_once_with(f"authz/roles/{dummy_id}/assignees", None)

    # /ca
    def test_get_ca(self):
        ca = self.graylog_api.get_ca()
        self.assertIsInstance(ca, GraylogApiResult)
        self.graylog_api._rest_adapter.get.assert_called_once_with("ca")

    # /certificates
    def test_get_certificates(self):
        certs = self.graylog_api.get_certificates()
        self.assertIsInstance(certs, GraylogApiResult)
        self.graylog_api._rest_adapter.get.assert_called_once_with("certificates")

    # /cluster
    def test_get_cluster(self):
        cluster = self.graylog_api.get_cluster()
        self.assertIsInstance(cluster, GraylogApiResult)
        self.graylog_api._rest_adapter.get.assert_called_once_with("cluster")

    def test_get_processbufferdump_no_id(self):
        dump = self.graylog_api.get_processbufferdump()
        self.assertIsInstance(dump, GraylogApiResult)
        self.graylog_api._rest_adapter.get.assert_called_once_with("cluster/processbufferdump")

    def test_get_processbufferdump_with_id(self):
        dummy_id = "foo"
        dump = self.graylog_api.get_processbufferdump(dummy_id)
        self.assertIsInstance(dump, GraylogApiResult)
        self.graylog_api._rest_adapter.get.assert_called_once_with(f"cluster/{dummy_id}/processbufferdump")

    def test_get_jvminfo(self):
        dummy_id = "foo"
        jvm_info = self.graylog_api.get_jvminfo(dummy_id)
        self.assertIsInstance(jvm_info, GraylogApiResult)
        self.graylog_api._rest_adapter.get.assert_called_once_with(f"cluster/{dummy_id}/jvm")

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
    # /plugins/SecurityApp/Assets
    def test_securityapp_assets_share_rest_adapter(self):
        security_app = self.graylog_api.plugins.SecurityApp

        self.assertIs(security_app._rest_adapter, self.graylog_api._rest_adapter)
        self.assertIs(security_app.Assets._rest_adapter, self.graylog_api._rest_adapter)

    def test_get_securityapp_assets_defaults(self):
        result = self.graylog_api.plugins.SecurityApp.Assets.get_assets()

        self.assertIs(result, self.graylog_api._rest_adapter.get.return_value)
        self.graylog_api._rest_adapter.get.assert_called_once_with(
            "plugins/org.graylog.plugins.securityapp.asset/assets",
            {
                "sort": "name",
                "page": 1,
                "per_page": 15,
                "query": "",
                "filters": "",
                "direction": "asc",
            },
        )

    def test_get_securityapp_assets_custom_parameters(self):
        parameters = {
            "sort": "risk_score",
            "page": 2,
            "per_page": 30,
            "query": "server",
            "filters": "category:production",
            "direction": "desc",
        }

        result = self.graylog_api.plugins.SecurityApp.Assets.get_assets(**parameters)

        self.assertIs(result, self.graylog_api._rest_adapter.get.return_value)
        self.graylog_api._rest_adapter.get.assert_called_once_with(
            "plugins/org.graylog.plugins.securityapp.asset/assets", parameters
        )

    def test_create_securityapp_user_asset_defaults(self):
        result = self.graylog_api.plugins.SecurityApp.Assets.create_user_asset(
            name="Alice", usernames=["alice"]
        )

        self.assertIs(result, self.graylog_api._rest_adapter.post.return_value)
        self.graylog_api._rest_adapter.post.assert_called_once_with(
            "plugins/org.graylog.plugins.securityapp.asset/assets",
            data={
                "category": [],
                "details": {
                    "type": "user",
                    "usernames": ["alice"],
                    "user_ids": [],
                    "email_addresses": [],
                    "first_name": "",
                    "last_name": "",
                },
                "name": "Alice",
                "priority": 1,
            },
        )

    def test_create_securityapp_user_asset_custom_parameters(self):
        result = self.graylog_api.plugins.SecurityApp.Assets.create_user_asset(
            name="Alice Example", usernames=["alice", "a.example"],
            user_ids=["user-1"], email_addresses=["alice@example.com"],
            first_name="Alice", last_name="Example", category=["staff"], priority=0,
        )

        self.assertIs(result, self.graylog_api._rest_adapter.post.return_value)
        self.graylog_api._rest_adapter.post.assert_called_once_with(
            "plugins/org.graylog.plugins.securityapp.asset/assets",
            data={
                "category": ["staff"],
                "details": {
                    "type": "user",
                    "usernames": ["alice", "a.example"],
                    "user_ids": ["user-1"],
                    "email_addresses": ["alice@example.com"],
                    "first_name": "Alice",
                    "last_name": "Example",
                },
                "name": "Alice Example",
                "priority": 0,
            },
        )

    def test_create_securityapp_machine_asset_defaults(self):
        result = self.graylog_api.plugins.SecurityApp.Assets.create_machine_asset(
            name="Server", hostnames=["server.example.com"]
        )

        self.assertIs(result, self.graylog_api._rest_adapter.post.return_value)
        self.graylog_api._rest_adapter.post.assert_called_once_with(
            "plugins/org.graylog.plugins.securityapp.asset/assets",
            data={
                "category": [],
                "details": {
                    "type": "machine",
                    "hostnames": ["server.example.com"],
                    "ip_addresses": [],
                    "mac_addresses": [],
                    "custom_fields": {},
                    "description": "",
                    "geo_info": {},
                    "owner": "",
                },
                "name": "Server",
                "priority": 1,
            },
        )

    def test_create_securityapp_machine_asset_custom_parameters(self):
        result = self.graylog_api.plugins.SecurityApp.Assets.create_machine_asset(
            name="Production server", hostnames=["server.example.com", "server"],
            ip_addresses=["192.0.2.1"], mac_addresses=["00:11:22:33:44:55"],
            category=["production"], custom_fields={"team": "operations"},
            description="Application server", geo_info={"country": "DE"},
            owner="operations", priority=0,
        )

        self.assertIs(result, self.graylog_api._rest_adapter.post.return_value)
        self.graylog_api._rest_adapter.post.assert_called_once_with(
            "plugins/org.graylog.plugins.securityapp.asset/assets",
            data={
                "category": ["production"],
                "details": {
                    "type": "machine",
                    "hostnames": ["server.example.com", "server"],
                    "ip_addresses": ["192.0.2.1"],
                    "mac_addresses": ["00:11:22:33:44:55"],
                    "custom_fields": {"team": "operations"},
                    "description": "Application server",
                    "geo_info": {"country": "DE"},
                    "owner": "operations",
                },
                "name": "Production server",
                "priority": 0,
            },
        )

    def test_add_categories_to_multiple_securityapp_assets(self):
        asset_ids = ["asset-1", "asset-2"]
        categories = ["production", "servers"]

        result = self.graylog_api.plugins.SecurityApp.Assets.add_categories_to_multiple_assets(
            asset_ids=asset_ids, categories=categories
        )

        self.assertIs(result, self.graylog_api._rest_adapter.put.return_value)
        self.graylog_api._rest_adapter.put.assert_called_once_with(
            "plugins/org.graylog.plugins.securityapp.asset/assets/bulk/categories_add",
            data={"asset_ids": asset_ids, "categories": categories},
        )

    def test_get_securityapp_asset_by_id_detailed(self):
        asset_id = "asset-1"

        result = self.graylog_api.plugins.SecurityApp.Assets.get_asset_by_id_detailed(asset_id)

        self.assertIs(result, self.graylog_api._rest_adapter.get.return_value)
        self.graylog_api._rest_adapter.get.assert_called_once_with(
            f"plugins/org.graylog.plugins.securityapp.asset/assets/{asset_id}"
        )

    def test_edit_securityapp_asset_by_id(self):
        asset_id = "asset-1"
        updates = {"name": "updated-server", "priority": 0, "category": []}
        existing_data = {
            "id": asset_id,
            "name": "original-server",
            "priority": 1,
            "category": ["production"],
            "details": {"type": "machine", "hostnames": ["server.example.com"]},
        }
        expected_data = {**existing_data, **updates}
        self.graylog_api._rest_adapter.get.return_value = GraylogApiResult(200, data=existing_data)

        result = self.graylog_api.plugins.SecurityApp.Assets.edit_asset_by_id(asset_id, **updates)

        self.assertIs(result, self.graylog_api._rest_adapter.put.return_value)
        self.graylog_api._rest_adapter.get.assert_called_once_with(
            f"plugins/org.graylog.plugins.securityapp.asset/assets/{asset_id}"
        )
        self.graylog_api._rest_adapter.put.assert_called_once_with(
            f"plugins/org.graylog.plugins.securityapp.asset/assets/{asset_id}", data=expected_data
        )

    def test_edit_securityapp_asset_by_id_without_updates(self):
        asset_id = "asset-1"
        existing_data = {"id": asset_id, "name": "server", "priority": 1}
        self.graylog_api._rest_adapter.get.return_value = GraylogApiResult(200, data=existing_data.copy())

        result = self.graylog_api.plugins.SecurityApp.Assets.edit_asset_by_id(asset_id)

        self.assertIs(result, self.graylog_api._rest_adapter.put.return_value)
        self.graylog_api._rest_adapter.get.assert_called_once_with(
            f"plugins/org.graylog.plugins.securityapp.asset/assets/{asset_id}"
        )
        self.graylog_api._rest_adapter.put.assert_called_once_with(
            f"plugins/org.graylog.plugins.securityapp.asset/assets/{asset_id}", data=existing_data
        )

    def test_delete_securityapp_asset_by_id(self):
        asset_id = "asset-1"

        result = self.graylog_api.plugins.SecurityApp.Assets.delete_asset_by_id(asset_id)

        self.assertIs(result, self.graylog_api._rest_adapter.delete.return_value)
        self.graylog_api._rest_adapter.delete.assert_called_once_with(
            f"plugins/org.graylog.plugins.securityapp.asset/assets/{asset_id}"
        )

    # /remote-reindex-migration
    # /roles
    # /views/search Search
    # /search Search Options (Decorators, Export, Functions etc.)
    def test_post_search_query(self):
        dummy_query = "foo"
        dummy_start = 0
        dummy_timerange = {"type": "relative", "range": 300}
        dummy_streams = ["stream1", "stream2"]
        dummy_stream_categories = ["category1", "category2"]
        dummy_sort = "timestamp"
        dummy_sort_order = "Ascending"
        dummy_fields = ["field1", "field2"]
        dummy_size = 100

        result = self.graylog_api.post_search_query(
            query=dummy_query,
            start=dummy_start,
            timerange=dummy_timerange,
            streams=dummy_streams,
            stream_categories=dummy_stream_categories,
            sort=dummy_sort,
            sort_order=dummy_sort_order,
            fields=dummy_fields,
            size=dummy_size
        )

        self.assertIsInstance(result, GraylogApiResult)
        self.graylog_api._rest_adapter.post.assert_called_once_with(
            "search/messages",
            data={
                "query": dummy_query,
                "from": str(dummy_start),
                "timerange": dummy_timerange,
                "streams": dummy_streams,
                "stream_categories": dummy_stream_categories,
                "sort": dummy_sort,
                "sort_order": dummy_sort_order,
                "fields": dummy_fields,
                "size": str(dummy_size),
            }
        )

    # /views/searchjobs Searchjobs
    # /sidecars
    # /sidecar
    # /startpage
    # /system/inputs/{inputId}/staticfields Staticfields
    # /streams
    def test_get_streams(self):
        streams = self.graylog_api.get_streams()
        self.assertIsInstance(streams, GraylogApiResult)
        self.graylog_api._rest_adapter.get.assert_called_once_with("streams")

    # /system Main System endpoints
    # /telemetry
    # /token_usage
    # /users
    def test_create_user(self):
        dummy_data = {"username": "foo", "first_name": "bar", "last_name": "baz", "email": "foo@bar.baz", "password": "secret", "permissions": ["read:foo"]}
        user = self.graylog_api.create_user(**dummy_data)
        self.assertIsInstance(user, GraylogApiResult)
        self.graylog_api._rest_adapter.post.assert_called_once_with("users", data={**dummy_data})

    def test_get_users(self):
        users = self.graylog_api.get_users()
        self.assertIsInstance(users, GraylogApiResult)
        self.graylog_api._rest_adapter.get.assert_called_once_with("users", None)

    def test_get_users_paginated(self):
        users = self.graylog_api.get_users_paginated()
        self.assertIsInstance(users, GraylogApiResult)
        self.graylog_api._rest_adapter.get.assert_called_once_with("users/paginated", None)

    def test_get_user_by_id(self):
        dummy_id = "foo"
        user = self.graylog_api.get_user_by_id(dummy_id)
        self.assertIsInstance(user, GraylogApiResult)
        self.graylog_api._rest_adapter.get.assert_called_once_with(f"users/id/{dummy_id}")

    def test_get_user_by_username(self):
        dummy_user = "foo"
        user = self.graylog_api.get_user_by_username(dummy_user)
        self.assertIsInstance(user, GraylogApiResult)
        self.graylog_api._rest_adapter.get.assert_called_once_with(f"users/{dummy_user}")

    def test_get_user_tokens_by_id(self):
        dummy_id = "foo"
        user = self.graylog_api.get_user_tokens_by_id(dummy_id)
        self.assertIsInstance(user, GraylogApiResult)
        self.graylog_api._rest_adapter.get.assert_called_once_with(f"users/{dummy_id}/tokens")

    def test_delete_user_by_id(self):
        dummy_id = "foo"
        result = self.graylog_api.delete_user_by_id(dummy_id)
        self.assertIsInstance(result, GraylogApiResult)
        self.graylog_api._rest_adapter.delete.assert_called_once_with(f"users/id/{dummy_id}")

    def test_delete_user_by_username(self):
        dummy_user = "foo"
        result = self.graylog_api.delete_user_by_username(dummy_user)
        self.assertIsInstance(result, GraylogApiResult)
        self.graylog_api._rest_adapter.delete.assert_called_once_with(f"users/{dummy_user}")

    def test_change_user_status_valid(self):
        dummy_id = "foo"
        for status in ["enabled", "disabled", "deleted"]:
            with self.subTest(status=status):
                result = self.graylog_api.change_user_status(dummy_id, status)
                self.assertIsInstance(result, GraylogApiResult)
                self.graylog_api._rest_adapter.put.assert_called_once_with(f"users/{dummy_id}/status/{status}")
                self.graylog_api._rest_adapter.put.reset_mock()

    def test_change_user_status_invalid(self):
        dummy_id = "foo"
        with self.assertRaises(ValueError):
            self.graylog_api.change_user_status(dummy_id, "invalid_status")

    # /views Main Views Endpoints
    def test_get_views(self):
        views = self.graylog_api.get_views()
        self.assertIsInstance(views, GraylogApiResult)
        self.graylog_api._rest_adapter.get.assert_called_once_with("views", None)

    def test_get_view_by_id(self):
        dummy_id = "foo"
        view = self.graylog_api.get_view_by_id(dummy_id)
        self.assertIsInstance(view, GraylogApiResult)
        self.graylog_api._rest_adapter.get.assert_called_once_with(f"views/{dummy_id}")
