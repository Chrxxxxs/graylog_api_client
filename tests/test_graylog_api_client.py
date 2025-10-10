from unittest import TestCase, mock

from src.graylog_api_client.data_structures import GraylogApiResult
from src.graylog_api_client.graylog_api_client import GraylogAPI


class TestGraylogApiClient(TestCase):
    def setUp(self):
        self.graylog_api = GraylogAPI("", "")
        self.graylog_api._rest_adapter.get = mock.Mock(spec=["endpoint", "parameters"],
                                                        return_value=GraylogApiResult(200))
        self.graylog_api._rest_adapter.post = mock.Mock(spec=["endpoint", "parameters", "data"],
                                                        return_value=GraylogApiResult(200))
        self.graylog_api._rest_adapter.delete = mock.Mock(spec=["endpoint", "parameters", "data"],
                                                        return_value=GraylogApiResult(200))
        self.graylog_api._rest_adapter.put = mock.Mock(spec=["endpoint", "parameters", "data"],
                                                        return_value=GraylogApiResult(200))

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
    def test_get_streams(self):
        streams = self.graylog_api.get_streams()
        self.assertIsInstance(streams, GraylogApiResult)
        self.graylog_api._rest_adapter.get.assert_called_once_with("streams")

    # /system Main System endpoints
    # /telemetry
    # /token_usage
    # /users
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
